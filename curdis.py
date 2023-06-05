import requests
import json
"""
    TODO:
    implement init function that will authenticate user and get his app id
    implement Channel, Message, Guild classes and their _api (get, delete, create)
    implement WebSocket events like MESSAGE_CREATE, MESSAGE_DELETE, INTERACTION_CREATE
"""
api = "https://discord.com/api/v9"
class DiscordAPI:
    def __init__(self, token):
        self.__token = token
        self._headers = {
            "Authorization": f"Bot {self.__token}"
        }
        response = requests.get(f"{api}/gateway/bot", headers=self._headers)
        response.raise_for_status()
        self.api_url = json.loads(response.text)
        self.app_id = self._getAppId()
    def _getAppId(self):
        response = requests.get(f"{api}/oauth2/applications/@me" , headers=self._headers)
        response.raise_for_status()
        app_data = json.loads(response.text)
        return app_data['id']
    def send_message(self, message, channel_id):
        payload = {
            'content': message
        }
        response = requests.post(f"{api}/channels/{channel_id}/messages", headers=self._headers, json=payload)
        response.raise_for_status()
    def delete_mesage(self, message_id, channel_id):
        response = requests.delete(f"{api}/channels/{channel_id}/messages/{message_id}", headers=self._headers)
        response.raise_for_status()
        


        
   