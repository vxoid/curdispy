import op, json, requests, websockets, asyncio
from consts import *

class WSBot:
    def __init__(self, token):
        self.__interval = None
        self.__sequence = None

        self.__auth = {
            "token": token,
            "properties": {
                "os": "linux",
                "browser": "curdis",
                "device": "curdis"
            },
            "presence": {
                "status": "online",
                "afk": False
            }
        }
    
    async def run(self, message_handler):
        async with websockets.connect(WS_API) as ws:                
            await self.__hello(ws)
            if self.__interval is None:
                raise RuntimeError("discord hello ws failded")

            await asyncio.gather(self.__read_message(ws, message_handler), self.__heartbeat(ws))

    def __opcode(self, opcode, payload):
        return {
            "op": opcode,
            "d": payload
        }

    async def __hello(self, ws):
        await ws.send(json.dumps(self.__opcode(op.IDENTIFY, self.__auth)))
        hb = await ws.recv()

        data = json.loads(hb)
        if data["op"] != 10:
            return
        
        self.__interval = data["d"]["heartbeat_interval"]/1000

    async def __heartbeat(self, ws):
        while self.__interval is not None:
            await ws.send(json.dumps(self.__opcode(op.HEARTBEAT, self.__sequence)))
            await asyncio.sleep(self.__interval)
    
    async def __read_message(self, ws, message_handler, handler_by_command):
        async for data in ws:
            data = json.loads(data)
            if data["op"] != op.DISPATCH:
                continue

            self.__sequence = int(data["s"])
            event_type = data["t"]
            if event_type == "MESSAGE_CREATE":
                id = data["d"]["id"]
                content = data["d"]["content"]
                channel_id = data["d"]["channel_id"]
                username = data["d"]["author"]["username"]
                author_id = data["d"]["author"]["id"]
            elif event_type == "INTERACTION_CREATE":
                interaction_id = data["d"]["id"]
                interaction_token = data["d"]["token"]
                
                response = ""
                payload = { "type": 4, "data": { "content": response } }
                headers = {
                    "Content-Type": "application/json"
                }

                response = requests.post(f"{API}/interactions/{interaction_id}/{interaction_token}/callback", data=payload, headers=headers)

    # def set_message_handler(self, handler):
    #     self.__message_handler = handler
    
    # def add_handler(self, key: str, handler):
    #     self.__handlers[key] = handler

    # def command(self, key: str):
    #     def wrapper(func: Callable):
    #         self.add_handler(key, func)
    #     return wrapper
    
    # def message_handler(self):
    #     def wrapper(func):
    #         self.set_message_handler(func)
    #     return wrapper