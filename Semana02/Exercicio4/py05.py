## Dicionários

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name']) #o resultado seria o valor 'John'

print(student['idade']) #se nós usarmos esse método para acessar uma chave que não existe, o programa no retornará um erro

#Para que o programa retorne um valor padrão ou 'none' para chaves inexistentes, basta usar 'get'
print(student.get('name')) #retorna 'John'

print(student.get('idade')) #retorna 'none'

## Adicionar uma nova chave para o dicionário

student['phone'] = '5555-5555'

## Atualizar o valor de uma chave existente
student['name'] = 'Jane'

student.update({'name': 'Jane', 'age': 26, 'phone': '6666-6666'})

## Deletar uma chave do dicionário
del student['age']

age = student.pop('age') #exclui a chave do dicionário e passa o valor da chave para a variável

## Descobrir quantas chaves há no dicionário

print(len(student))

## Descobrir as chaves do dicionário

print(student.keys())

## Descobrir os valores das chaves

print(student.values())

## Descobrir os pares chave-valor

print(student.items())

#---------------------------------------------
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
    
