import requests, json, asyncio
from typing import *
from consts import *
from message import Message
from ws import WSBot

class DiscordAPI:
    def __init__(self, token):
        self.__token = token
        self.__headers = {
            "Authorization": f"Bot {self.__token}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{API}/gateway/bot", headers=self.__headers)
        response.raise_for_status()
        self.api_url = json.loads(response.text)
        self.app_id = self._getAppId()
        self.__message_handler = None
        self.__handlers = {}

    def _getAppId(self):
        response = requests.get(f"{API}/oauth2/applications/@me" , headers=self.__headers)
        response.raise_for_status()
        app_data = json.loads(response.text)
        return app_data["id"]
    
    def get_all_messages(self, channel_id):
        responce = requests.get(f"{API}/channels/{channel_id}/messages", headers=self.__headers)
        responce.raise_for_status()
        messages = json.loads(responce.text)

        messages = [Message(self.__token, message["content"], message["channel_id"], message["id"], message["author"]["id"]) for message in messages]
        return messages

    def send_message(self, message=None, channel_id=None, files=None):
        headers = {
            "Authorization": f"Bot {self.__token}"
        }
        payload = {
            "content": message
        }
        response = requests.post(f"{API}/channels/{channel_id}/messages", headers=headers, json=payload,)
        response.raise_for_status()

    def register_commands(self):
        command_data = {
         "name": "hi",
         "description": "hello"
        }
        response = requests.post(f"{API}/applications/{self.app_id}/commands", headers=self.__headers, data=json.dumps(command_data))
        response.raise_for_status()

    def set_message_handler(self, handler):
        self.__message_handler = handler
    
    def add_handler(self, key: str, handler):
        self.__handlers[key] = handler

    def command(self, key: str):
        def wrapper(func: Callable):
            self.add_handler(key, func)
        return wrapper
    
    def message_handler(self):
        def wrapper(func):
            self.set_message_handler(func)
        return wrapper
    
    def listen(self):
        ws = WSBot(self.__token)
        asyncio.run(ws.run(self.__message_handler, self.__handlers))
