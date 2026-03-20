# ex. 1 - calcule a área de um círculo com raio 5. Use a fórmula: área = π * raio^2. (Dica: você pode usar 3.14159
# como valor aproximado de π).
raio =5
pi = 3.14159
area = pi * (raio^2)
print(area)

# ex.2 - converta uma temperatura de Fahrenheit para Celsius. A fórmula de conversão é: Celsius = (Fahrenheit
# - 32) * 5/9.
fahrenheit = 45
celsius = (fahrenheit-32) * 5/9
print(celsius)

# ex.3 - você comprou 3 livros por R$ 25 cada e 2 canetas por R$ 5 cada. Calcule o total gasto.
livro = 25
caneta = 5
print(f'Total gasto foi de R${(25*3) + (2*5)}')

# ex. 4 - Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro
# levou para percorrer essa distância?
d = 150
vm = 60
print(f'O carro levou {d/vm}h')

# ex.5 - Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
# aritmética do aluno.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'A média foi de {(nota1+nota2)/2}')


# ex.6 - Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
# ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'A média foi de {((nota1*4)+(nota2*6))/10}')

#ex. 7 - neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
# o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
# unitário de cada peça2. Após, calcule e mostre o valor a ser pago
nome_peca1 = input('Nomeie a primeira peça: ')
qtd_peca1 = int(input(f'Quantidade de {nome_peca1} desejada: '))
vlr_peca1 = float(input(f'Valor unitário de {nome_peca1}: '))

nome_peca2 = input('Nomeie a primeira peça: ')
qtd_peca2 = int(input(f'Quantidade de {nome_peca2} desejada: '))
vlr_peca2 = float(input(f'Valor unitário de {nome_peca2}: '))

print(f'O valor gasto total é de {(qtd_peca1*vlr_peca1) + (qtd_peca2*vlr_peca2)}')

# ex.8 - Crie um programa que receba o valor do produto e valor pago.
#  Calcule o troco a ser pago.
#  O valor do troco deve ser exibido no termina

v_produto = float('Digite o valor do produto: R$')
v_pago = float('Digite o valor pago: R$')

print(f'O troco foi de R${v_pago - v_produto}')




