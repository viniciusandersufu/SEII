language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

#------------------------------------------

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

#----------------------------------------

a = [1,2,3]
b = [1,2,3]

print(a == b) #retorna 'True'

print(a is b) #retorna 'False'

#print(a is b) verifica se as variáveis têm o mesmo endereço de memória

#-----------------------------------------
a = [1,2,3]
b = a

print(id(a)) #retorna o id de a
print(id(b)) #retorna o id de b
print(id(a) == id(b)) #retorna 'True', porque a e b são a mesma variável

#-----------------------------------------

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#retorna 'Evaluated to False'

condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#retorna 'Evaluated to False'

condition = '' # ou (), [], {}, None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#retorna 'Evaluated to False'

