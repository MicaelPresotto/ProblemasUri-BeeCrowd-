'''4) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números impares'''
par = 0
impar = 0
for x in range(10):
    y = int(input('Digite um numero: '))
    if y % 2 == 0:
        par += 1
    else:
        impar +=1
        
print('Pares: ',par)
print('Impares: ', impar)