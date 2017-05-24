#print('----------conversão-de-moedas-------------')

c=float(input("Digite o valor de U$1,00 em R$: "))
while True:
    v=float(input("Escolha uma opção:\n1. Converter Real para Dólar\n2. Converter Dólar para Real\n3. Encerrar o programa:\n"))
    if v==1:
        valor=float(input("Digite o valor ser convertido:"))
        print("O valor de R$ %.2f em Dólar é U$ %.2f" % (valor,valor/c))
    elif v==2:
        valor=float(input("Digite o valor ser convertido:"))
        print("O valor de U$ %.2f em Reais é R$ %.2f" % (valor,c*valor))
    elif v==3:break
    else:
        print("Opção inválida.")
print("Fim-Do-Programa")
