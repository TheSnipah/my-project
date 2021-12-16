import requests as requests

url = "https://ammtp.pythonanywhere.com/testapp/get_example"
response = requests.get(url)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)  # json

valor = response.json()['request']['path']
print(valor)

assert valor == "/testapp/get_example"
