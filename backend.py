import requests

api_key='854e96f4e872d095ed95c98d4d7cfbc9'

def get_data(place,forecast_days=None,kind=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtred_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtred_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtred_data]
    if kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place = "London",forecast_days=3,kind="Sky"))