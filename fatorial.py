f=int(input("Digite o numéro que você quer o fatoria:"))
result=1
print(f,"!"," = ",sep='', end='')
for valor in range(f,0,-1):
    print(valor,end=' ') 
    if valor !=1:
        print('x',end=' ')
    
    result*=valor
    
   

print(" =",result) 
