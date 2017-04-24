msg_body = "sd"

author = ""
source = "A good friend."
start_sentence = msg_body.find("&ld")
end_sentence = msg_body.find("rd")
control = ""

def add_data(author, message, quotes):
    if author in quotes:
        if message not in quotes[author]:
            quotes[author].append(message)
    else:
        quotes[author] = [message]


def get_messages(msg_body):
    quotes = {}
    author = ""
    message = ""

    while True:
        #finds the quote
        if msg_body.find("&ldquo;") != -1:
            start_sentence = msg_body.find("&ldquo;") + 7
        else:
            return quotes
        end_sentence = msg_body.find("&rdquo;")
        message = msg_body[start_sentence:end_sentence]

        #finds th author
        msg_body = msg_body[end_sentence:]
        msg_body = msg_body[msg_body.find('<a class="authorOrTitle"') + 1:]
        start_sentence = msg_body.find(">") + 1
        end_sentence = msg_body.find("<")
        author = msg_body[start_sentence:end_sentence]

        add_data(author, message, quotes)
        msg_body = msg_body[end_sentence + 1:]