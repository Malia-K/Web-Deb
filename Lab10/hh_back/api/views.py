import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2}, status = 200)
    if request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company_desc = data.get('description', '')
        company_city = data.get('city', '')
        company_address = data.get('address', '')
        company = Company.objects.create(name=company_name, description=company_desc, city=company_city, address=company_address)
        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as dne:
        return JsonResponse({'error': str(dne)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json(), safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_category_name = data.get('name', company.name)
        company.name = new_category_name
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
    if request.method == 'POST':
        data = json.loads(request.body)
        vacancy_name = data.get('name', '')
        vacancy = Company.objects.create(name=vacancy_name)
        return JsonResponse(vacancy.to_json())

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as dne:
        return JsonResponse({'error': str(dne)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json(), safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_category_name = data.get('name', vacancy.name)
        vacancy.name = new_category_name
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})


def vacancy_top_ten(request):
    if request.method == 'GET':
        top_ten_vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        top_ten_vacancies_json = [v.to_json() for v in top_ten_vacancies]
        return JsonResponse(top_ten_vacancies_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def list_of_vacancies_by_company(request, company_id):
    try:
        vacancies_by_company = Vacancy.objects.all().filter(company_id=company_id)
        # print(vacancies_by_company)

    except Vacancy.DoesNotExist as dne:
        return JsonResponse({'error': str(dne)}, status=400)

    vacancies_by_company_json = [v.to_json() for v in vacancies_by_company]

    if request.method == 'GET':
        return JsonResponse(vacancies_by_company_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})