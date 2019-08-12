from django.shortcuts import render
from django.core.paginator import Paginator

from app.useAPI.service import *

# Create your views here.

def api_list(request):
    results = []
    if request.method == 'GET':
        results_list = get_results()
        paginator = Paginator(results_list, 3)
        page = request.GET.get('page')
        results = paginator.get_page(page)
    return render(request, 'index.html', {'results_list': results})