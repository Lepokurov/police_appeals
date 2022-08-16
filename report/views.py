from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, InvalidPage

from report.models import Report
from report.serializers import ReportFilterSerializer, RepotSerializer


class ReportsListView(APIView):

    def get(self, request):
        serializer = ReportFilterSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.validated_data
        queryset = Report.objects.all().order_by("id")
        try:
            date_from = (
                datetime.utcfromtimestamp(int(data.get('date_from', 0)))
                if data.get('date_from', 0)
                else None
            )
            date_to = (
                datetime.utcfromtimestamp(int(data.get('date_to', 0)))
                if data.get('date_to', 0)
                else None
            )

        except ValueError:
            return Response('Bad date param, required timestamp in seconds', status=400)

        page = data.get("page", 1)
        limit = data.get("limit", 100)
        if date_from:
            queryset = queryset.filter(report_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(report_date__lte=date_to)
        paginator = Paginator(queryset, limit)
        try:
            reports = paginator.page(page)
        except InvalidPage:
            return Response({"total": paginator.count, "data": []})
        report_serializer = RepotSerializer(reports, many=True)
        return Response({"total": paginator.count, "data": report_serializer.data})
