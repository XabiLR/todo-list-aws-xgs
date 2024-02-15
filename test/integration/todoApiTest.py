import os
import unittest
import requests
import json
import pytest

with open('env.properties') as f:
    for line in f:
        if '=' in line:
            key, value = line.split('=', 1)
            os.environ[key.strip()] = value.strip()

BASE_URL = os.environ.get("BASE_URL")
BASE_URL = "https://v5d7cgb6s3.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # en segundos

print("AAAAA")
print(BASE_URL)
print("BBBB")

@pytest.mark.api
class TestApi(unittest.TestCase):

    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODOOOOOOOO')
        # Agregar TODO
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add Todo: ' + str(json_response))
        try:
            jsonbody = json.loads(json_response['body'])
            ID_TODO = jsonbody['id']
            print('ID todo:' + ID_TODO)
        except KeyError as e:
            print('Error al procesar la respuesta:', e)
            self.fail('Error al procesar la respuesta: clave faltante')
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example", f"Error en la petición API a {url}"
        )
        # Listar
        url = BASE_URL + "/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertTrue(response.json())

        print('End - integration test List TODO')

    def test_api_addtodo(self):
        print('---------------------------------------')
        print('Starting - integration test Add TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        try:
            print('Response Add Todo: ' + json_response['body'])
            jsonbody = json.loads(json_response['body'])
            ID_TODO = jsonbody['id']
            print('ID todo:' + ID_TODO)
        except KeyError as e:
            print('Error al procesar la respuesta:', e)
            self.fail('Error al procesar la respuesta: clave faltante')
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example", f"Error en la petición API a {url}"
        )
        url = url + "/" + ID_TODO
        response = requests.delete(url)
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        print('End - integration test Add TODO')

    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - integration test Get TODO')
        # Agregar TODO
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - GET"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add Todo: ' + str(json_response))
        try:
            jsonbody = json.loads(json_response['body'])
            ID_TODO = jsonbody['id']
            print('ID todo:' + ID_TODO)
        except KeyError as e:
            print('Error al procesar la respuesta:', e)
            self.fail('Error al procesar la respuesta: clave faltante')
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example - GET", f"Error en la petición API a {url}"
        )
        # Prueba GET TODO
        url = BASE_URL + "/todos/" + ID_TODO
        response = requests.get(url)
        json_response = response.json()
        print('Response Get Todo: ' + str(json_response))
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response['text'], "Integration text example - GET", f"Error en la petición API a {url}"
        )
        # Eliminar TODO para restaurar el estado
        response = requests.delete(url)
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        print('End - integration test Get TODO')

    def test_api_updatetodo(self):
        print('---------------------------------------')
        print('Starting - integration test Update TODO')
        # Agregar TODO
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - Initial"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add todo: ' + json_response['body'])
        try:
            jsonbody = json.loads(json_response['body'])
            ID_TODO = jsonbody['id']
            print('ID todo:' + ID_TODO)
        except KeyError as e:
            print('Error al procesar la respuesta:', e)
            self.fail('Error al procesar la respuesta: clave faltante')
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example - Initial", f"Error en la petición API a {url}"
        )
        # Actualizar TODO
        url = BASE_URL + "/todos/" + ID_TODO
        data = {
            "text": "Integration text example - Modified",
            "checked": "true"
        }
        response = requests.put(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Update todo: ' + str(json_response))
        # jsonbody= json.loads(json_response['body'])
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response['text'], "Integration text example - Modified", f"Error en la petición API a {url}"
        )
        # Prueba GET TODO
        url = BASE_URL + "/todos/" + ID_TODO
        response = requests.get(url)
        json_response = response.json()
        print('Response Get Todo: ' + str(json_response))
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response['text'], "Integration text example - Modified", f"Error en la petición API a {url}"
        )
        # Eliminar TODO para restaurar el estado
        response = requests.delete(url)
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        print('End - integration test Update TODO')

    def test_api_deletetodo(self):
        print('---------------------------------------')
        print('Starting - integration test Delete TODO')
        # Agregar TODO
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - Initial"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add todo: ' + json_response['body'])
        try:
            jsonbody = json.loads(json_response['body'])
            ID_TODO = jsonbody['id']
            print('ID todo:' + ID_TODO)
        except KeyError as e:
            print('Error al procesar la respuesta:', e)
            self.fail('Error al procesar la respuesta: clave faltante')
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example - Initial", f"Error en la petición API a {url}"
        )
        # Eliminar TODO para restaurar el estado
        response = requests.delete(url + '/' + ID_TODO)
        self.assertEqual(
            response.status_code, 200, f"Error en la petición API a {url}"
        )
        print('Response Delete Todo:' + str(response))
        # Prueba GET TODO
        url = BASE_URL + "/todos/" + ID_TODO
        response = requests.get(url)
        print('Response Get Todo ' + url + ': ' + str(response))
        self.assertEqual(
            response.status_code, 404, f"Error en la petición API a {url}"
        )
        print('End - integration test Delete TODO')

if __name__ == "__main__":
    unittest.main()
