'''5) Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1.'''

num = int(input("Digite um número: "))
contador = 0



for i in range(1, num + 1):
    if num % i == 0:
        contador += 1



print("O número {} foi divisível {} vezes!".format(num, contador))



if contador == 2:

    print("O número é primo")

else:

    print("O número não é primo") 