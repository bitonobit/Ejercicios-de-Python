# *******************************************************************************
#                          Condicionales
# *******************************************************************************
a = 10
b = 20
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

if a==0: print("a es igual a 0")    #Si corto
print(a) if a>b else print(b)       #Si sino corto
print("a es mayor") if a > b else print("iguales") if a == b else print("b es mayor") #si con 3 condiciones