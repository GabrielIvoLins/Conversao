class ConversorDeMoedas:
    def __init__(self,real,dolar):
        self.real = real
        self.dolar = dolar       

    def dolar(self,dolar,real):#De dolar para real 
        return dolar * real

    def real(self,real,dolar):#De real para dolar
        return dolar / real  


money = ConversorDeMoedas()

v = float(input("Digite o valor do dolar U$: "))
m = float(input("Digite o valor a ser convertido: "))


print("De dolar para real é",money.dolar(v,m))
print("De real para dolar é",money.real(v,m))

