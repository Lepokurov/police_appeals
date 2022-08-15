import csv
import os
from datetime import datetime

from django.core.management import BaseCommand
from tqdm import tqdm

from police_appeals.settings import CVS_FILE_PATH
from report.models import CrimeType, City, State, Report, AddressType


class Command(BaseCommand):
    help = 'Загрузка данных в бд'

    def get_data_csv_from_file(self, file_path: str):
        data = []
        number_rows = int(os.popen(f'wc -l < {file_path}').read()[:-1]) - 1

        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in tqdm(reader, total=number_rows or 99, colour="green", desc="Считываение данных из файла"):
                data.append({
                    "id": int(row.get('Crime Id')),
                    "crime_type": row.get('Original Crime Type Name'),
                    "report_date": datetime.fromisoformat(row.get('Report Date')),
                    "call_data": datetime.fromisoformat(row.get('Call Date')),
                    "offense_date": datetime.fromisoformat(row.get('Offense Date')),
                    "call_time": row.get("Call Time"),
                    'call_datetime': datetime.fromisoformat(row.get('Call Date Time')),
                    'disposition': row.get('Disposition'),
                    'address': row.get('Address'),
                    'city': row.get("City"),
                    "state": row.get("State"),
                    'agency_id': row.get("Agency Id"),
                    'address_type': row.get("Address Type"),
                    "common_location": row.get('Common Location')
                })
        return data

    def inset_data(self, raw_data):
        new_report_count = 0
        reports = []
        crime_types = {}
        cities = {}
        states = {}
        address_types = {}
        created_report_ids = Report.objects.all().values_list('id', flat=True)
        for row in tqdm(raw_data, colour='green', desc='Сохранение данных в БД'):
            crime_type_name = row.pop('crime_type')
            city_name = row.pop('city')
            state_code = row.pop('state')
            address_type_name = row.pop('address_type')
            crime_type = crime_types.get(crime_type_name)
            if not crime_type:
                crime_type, _ = CrimeType.objects.get_or_create(name=crime_type_name)
                crime_types[crime_type_name] = crime_type
            city = cities.get(city_name)
            if not city:
                city, _ = City.objects.get_or_create(name=city_name)
                cities[city_name] = city
            state = states.get(state_code)
            if not state:
                state, _ = State.objects.get_or_create(code=state_code)
                states[state_code] = state
            address_type = address_types.get(address_type_name)
            if not address_type:
                address_type, _ = AddressType.objects.get_or_create(name=address_type_name)
                address_types[address_type_name] = address_type
            if row.get("id") in created_report_ids:
                continue
            reports.append(Report(crime_type=crime_type, city=city, state=state, address_type=address_type, **row))
            new_report_count += 1
        Report.objects.bulk_create(reports)
        print(f'Add {new_report_count} rows to DB')

    def handle(self, *args, **kwargs):
        raw_data = self.get_data_csv_from_file(file_path=CVS_FILE_PATH)
        self.inset_data(raw_data)
