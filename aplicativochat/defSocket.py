
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



def messagem_socket(message, room_name, body):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"chat_{room_name}", {"type": "receive", "message": message, "body": body}
    )

