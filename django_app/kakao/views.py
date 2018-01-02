import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def keyboard(request):
    return JsonResponse({
        "type" : "buttons",
        "buttons" : ["암호화폐 시세조회하기", "선택 2", "선택 3"]
    })


@csrf_exempt
def message(request):
    message = (request.body).decode('utf-8')
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    if return_str == '암호화폐 시세조회하기':
        return JsonResponse({
            'message': {
                'text': "시세 조회할 암호화폐를 입력하세요"
            },
            'keyboard': {
                'type': 'text'  # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
            }
        })


