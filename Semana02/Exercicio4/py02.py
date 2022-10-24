message = 'Hello World'
print(message)

#----------------------

message = "Hello World"
print(message)

#----------------------

message = 'She\'s beautiful'
print(message)

#----------------------

message = """I'm Vinicius and I am 24 years old
I can write multiple line messages with 3 quotes at the begin 
and at the end."""
print(message) 

#----------------------

# Como saber quantos caracteres tem a string

message = "Hello World"
print(len(message))

#Como recuperar um ou mais caracteres da string

message = "Hello World"
print(message[0])

print(message[0:5]
#resultado: Hello
print(message[:5]
#resultado: Hello
print(message[6:]
#resultado: World

#---------------------

#Transforma uma string em outra com  letras minúsculas ou maiúsculas

message = "Hello World"
print(message.lower())
print(message.upper())

#--------------------

message = "Hello World"
print(message.count('l'))
print(message.count('Hello'))

#--------------------

#Substitui palavras da string

message = "Hello World"
new_message = message.replace('World', 'Universe')
print(new_message)

#--------------------

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)

#--------------------

greeting = 'Hello'
name = 'Michael'

message = '{}, {}. Welcome!'.format(greeting, name)

#-------------------

greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name.upper()}. Welcome!'

#-------------------

#Help de funções

print(help(str))

print(help(str.lower))

#------------------- 

num - 3

print(type(num))

#resultado: '<class 'int'>

