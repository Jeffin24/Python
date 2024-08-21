print('MULTIPLOS')
print('----------')
multi=int(input("Numero: "))
q=int(input("Quantos: "))
result=0
print("Os multiplos de",multi,"são:",end=" ")
for valor in range(1,q+1,1):
    result+=multi
    print(result,end=" ")
    