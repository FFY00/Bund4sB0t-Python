#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Skype4Py
import re
import urllib2
from sys import exit

# Config
# Use /me <msg>
modo_me = True


class cores:
    ROXO = '\033[95m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AVISO = '\033[93m'
    BRANCO = '\033[0m'
    BOLD = '\033[1m'
    SUBLINHADO = '\033[4m'
    AZUL_CLARO = '\033[96m'
    VERMELHO = '\033[91m'
    LARANJA = '\033[33m'

prefixo = ""

if modo_me == True:
    prefixo = "/me "


print cores.VERDE, cores.BOLD, """
\n\n\n\n
Bund4sB0t - SkypeBot BR/PT :P
Made by FFY00
Versão 1.5
\n\n\n\
""" + cores.VERMELHO

cmd_ajuda = cores.AZUL_CLARO + cores.BOLD + """\n\n\n\tBund4sB0t Help\n\n
exit : exit Bund4sBot\n
\n\n""" + cores.BRANCO

ajuda = """Bund4sB0t Help

!alive : check if Bund4sB0t is active
!resolve [skype] : resolves a skype
!skypedb [skype] : search for skype resolves in the DB
!ip2skype [ip] : search for a skype using a IP
!email2skype [email] : search for a skype using a email
!geoip [ip] : geoip info of an IP"""

def comandos(mensagem, estado):
    if estado == 'SENT' or (estado == 'RECEIVED'):
        print mensagem.FromDisplayName + ":", mensagem.Body
        if mensagem.Body[:1] == "!":
           msg = re.sub("[^\w]", " ",  mensagem.Body).split()
           if msg[0] == "alive":
               vivo(mensagem, msg)

           elif msg[0] == "ajuda" or msg[0] == "help":
               mensagem.Chat.SendMessage(ajuda)

           elif msg[0] == "resolver" or msg[0] == "resolve":
               resolver(mensagem, msg)

           elif msg[0] == "geoip":
               geoip(mensagem, msg)

           elif msg[0] == "skypedb":
               skypedb(mensagem, msg)

           else:
               nao_cmd(mensagem, msg)

def nao_cmd(mensagem, msg):
    msg1 = prefixo + "Command not found! Use !help for a complete list of commands..."
    mensagem.Chat.SendMessage(msg1)
    print cores.ROXO + cores.BOLD + "Command not found (!" + msg[0] + ")..." + cores.BRANCO

def vivo(mensagem, msg):
    msg1 = prefixo + "Bund4sBot here! e_e :D"
    mensagem.Chat.SendMessage(msg1)
    print cores.ROXO + cores.BOLD + "Command !alive recived..." + cores.BRANCO

def resolver(mensagem, msg):
    print cores.ROXO + cores.BOLD + "Command !resolve recived..." + cores.BRANCO
    api = "http://api.predator.wtf/resolver/?arguments=" + msg[1]
    url = urllib2.urlopen(api)
    ip = url.read()
    msg1 = prefixo + "IP: " + ip
    mensagem.Chat.SendMessage(msg1)

def skypedb(mensagem, msg):
    print cores.ROXO + cores.BOLD + "Command !skypedb recived..." + cores.BRANCO
    api = "http://api.predator.wtf/lookup/?arguments=" + msg[1]
    url = urllib2.urlopen(api)
    ip = url.read()
    ip = ip.replace("Athena Found No Results!", "IP not found :(")
    msg1 = prefixo + "IP: " + ip
    mensagem.Chat.SendMessage(msg1)

def geoip(mensagem, msg):
    print cores.ROXO + cores.BOLD + "Command !skypedb receved..." + cores.BRANCO
    api = "http://api.predator.wtf/geoip/?arguments=" + msg[1]
    url = urllib2.urlopen(api)
    dados = url.read()
    dados = dados.replace("Athena Found No Results!", "Found no results :(")
    dados = dados.replace("<br> ", """
    """)
    msg1 = prefixo + dados
    mensagem.Chat.SendMessage(msg1)

skype = Skype4Py.Skype()
skype.OnMessageStatus = comandos

if skype.Client.IsRunning == False:
    skype.Client.Start()


skype.Attach()
print cores.AZUL + 'Bund4sB0t start in user:',skype.CurrentUserHandle + "\n\n\n" + cores.BRANCO

while True:
    comando = raw_input('')
    if comando == "sair" or comando == "exit":
        exit()
    if comando == "help":
        print cmd_ajuda
    else:
        print cores.VERMELHO + cores.BOLD + 'Command not found! Use "help"\n' + cores.BRANCO
