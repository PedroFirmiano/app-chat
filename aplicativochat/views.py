
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .defSocket import messagem_socket
from .models import Message, Group
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated

class Sessao(APIView): 
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):


        groupId = self.kwargs["pk"]

        data = self.request.data
        username = request.user.username
        print(groupId)
        groupId = Group.objects.get(groupId=groupId)
        print(groupId)
        user = User.objects.get(username=username)

        message = data["mensagem"]
        mensagem = Message(userSend = user, message= message, date = datetime.now(), groupId=groupId)
        mensagem.save()

        # body = {'usuario':user, 'mensagem':mensagem}
        # messagem_socket('NOVA_MENSAGEM', groupId, body)


        return Response({'success':'mensagem enviada'}, status = 200)


class NewGroup(APIView):

    permission_classes = (IsAuthenticated,)
    def post(self, request):
        
        group = Group(lastModificated= datetime.now())
        group.save()

        return Response({'group':group.groupId}, status = 201)

