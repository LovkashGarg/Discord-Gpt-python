from dotenv import load_dotenv,dotenv_values
import os
import requests
import time


    # response.raise_for_status()
    


load_dotenv(); # loads dotenv values to this file 
MY_SECRET_KEY=os.getenv('token')


# import openai 
# openai.api_key=os.getenv('OPEN_AI_KEY')

# file = input("Enter 1, 2, or 3 for loading the chat:\n ")
file = "1"
match(file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3": 
    file = "chat3.txt"
  case _:
    print("Invalid choice.")
    exit()
    
with open(file, "r") as f:
  chat = f.read() 
# client = openai()

import discord
chat=""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
      time.sleep(3) 
      global chat
      # chat +=f"{message.author} :{message.content}"
      print(f"message from author {message.author} :{message.content}")
        # print(message.mentions)
        # means do not reply if author that is gpt is the user 
      try:
      
        if self.user != message.author:
            if self.user in message.mentions:
              try:
                cleaned_message = message.content.replace(f"<@{self.user.id}>", "").strip()
                chat+=cleaned_message
                url = "https://discord-bot-gpt.onrender.com/api/generate"
                payload = { 'question': chat}
                headers = {
                    'Content-Type': 'application/json'
                }


                response = requests.post(url, json=payload, headers=headers)
                # print(response.json())
              except requests.exceptions.RequestException as error:
                print("Error:", error)
              # print(chat)
            #   response = openai.ChatCompletion.create(
            #    model="gpt-3.5-turbo-0613",
            #    messages=[{"role": "user", "content": f"{chat}\n LovkashGpt : "}]
            #   )
              channel=message.channel
            #   print(response.choices[0])
            #   response.choices[0]['message']['content']
              # messageTosend=message.content
              await channel.send(response.json())

      except Exception as e:
        print(e)
        chat = ""
        # # don't respond to ourselves
        # if message.author == self.user:
        #     return

        # if message.content == 'ping':
        #     await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(MY_SECRET_KEY)