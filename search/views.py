# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
 
from .models import Meaning
 
 
class HomePageView(TemplateView):
	template_name = 'home.html'
 
class SearchResultsView(ListView):
	model = Meaning
	template_name = 'search_results.html'

	def get_queryset(self): # новый
		query = self.request.GET.get('q')
		object_list = Meaning.objects.filter(word__icontains=query)
		return object_list