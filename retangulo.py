

def area(a,l):
    return a*l

def perimetro(a,l):
    return 2*(a+l)

print('')
print('VAMOS CALCULAR A ÁREA E O PERIMETRO DE UM RETANGULO =)')
print('------------------------------------------------------')
base=float(input("Digite a base: "))
altura=float(input("Digite a altura: "))

if(base<=0 or altura<=0):
     print('')
     print('ESSE RETÂNGULO NÃO EXISTE')
     print(" ")
    
else:
    print("")
    print('Área:', area(altura,base))
    print('Perimetro:',perimetro(altura,base))
    print('')

