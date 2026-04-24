# ▪ Faça um programa que receba um número n
# ▪ Exiba a tabuada deste número do 0 ao 25.
# ▪ Utilize laços de repetição.

n = int(input("digite um número: "))

count = 0
while count <=25:
    print(n*count)
    count+=1
