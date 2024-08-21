print("Vamos ver a potencia de um numero? Digite a base e o expoente")
num=int(input("Base: "))
exp=int(input("Expoente: "))
result=1
for valor in range(1,exp+1,1):
    result*=num
    
    
    
print("O resultado dessa potência é:",result)