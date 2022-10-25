nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break #sai do loop
    print(num)
#Resultado: 1
#           2
#           Found

for num in nums:
    if num == 3:
        print('Found')
       continue #vai para a próxima iteração do laço sem executar as instruções seguintes
    print(num)
#Resultado: 1
#           2
#           Found
#           4
#           5

#--------------------------------------------

x = 0 

while x < 10:
    print(x)
    x += 1

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
# Ctrl + C para parar um laço infinito


