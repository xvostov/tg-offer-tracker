import requests
from flask import request
from loader import bot, app, msg_pool
from offer import Offer
from settings import api_token
from waitress import serve
import threading
import requests
from requests.exceptions import HTTPError


@app.route('/offer', methods=['POST'])
def send_msg():
    request_json = request.get_json()
    request_token = request_json.get('token', '')
    if request_token == api_token:
        offer = Offer()
        offer.url = request_json['url']
        offer.title = request_json['title']
        offer.id = request_json['id']
        offer.description = request_json['description']
        offer.price = request_json['price']
        offer.img_url = request_json['img_url']

        msg_pool.append(offer)
        return 'OK', 200

    else:
        return 'access denied', 401


def target():
    return serve(app, host="0.0.0.0", port=8080)


def listen():
    t = threading.Thread(target=target, daemon=True)
    t.start()



# def base_request_to_api(cmd, url, token):
#     resp = requests.post(f'http://{olx_api_address}/categories', json={
#         'token': token,
#         'cmd': cmd,
#         'url': url
#     }, timeout=1)

    # if resp.status_code != 200:
    #     raise HTTPError(f'Неверный ответ сервера, статус код: {resp.status_code}')


# def add_category(url):
#     # return base_request_to_api(cmd='add', url=url, token=olx_api_token)
#
#
# def remove_category(url):
#     # return base_request_to_api(cmd='remove', url=url, token=olx_api_token)


# def get_categories():
    # resp = requests.get(f'http://{olx_api_address}/categories', json={'token': olx_api_token}, timeout=1)
    #
    # if resp.status_code != 200:
    #     raise HTTPError(f'Неверный ответ сервера, статус код: {resp.status_code}')
    #
    #
    # return resp.json()['categories']
