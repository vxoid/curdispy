import requests
from consts import *

class Message:
    def __init__(self, token, content, channel_id, message_id, user_id):
        self.__token = token
        self.__content = content
        self.__channel_id = channel_id
        self.__message_id = message_id
        self.__user_id = user_id
        self.__gulid = "1086953817184141322"
        self.__headers = {
            "Authorization": f"Bot {self.__token}",
            "Content-Type": "application/json"
        }
    
    def delete(self):
        response = requests.delete(f"{API}/channels/{self.__channel_id}/messages/{self.__message_id}", headers=self.__headers)
        response.raise_for_status()

    def kick_member(self):
        payload = {
            'reason': 'violation'
        }
        response = requests.delete(f"{API}/guilds/{self.__gulid}/members/{self.__user_id}", headers=self.__headers, json=payload)
        response.raise_for_status()

    def send_message(self):
        headers = {
            "Authorization": f"Bot {self.__token}"
        }
        payload = {
            "content": "забанив лошка 😈"
        }
        with open("equipment/cum.mp4", "rb") as file:
            f = file.read()
        data = {
            "file": ("cum.mp4", f)
        }
        response = requests.post(f"{API}/channels/{self.__channel_id}/messages", json=payload, headers=headers)
        response = requests.post(f"{API}/channels/{self.__channel_id}/messages", json=payload, headers=headers, files=data)

        response.raise_for_status()

    def get_usr_id(self):
        return self.__user_id

    def get_content(self):
        return self.__content