#python 3, from JMTT

import random
import json
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

msg_body = """"""

phone_list = [
    #!enter receiver phoneNumbers here
] 

quotes_file = json.load(open(r"C:\Users\userName\Documents\projects\py\qmessage\quotes.json"))
sent = []


def get_random_message(quotes, sent):
    random_set = random.choice(list(quotes))
    random_author = random_set['author']
    random_quote = random.choice(random_set['quote'])
    if random_quote not in sent:
        sent.append(random_quote)
        return random_author, random_quote
    else:
        get_random_message(quotes, sent)

#author, quote = get_random_message(quotes_file, sent)

def send_sms(quotes, phone_list):
    author, quote = get_random_message(quotes, sent)
    if len(quote)  > 5:
        for n in phone_list:
            message = client.messages.create(
                to=n,
                from_="+4400000000000", #!Replace with your phone number
                body="\n\n" + quote + "\n" + "\n Author: " + author +
                "\n\n From: A bad friend who happens to be good :D")




send_sms(quotes_file, phone_list)
#print(author, quote)

#from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "xxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
#auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#    to="+4475xxxxxxxxxx", 
#    from_="+441xxxxxxxx",
#    body="Hello from Python!")

#print(message.sid)
