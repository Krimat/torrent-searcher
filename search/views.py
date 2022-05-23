from django.shortcuts import render
from requests import get, post
from bs4 import BeautifulSoup
import json


from .forms import SearchForm
from .loaders import PirateBayLoader



def index(request):
    if request.method == 'GET':

        search = SearchForm(request.GET)

        context = {
            'form': search,
        }
        if search.data:
            context['data'] = PirateBayLoader.load(search.data.get('search_request'))

        return render(
            template_name='search/index.html',
            request=request,
            context=context,
        )
