from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    IntegerField
)

from report import models


class CrimeTypeSerializer(ModelSerializer):
    class Meta:
        model = models.CrimeType
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class StateSerializer(ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class AddressTypeSerializer(ModelSerializer):
    class Meta:
        model = models.AddressType
        fields = '__all__'


class ReportFilterSerializer(Serializer):
    date_from = IntegerField(required=False)
    date_to = IntegerField(required=False)
    page = IntegerField(
        min_value=1,
        required=False,
        default=1)
    limit = IntegerField(
        min_value=1,
        required=False,
        default=25)


class RepotSerializer(ModelSerializer):
    crime_type = CrimeTypeSerializer(many=False)
    city = CitySerializer(many=False)
    state = StateSerializer(many=False)
    address_type = AddressTypeSerializer(many=False)

    class Meta:
        model = models.Report
        fields = '__all__'
