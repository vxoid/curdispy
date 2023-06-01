import requests
import json
"""m
    TODO:
    implement init function that will authenticate user and get his app id
    implement Channel, Message, Guild classes and their _api (get, delete, create)
    implement WebSocket events like MESSAGE_CREATE, MESSAGE_DELETE, INTERACTION_CREATE
"""

class DiscordAPI:
    def __init__(self, token):
        self._token = token
        self.api = "https://discord.com/api/v9"
        self._headers = {
            "Authorization": f"Bot {self._token}"
        }
        response = requests.get(f"{self.api}/gateway/bot", headers=self._headers)
        self.dick_url = json.loads(response.text)
        print(f"url: {self.dick_url['url']}")
        self.app_id = self._getAppId()
    def _getAppId(self):
        response = requests.get(f"{self.api}/oauth2/applications/@me" , headers=self._headers)
        response.raise_for_status()
        app_data = json.loads(response.text)
        return f"App ID: {app_data['id']}"
        
   