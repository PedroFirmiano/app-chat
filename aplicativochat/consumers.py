import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
           
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.user = self.scope["url_route"]["kwargs"]["user"]
        self.room_group_name = "chat_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
                self.room_group_name, self.channel_name
            )
        self.accept()
            

    def disconnect(self, close_code):
        pass


    def receive(self, text_data=None, type="receive", **kwargs):
        if isinstance(text_data, dict):
            text_data_json = text_data

            message = text_data_json["message"]
            body = text_data_json["body"]

        else:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]
            body = text_data_json["body"]

        self.send(text_data=json.dumps({"message": message, "body": body}))

    