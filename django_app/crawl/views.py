import requests
import json
import csv
import os
import datetime

#Bithumb in KRW and
#Bitfinex in USD.
from django.http import HttpResponse, JsonResponse


def crawl(request):
    _params = {"fsym":"ETH", "tsyms":"BTC,KRW", "markets":"Coinbase, Bithumb"}
    bit_thumb = requests.get("https://min-api.cryptocompare.com/data/price", params=_params)
    thumb = bit_thumb.json()
    print(thumb)

    _params = {"fsym":"ETH", "tsyms":"BTC,USD", "markets":"Coinbase, Bitfinix"}
    bit_finix = requests.get("https://min-api.cryptocompare.com/data/price", params=_params)
    finix = bit_finix.json()
    print(finix)

    return JsonResponse({
        'message': {
            'text': thumb
        },
    })


def korbit_api(request):
    _api = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=eth_krw")
    print(_api)
    
    return JsonResponse({
        'message': {
            'text': _api
        },
    })
