from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import *
import json

def load_documents(request: HttpRequest) -> JsonResponse:
    if request.method != "POST": return JsonResponse(status=500)
    
    #parse request json to dictionary
    data : list[str] = json.loads(request.body);

    print(data)
    response = {"message":"dummy"}
    return JsonResponse(response)

def chat_response(request: HttpRequest) -> JsonResponse:
    pass

def remove_document(request: HttpRequest) -> JsonResponse:
    pass

