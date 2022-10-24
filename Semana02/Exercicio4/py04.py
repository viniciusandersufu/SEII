## Criando listas

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses) #printa a lista completa

print(len(courses)) #printa o comprimento da lista

print(courses[0]) #printa o conteúdo do índice 0 "History"

print(courses[-1]) #printa o último elemento da lista

print(courses[0:2]) #printa os índices entre 0 e 2, incluindo o primeiro, mas não o segundo

print(courses[2:]) #printa os índices do primeiro até o último índice

## Para adicionar um índice à liste:

courses.append('Nome') #adiciona ao fim da lista

courses.insert(0, 'Art') #adiciona ao índice indicado

#------------------------------------------------------

courses_2 = ['Chemistry', 'Education']
courses.insert(0, courses_2) #adiciona a lista courses_2 em courses como uma sublista (com os colchetes
print(courses[0]) #mostra que o índice zero da lista courses é ['Chemistry', 'Education']

#-------------------------------------------------------
courses.extend(courses_2) #os índices de courses_2 são adicionados individualmente em courses

## Remover itens
courses.remove('Math') #remove o indice que contém 'Math'

courses.pop() #remove o último valor da lista

popped = courses.pop() #a variável popped recebe o item excluído da lista

## Ordenando listas

nums = [1, 5, 2, 4, 3]

courses.reverse() #inverte a lista, coloca-a de trás para frente
courses.sort() #coloca a lista em ordem alfabética

courses.sort(reverse=True) #coloca a lista em ordem alfabética invertida
nums.sort(reverse=True) #printa os índices em ordem decrescente

lista_ordenada = sorted(courses) #ordena a lista em ordem alfabética

## Mínimo, máximo valor das listas

print(min(nums)) #mostra o mínimo valor de nums
print(sum(nums)) #mostra a soma dos valores da lista nums

## Encontrar o índice de um valor da lista

print(courses.index('CompSci')) #retorna o valor do índice do item

## Para verificar se um valor está contino na lista

print('Math' in courses) #se 'Math' estiver na lista, o programa nos retornará 'True', senão, 'False'

## Obter os valores de uma lista com o 'for'

for item in courses:
    print(item)

## Obter os índices e os valores de uma lista usando 'for'

for index,course in enumerate(courses):
    print(index, course)
# retorna todos os índices e valores da lista com os índices começando do zero

for index,course in enumerate(courses, start=1):
    print(index, course)
# retorna todos os índices e valores da lista com os índices começando de 1, ou seja, o índice zero é mostrado como 1, o índice 2 é mostrado como 3 e assim por diante

## Colocar os valores da lista 'courses' na string 'course_str' separados por vírgula

course_str = ','.join(courses)

## Criar uma lista a partir de uma string, passando o elemento utilizado para separar os elementos das string: espaço, vírgula, traço. No nosso caso, vírgula  

nova_lista = course_str.split(',')

## Tuplas não são mutáveis como as listas

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

#se nós tentarmos modificar um valor da tupla_1, como se segue:
tuple_1[0] = 'Art'
#o programa mostrará um erro dizendo que tuplas não podem ser modificadas

## Sets tem valores desordenados e não repetidos

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

#se nós adicionarmos um valor repetido a um 'Set', o ele não será adicionado ao 'Set'

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
#Resultado:
{'History', 'Math', 'Physics', 'CompSci', 'Math'}

print('Math' in cs_course) #mostra se um valor está presente no 'Set'

#--------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

#Verificar os valores em comum dos 'Sets'
print(cs_courses.intersection(art_courses))

#Verificar os valores diferentes
print(cs_courses.difference(art_courses))

#Fazer a união dos 'Sets'
print(cs_courses.union(art_courses))

## Criando listas vazias

empty_list = []
empty_list = list()

## Criando tuplas vazias
empty_tuple = ()
empty_tuple = tuple()

## Criando sets vazios

empty_set = {} #não é correto, esse comando criaria um dicionário vazio
empty_set = set()


