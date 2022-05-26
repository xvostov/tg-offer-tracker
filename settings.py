import configparser

config = configparser.ConfigParser()
config.read('config.ini')

to_send_debug_info = config['Telegram']['to_send_debug_info']
bot_token = config['Telegram']['bot_token']
admins_list = [chat_id for chat_id in config['Telegram']['admins'].split(',') if chat_id]
api_token = config['Api']['api_token']
olx_api_token = config['olx']['api_token']
olx_api_address = config['olx']['address']