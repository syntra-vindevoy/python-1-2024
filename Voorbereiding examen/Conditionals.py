language = 'python'

if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
else:
    print('language is not python or java')

user ='admin'
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')

if not logged_in:
    print('please log in')
else:
    print('welcome')
