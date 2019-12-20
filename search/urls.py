from django.conf.urls import url

from .views import HomePageView, SearchResultsView

urlpatterns = [
    url(r'^search', SearchResultsView.as_view(), name='search_results'),
    url(r'', HomePageView.as_view(), name='home'),
]

