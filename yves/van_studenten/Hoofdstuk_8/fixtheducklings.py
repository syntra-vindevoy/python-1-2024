prefixes = 'JKLMNOPQ'
suffix = 'ack'

for l in prefixes:
    if l == 'O' or l == 'Q':
        print(l + 'u' + suffix)
    else:
        print(l +  suffix)