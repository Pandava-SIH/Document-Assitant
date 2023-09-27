from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from .helpers import llm_response
from .helpers.chat_store import chat_store
from uuid import uuid4

@csrf_exempt
def load_documents(request: HttpRequest) -> JsonResponse:
    if request.method != "POST": return JsonResponse(status=500)
    
    #parse request json to dictionary
    data : list[str] = json.loads(request.body);
    data, uid = data["documents"], data["uid"]
    
    summary, time = llm_response.get_summary(data)
    for i in data:
        chat_store.append({"role": "user", "content": i})
    chat_store.append({"role": "system", "content": summary})
    # db = Store(uid=uid, data="<-||->".join(data), summary=summary)
    # db.save()
    print(time)

    response = {"summary":summary}
    return JsonResponse(response)

def chat_response(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)["prompt"]
    res = llm_response.chat_reponse(data)
    return JsonResponse({"reply": res}, status=200)


def remove_document(request: HttpRequest) -> JsonResponse:
    pass

