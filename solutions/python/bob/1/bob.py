responseFor = {
    'silence': 'Fine. Be that way!',
    'query': 'Sure.',
    'yelling': 'Whoa, chill out!',
    'yelledQuery': 'Calm down, I know what I\'m doing!',
    'default': 'Whatever.'
}

def response(m):
    m = m.rstrip()

    if m == '':
        key = 'silence'
    elif m.isupper():
        if m.endswith('?'):
            key = 'yelledQuery'
        else:
            key = 'yelling'
    elif m.endswith('?'):
        key = 'query'
    else:
        key = 'default'
        
    return responseFor[key]
