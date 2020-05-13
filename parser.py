def parse(message):
    (command, ys) = message.content[1:].split(' ')
    if command == 'q' or 'quote':
        return "Joe quote"
    else:
        return False

def isCommand(message):
    return message.content[0] == '!'
