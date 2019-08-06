'''
Software in python convert purchases another currency and calcule purchase IOF
Created by Marcos Vinicius
'''

import json
from requests import Session
from datetime import date, timedelta


def get_full_url(currency, date_ptax):
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia"
    param = "(moeda=@moeda,dataCotacao=@dataCotacao)?%40moeda='{}'&%40dataCotacao='{}'&%24format=json&%24" \
            "select=cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim".format(currency, date_ptax)
    return "{}{}".format(url,param)


def get_api(currency, date_ptax):
    response = Session().get(get_full_url(currency, date_ptax))
    response.encoding = 'utf-8'
    return json.loads(response.text)


def get_ptax(currency, date_ptax):
    date_str = date_ptax.strftime("%m-%d-%Y")
    price = get_api(currency, date_str)
    return [x for x in price['value'] if x['tipoBoletim'] == 'Fechamento PTAX'][0]


currency = 'USD'
date_ptax = date.today()
value = [14.59, 21.59, 73.49, 31.87, 14.32]

ptax = get_ptax(currency, date_ptax)

less_days = 1
while(ptax is None):
    date_ptax = date.today() - timedelta(days=less_days)
    less_days += less_days
    ptax = get_ptax(currency, date_ptax)

ptax_buy = float(ptax['cotacaoCompra'])
converted_value = [round(((x*ptax_buy)+((x*ptax_buy)*0.0638)), 2) for x in value]

print('Ptax: {} consolidate in {}'.format(ptax_buy, ptax['dataHoraCotacao']))
print(value)
print(converted_value)
