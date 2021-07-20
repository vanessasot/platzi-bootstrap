from django.http import HttpResponse
from django.views import View
from hackernewsApp import hackernewstop
import json


class HackerNewsStories(View):
    """ Show selected top stories """
    def get(self, request):
        
        headlines = hackernewstop.get_headlines(2, 4)
        
        return HttpResponse(json.dumps(headlines), content_type="application/json")