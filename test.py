import requests

appid = '8231d793028bb94abe760a02c187eef6'
q = 'Lugu'
# url = 'https://samples.openweathermap.org/data/2.5/weather?q=' + q + '&appid=' + appid
lat = str(25)
lon = str(121)
# url = 'https://samples.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&' + q + '&appid=' + appid
url = 'http://www.google.com/ig/cities?country=cn'
res = requests.get(url)

print(res.json())

{
    'coord': {'lon': -0.13, 'lat': 51.51},
    'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}],
    'base': 'stations',
    'main': {'temp': 280.32, 'pressure': 1012, 'humidity': 81, 'temp_min': 279.15, 'temp_max': 281.15},
    'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 80}, 'clouds': {'all': 90}, 'dt': 1485789600,
    'sys': {'type': 1, 'id': 5091, 'message': 0.0103, 'country': 'GB', 'sunrise': 1485762037, 'sunset': 1485794875},
    'id': 2643743, 'name': 'London', 'cod': 200
}
