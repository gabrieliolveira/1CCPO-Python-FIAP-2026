#algoritmo que recebe um número inteiro positivo n e imprime na tela todos os número de 1 a n
# 100


def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("a nota tem q estar entre 0 e 10")
        nota = float(input("digite a nota novamente: "))
    return nota


nota1 = float(input("digite a primeira nota: "))
nota1 = verificar_nota(nota1)

nota2 = float(input("digite a segunda nota: "))
nota2 = verificar_nota(nota2)

media = (nota1+nota2)/2
print(f"a média é {media}")