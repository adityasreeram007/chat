from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('bot')
bot.set_trainer(ListTrainer)
for files in os.listdir("C:/Users/adity/Desktop/chatterbot-corpus/chatterbot_corpus/data/english/"):
	data=open("C:/Users/adity/Desktop/chatterbot-corpus/chatterbot_corpus/data/english/"+files,'r').readlines()
	bot.train(data) 
while True:
	message=input('You:')
	if(message.strip()=='Bye' or message.strip()=='bye'):
		print("chatBot: BYe!")
		break
	else:
		reply=bot.get_response(message)
		print('chatBot:',reply)
	