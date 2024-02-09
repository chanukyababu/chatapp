"""import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.roomGroupName = "group_chat_gfg"
		await self.channel_layer.group_add(
			self.roomGroupName ,
			self.channel_name
		)
		await self.accept()
	async def disconnect(self , close_code):
		await self.channel_layer.group_discard(
			self.roomGroupName , 
			self.channel_layer 
		)
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]
		username = text_data_json["username"]
		await self.channel_layer.group_send(
			self.roomGroupName,{
				"type" : "sendMessage" ,
				"message" : message , 
				"username" : username ,
			})
	async def sendMessage(self , event) : 
		message = event["message"]
		username = event["username"]
		await self.send(text_data = json.dumps({"message":message ,"username":username}))"""


"""import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name  # Corrected argument
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })

    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))
        

        
"""
"""import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chatapp.models import Message  # Import your Message model
from django.contrib.auth.models import User  # Import the User model if not already imported
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        username = text_data_json["username"]
        
        # Get the user object based on the username (assuming username is unique)
        #user = User.objects.get(username=username)
        user = await sync_to_async(User.objects.get)(username=username)
        
        # Save message to the database along with the user
        #Message.objects.create(user=user, content=message_content)
        await sync_to_async(Message.objects.create)(username=username, content=message_content)


        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                "type": "sendMessage",
                "message": message_content,
                "username": username,
            }
        )

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))

"""
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chatapp.models import Message  # Import your Message model
from django.contrib.auth.models import User  # Import the User model if not already imported
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

        # Retrieve existing messages from the database asynchronously
        messages = await sync_to_async(list)(Message.objects.all())

        # Send existing messages to the newly connected user
        for message in messages:
            await self.send(text_data=json.dumps({
                "message": message.content,
                "username": message.username,
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        username = text_data_json["username"]
        
        # Get the user object based on the username (assuming username is unique)
        user = await sync_to_async(User.objects.get)(username=username)
        
        # Save message to the database along with the user
        await sync_to_async(Message.objects.create)(username=username, content=message_content)

        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                "type": "sendMessage",
                "message": message_content,
                "username": username,
            }
        )

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))
