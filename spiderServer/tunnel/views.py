from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.



def test(request):
    response_data = {}
    response_data['result'] = 'success'
    response_data['status'] = {}
    response_data['status']['message'] = 'the port is already opened and ready for development...'
    return HttpResponse(json.dumps(response_data), content_type="application/json")



