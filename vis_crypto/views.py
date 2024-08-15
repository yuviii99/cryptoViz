from django.shortcuts import render
import os
import requests

def index(request):
    return render(request, "vis_crypto/base.html")

def fetch_coin_market_chart(crypto_coin='bitcoin', versus_currency='usd'):
    query_params = {
        'vs_currency': versus_currency,
        'days': 100,
        'interval': 'daily',
        'x_cg_demo_api_key': os.getenv('COINGECK_API_KEY')
    }
    headers={
        'accept': 'application/json',
    }
    api_endpoint = f'https://api.coingecko.com/api/v3/coins/{crypto_coin}/market_chart'
    response = requests.get(api_endpoint, params=query_params, headers=headers).json()
    return response
