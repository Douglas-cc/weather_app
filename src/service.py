import requests
from loguru import logger


def data_clima(city, api_key):
    # URL da Weatherstack API para obter a previsão do tempo atual
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'

    try:
        # Envia a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            data = response.json()        
            return {
                'city':data['location']['name'],
                'state':data['location']['region'],
                'uv_index':data['current']['uv_index'],
                'humidity':data['current']['humidity'],
                'weather_descriptions':data['current']['weather_descriptions'][0],
                'temperature':data['current']['temperature'],
                'icon':data['current']['weather_icons'][0],
                'wind_speed':data['current']['wind_speed']
            }
        else:
            logger.error(f'Erro na solicitação. Código de status: {response.status_code}')

    except requests.exceptions.RequestException as e:
        logger.error(f'Erro na solicitação: {e}')