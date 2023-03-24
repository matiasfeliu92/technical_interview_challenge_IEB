import unittest
from django.urls import reverse
from django.test import TestCase
import requests

def test_get_all_products():
    response = requests.get('http://localhost:8000/products')
    assert response.status_code == 200

def test_get_one_product():
    response = requests.get('http://localhost:8000/products/a04')
    res_body = response.json()
    assert res_body["code"] == "a04"

# def test_create_product():
#     body = {
#         "code": "a06",
#         "purchase_price": 754757,
#         "sale_price": 4634643,
#         "description": "fhfdhgffjf"
#     }
#     response = requests.post('http://localhost:8000/create', body)
#     assert response.status_code == 201

def test_update_product():
    body = {
        "code": "a06",
        "purchase_price": 754757,
        "sale_price": 4634643,
        "description": "BCDFGHJKLMNÑ"
    }
    response = requests.post('http://localhost:8000/update/a06', body)
    assert response.status_code == 201