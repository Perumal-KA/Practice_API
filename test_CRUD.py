import pytest
import requests

def test_post_token_req():
    payload={"username":"admin",
    "password":"password123"}
    response=requests.post('https://restful-booker.herokuapp.com/auth', json=payload)
    print(response.text)
    print(response.status_code)


def test_post_req():
    payload_post_data= {'firstname': "perumal", 'lastname': "vj", 'totalprice': 111, 'depositpaid': True,
                        'bookingdates': {
                            "checkin": "2018-01-01",
                            "checkout": "2019-01-01"
                        }, 'additionalneeds': "Breakfast"}
    headers={"content-type":"application/json"}

    response=requests.post('https://restful-booker.herokuapp.com/booking',json=payload_post_data,headers=headers)
    print(response.text)
    print(response.status_code)
    print(response.headers)

def test_get_req():
    response=requests.get(url='https://restful-booker.herokuapp.com/booking/2845')
    print(response.status_code)
    print(response.text)

def test_put_req():
    headers={"content-type":"application/json"
             'Accept: application/json'
             }
    payload_put_data={'firstname': "perumal", 'lastname': "vj", 'totalprice': 111, 'depositpaid': True,
                        'bookingdates': {
                            "checkin": "2018-01-01",
                            "checkout": "2019-01-01"
                        }, 'additionalneeds': "Breakfast"}
    response = requests.post('https://restful-booker.herokuapp.com/booking/firstname=perumal&lastname=vj', json=payload_put_data, headers=headers)
    print(response.text)
    print(response.status_code)
    print(response.headers)

