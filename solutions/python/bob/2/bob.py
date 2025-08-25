RESPONSES = {
    'silence': 'Fine. Be that way!',
    'query': 'Sure.',
    'yelling': 'Whoa, chill out!',
    'yelledQuery': 'Calm down, I know what I\'m doing!',
    'default': 'Whatever.'
}

def is_silence(s): return s == ""
def is_yelling(s): return s.isupper()
def is_question(s): return s.endswith('?')
    

def response(msg):
    msg = msg.rstrip()

    if is_silence(msg):
        key = 'silence'
    elif is_yelling(msg):
        if is_question(msg):
            key = 'yelledQuery'
        else:
            key = 'yelling'
    elif is_question(msg):
        key = 'query'
    else:
        key = 'default'
        
    return RESPONSES[key]
