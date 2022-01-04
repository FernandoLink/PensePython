import requests

requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = requisicao.json()
print('-'*30,'Cotação')
print(cotacao['USDBRL']['name'],cotacao['USDBRL']['bid'])
print(cotacao['EURBRL']['name'],cotacao['EURBRL']['bid'])
print(cotacao['BTCBRL']['name'],cotacao['BTCBRL']['bid'])

cep = 82900150
requisicao = requests.get('https://cep.awesomeapi.com.br/json/'+str(cep))
endereço = requisicao.json()
print('-'*30,'Endereço')
print(f'{endereço["address_type"]}: {endereço["address"]}')
print(f'Bairro: {endereço["district"]}')
print(f'CEP: {endereço["cep"]}')
print(f'Cidade: {endereço["city"]} - Estado: {endereço["state"]}')
print(f'IBGE: {endereço["city_ibge"]}')
print(f'DDD: {endereço["ddd"]}')
print(f'Latitude: {endereço["lat"]}')
print(f'Longitude: {endereço["lng"]}')
