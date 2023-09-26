from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

def load_documents(request: HttpRequest) -> JsonResponse:
    response = {"message":"dummy"}
    return JsonResponse(response)

def chat_response(request: HttpRequest) -> JsonResponse:
    pass

def remove_document(request: HttpRequest) -> JsonResponse:
    pass

