from django.shortcuts import JsonResponse
from data.models import DataPoint, DataSet, DataSource, Variable

def Reports(request):
    variables = Variable.objects.filter(name__in=['Diabetes Prevalence', 'Population'])
    data_points = DataPoint.objects.filter(variable__in=variables)

    report_data = []
    for location in data_points.values_list('location', flat=True).distinct():
        region_data = {
        'region': location.get_full_name(),  # Assuming get_full_name method in Location
        'diabetes_prevalence': data_points.filter(location=location, variable__name='diabetes_prevalence').average('value'),
        'population': data_points.filter(location=location, variable__name='population').sum('value'),
        }
        report_data.append(region_data)

    return JsonResponse(report_data, safe=False)
