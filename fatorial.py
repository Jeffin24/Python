f=int(input("Digite o numéro que você quer o fatoria:"))
result=f
for valor in range(f-1,0,-1):
    result*=valor
   
   
print(f,"!","=",result)  
