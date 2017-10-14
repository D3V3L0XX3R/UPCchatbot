import time
import random
import datetime
import telepot
import os
import commands

def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    start='Hola /roll para numero aleatorio entre el 1 y el 6 y /time para dar la hora'
    name= msg['from']['first_name']
    h='Hola, '

    print name+': '+command
    if command == '/start':
        bot.sendMessage(chat_id, start)
    elif command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id,  str(datetime.datetime.now()))
    elif command=='/system' and name=='Oriol':
        os.system('clear')
        os.system('ifconfig')
        os.system('scrot /home/pi/Desktop/screen/screen.png')
        screenFile = open("/home/pi/Desktop/screen/screen.png")
        bot.sendPhoto(chat_id, screenFile )
        screenFile.close()
    elif command=='/screen' and name=='Oriol':
        os.system('scrot /home/pi/Desktop/screen/screen.png')
        screenFile = open("/home/pi/Desktop/screen/screen.png")
        bot.sendPhoto(chat_id, screenFile )
        screenFile.close()
    elif command=='/clear' and name=='Oriol':
        os.system('clear')
    elif command=='/rude':
        bot.sendMessage(chat_id, 'Una bala, un disparo...')
        time.sleep(5)
        bot.sendMessage(chat_id, 'Si haces las cuentas te sale!')
    elif command=='Hola bot' or command=='hola bot':	
	bot.sendMessage(chat_id, h+name)
    elif command=='/temp':
        temperatura= "Temperatura CPU: "+str(round(get_cpu_temp()))+' C'
        bot.sendMessage(chat_id, temperatura)
    elif command=='hijueputa' or command=='Hijueputa' :
        song= open("/home/pi/Desktop/screen/nar.mp3",'rb')
        print 'Uploading File'
        bot.sendAudio(chat_id, song)
        print 'File Sent'
        bot.sendMessage(chat_id, 'Hijueputa mal pario gonorrea!')
        song.close()
        
#if round(get_cpu_temp())>=56:
        #start fan
bot = telepot.Bot('TOKEN')
bot.message_loop(handle)
print 'I am listening niggi ...'

while 1:
    time.sleep(10)
