
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .defSocket import messagem_socket


class Sessao(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, pk):
        sala = self.kwargs["pk"]
        
        data = self.request.data

        usuario = data['usuario']
        mensagem = data["mensagem"]
        
        # mensagem = Mensagem(enviadoPor = 'Pedro', mensagem = "Acorda pedrinho", sala = "minha_e_do_pedro")
        # mensagem.save()
        body = {'usuario':usuario, 'mensagem':mensagem}

        messagem_socket('NOVA_MENSAGEM', sala, body)


        return Response({'success':'mensagem enviada'}, status = 200)


