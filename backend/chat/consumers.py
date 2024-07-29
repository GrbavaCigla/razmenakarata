import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.group_name = f"chat_{self.chat_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        message = json.loads(text_data)["message"]
        user = self.scope["user"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": message,
                "user_id": user.id,
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "user_id": event["user_id"],
                }
            )
        )


# from channels.generic.websocket import AsyncJsonWebsocketConsumer


# class ChatConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
#         self.group_name = f"chat_{self.chat_id}"

#         await self.channel_layer.group_add(self.group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)

#     async def receive(self, json_data):
#         message = json_data["message"]
#         print(f"RECEIVE {message}")

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 "type": "chat_message",
#                 "message": message,
#             },
#         )

#     async def chat_message(self, event):
#         message = event["message"]
#         await self.send(json_data={"message": message})
