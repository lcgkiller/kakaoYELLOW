import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from bithumb.xcoin_api_client import XCoinAPI
from config import settings


def user_transactions(request):
    _api = json.loads(open(settings.base.CONFIG_SECRET_API).read())
    api_key = _api['bithumb']['connect_key']
    api_secret = _api['bithumb']['secret_key']

    api = XCoinAPI(api_key, api_secret)

    rgParams = {
        "order_currency" : "BTC",
        "payment_currency" : "KRW"
    }

    result = api.xcoinApiCall("/info/user_transactions", rgParams)
    print("result : ", result)
    return JsonResponse({"result": result})