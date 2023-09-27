from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from .helpers import llm_response

@csrf_exempt
def load_documents(request: HttpRequest) -> JsonResponse:
    if request.method != "POST": return JsonResponse(status=500)
    
    #parse request json to dictionary
    data : list[str] = json.loads(request.body)["documents"];
    
    summary, time = llm_response.get_summary(data)
    print(time)
    response = {"summary":summary}
    return JsonResponse(response)

def chat_response(request: HttpRequest) -> JsonResponse:
    pass

def remove_document(request: HttpRequest) -> JsonResponse:
    pass

