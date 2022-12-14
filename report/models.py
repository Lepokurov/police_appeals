from django.db import models


class CrimeType(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)


class City(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)


class State(models.Model):
    code = models.CharField(primary_key=True, blank=False, max_length=100, null=False)


class AddressType(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)


class Report(models.Model):
    id = models.BigIntegerField(primary_key=True)
    crime_type = models.ForeignKey(
        CrimeType,
        on_delete=models.CASCADE,
        default=None,
    )
    report_date = models.DateTimeField(
        blank=True, null=False)
    call_data = models.DateTimeField(
        blank=True, null=False)
    offense_date = models.DateTimeField(
        blank=True, null=False)
    call_time = models.CharField(blank=False, max_length=100, null=False)
    call_datetime = models.DateTimeField(
        blank=True, null=False)
    disposition = models.CharField(blank=False, max_length=100, null=False)
    address = models.CharField(blank=False, max_length=100, null=False)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        default=None,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        default=None,
    )
    agency_id = models.CharField(blank=False, max_length=100, null=True)
    address_type = models.ForeignKey(
        AddressType,
        on_delete=models.CASCADE,
        default=None,
    )
    common_location = models.CharField(blank=False, max_length=100, null=True)
