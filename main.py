import csv
import os
from datetime import datetime

from tqdm import tqdm

from police_appeals.settings import CVS_FILE_PATH


def get_data_from_file(file_path: str):
    data = []
    number_rows = int(os.popen(f'wc -l < {file_path}').read()[:-1]) - 1

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in tqdm(reader, total=number_rows or 99, colour="green", desc="Считываение данных из файла"):
            data.append({
                "id": row.get('Crime Id'),
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


def main():
    raw_data = get_data_from_file(file_path=CVS_FILE_PATH)
    b = 1


if __name__ == "__main__":
    main()
