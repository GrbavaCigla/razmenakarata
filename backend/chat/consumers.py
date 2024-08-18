import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.exceptions import ValidationError

from .serializers import MessageSerializer
from .models import Chat

# TODO: Optimize this
# TODO: Recheck security, I think everything is fine, but it doesn't hurt to recheck
class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def verify_connection(self):
        assert hasattr(self, "chat_id")

        chat_row = Chat.objects.filter(pk=self.chat_id).first()
        if not chat_row:
            return False

        self.allowed_users = [chat_row.owner.pk, chat_row.ticket.owner.pk]

        if not self.scope["user"].pk in self.allowed_users:
            return False

        return True

    @database_sync_to_async
    def save_message(self, serializer):
        assert hasattr(self, "chat_id")

        data = serializer.validated_data
        chat_row = Chat.objects.filter(pk=self.chat_id).first()

        chat_row.messages.append({"owner": data["owner"].pk, "text": data["text"]})

        chat_row.save()
    
    @database_sync_to_async
    def get_messages(self):
        assert hasattr(self, "chat_id")

        chat_row = Chat.objects.filter(pk=self.chat_id).first()
        return chat_row.messages


    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.group_name = f"chat_{self.chat_id}"

        if not await self.verify_connection():
            await self.close()
            return

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

        for message in await self.get_messages():
            await self.send(text_data=json.dumps({
                "message": message["text"],
                "user_id": message["owner"]
            }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        message = json.loads(text_data)["message"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": message,
                "user_id": self.scope["user"].pk,
            },
        )

    async def chat_message(self, event):
        serializer = MessageSerializer(
            data={"text": event["message"], "owner": event["user_id"]}
        )
        try:
            await database_sync_to_async(
                lambda: serializer.is_valid(raise_exception=True)
            )()
        except ValidationError as e:
            print(e)
            # TODO: Add error handling to chat
            return

        await self.save_message(serializer)

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
