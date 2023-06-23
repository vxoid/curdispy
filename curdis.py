import requests, json

api = "https://discord.com/api/v9"
class DiscordAPI:
    def __init__(self, token):
        self.__token = token
        self.__headers = {
            "Authorization": f"Bot {self.__token}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{api}/gateway/bot", headers=self.__headers)
        response.raise_for_status()
        self.api_url = json.loads(response.text)
        self.app_id = self._getAppId()

    def _getAppId(self):
        response = requests.get(f"{api}/oauth2/applications/@me" , headers=self.__headers)
        response.raise_for_status()
        app_data = json.loads(response.text)
        return app_data["id"]
    
    def get_all_messages(self, channel_id):
        responce = requests.get(f"{api}/channels/{channel_id}/messages", headers=self.__headers)
        responce.raise_for_status
        messages = json.loads(responce.text)
        all_messages = []
        for message in messages:
            content = message["content"]
            id = message["id"]
            channel_id = message["channel_id"]
            author = message["author"]
            user_id = author["id"]
            all_messages.append(Message(self.__token, content, channel_id, id, user_id))
        return all_messages

    def send_message(self, message=None, channel_id=None, files=None):
        headers = {
            "Authorization": f"Bot {self.__token}"
        }
        payload = {
            "content": message
        }
        data = {
            "file": ("cum.mp4", files)
        }
        response = requests.post(f"{api}/channels/{channel_id}/messages", headers=headers, json=payload,)
        response.raise_for_status()



    def register_commands(self):
        command_data = {
         "name": "spam",
         "description": "spartaaaa"
        }
        response = requests.post(f"{api}/applications/{self.app_id}/commands", headers=self.__headers, data=json.dumps(command_data))
        response.raise_for_status()
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
        response = requests.delete(f"{api}/channels/{self.__channel_id}/messages/{self.__message_id}", headers=self.__headers)
        response.raise_for_status()

    def kick_member(self):
        payload = {
            'reason': 'violation'
        }
        response = requests.delete(f"{api}/guilds/{self.__gulid}/members/{self.__user_id}", headers=self.__headers, json=payload)
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
        response = requests.post(f"{api}/channels/{self.__channel_id}/messages", json=payload, headers=headers)
        response = requests.post(f"{api}/channels/{self.__channel_id}/messages", json=payload, headers=headers, files=data)

        response.raise_for_status()

    def get_usr_id(self):
        return self.__user_id

    def get_content(self):
        return self.__content
    


