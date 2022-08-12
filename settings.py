# import configparser
import os


# config = configparser.ConfigParser()
# config.read('config.ini')

# to_send_debug_info = config['Telegram']['to_send_debug_info']
# bot_token = config['Telegram']['bot_token']
# admins_list = [chat_id for chat_id in config['Telegram']['admins'].split(',') if chat_id]
# api_token = config['Api']['api_token']
# olx_api_token = config['olx']['api_token']
# olx_api_address = config['olx']['address']

to_send_debug_info = os.environ.get('to_send_debug_info')
bot_token = os.environ.get('bot_token')
admins_list = [chat_id for chat_id in os.environ.get('admins').split(',') if chat_id]
api_token = os.environ.get('api_token')
# olx_api_token = os.environ.get('olx_api_token')
# olx_api_address = os.environ.get('olx_api_address')



# # Database
# db_user = config['Database']['db_user']
# db_password = config['Database']['db_password']
# db_host = config['Database']['db_host']
# db_port = int(config['Database']['db_port'])
# db_name = config['Database']['db_name']

# Database
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_host = os.environ.get('db_host')
db_port = int(os.environ.get('db_port'))
db_name = os.environ.get('db_name')