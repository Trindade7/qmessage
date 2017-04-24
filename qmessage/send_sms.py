#python 3, from JMTT

import random
import json
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC58092df82efed4fe15957341c677d76d"
# Your Auth Token from twilio.com/console
auth_token = "0dded774b6963e031df9c79f2d357019"

client = Client(account_sid, auth_token)

msg_body = """"""

phone_list = [
    "+447506921742", "+447490390963", "+447474937889"
]
#phone_list = {"1": "+447506921742", "2":"+447474937889", "3":"+447490389049", "4":"+447490390963"}

quotes_file = json.load(open(r"C:\Users\Trindade\Documents\projects\py\qmessage\quotes.json"))
sent = []
#sent = json.load(open(r"C:\Users\Trindade\Documents\projects\py\qmessage\quotes.json"))


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
                from_="+441667502053",
                body="\n\n" + quote + "\n" + "\n Author: " + author +
                "\n\n From: A bad friend who happens to be good :D")




send_sms(quotes_file, phone_list)
#print(author, quote)

#from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "AC58092df82efed4fe15957341c677d76d"
# Your Auth Token from twilio.com/console
#auth_token  = "0dded774b6963e031df9c79f2d357019"

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#    to="+447506921742", 
#    from_="+441667502053",
#    body="Hello from Python!")

#print(message.sid)
