# app-chat
aplicativo de chat com django e web socket

front-end se encontra no repositorio: https://github.com/hugoiandev/chat-web

# Para rodar o app

- Instale [python](https://www.python.org/downloads/)


# Inicialização

1 - iniciando um ambiente virtual (venv)

Navegue até a pasta que deseja clonar o repositorio e inicie um ambiente virtual

Para o Windows:

py -m venv venv


Para Linux e Mac:

python3 -m venv ./venv



2 - na mesma pasta clone o repositorio do git e ative a venv
- git clone  https://github.com/PedroFirmiano/app-chat.git


Para o Windows:
venv/Scripts/activate


Para Linux e Mac:
source venv/bin/activate

3 - entre na pasta meu-chat e installe os requirements:

cd .\meu-chat\
pip install --upgrade pip
pip install -r requirements.txt

4 - Faça as migrações:
python manage.py migrate

5 - rode o servidor
python manage.py runserver



