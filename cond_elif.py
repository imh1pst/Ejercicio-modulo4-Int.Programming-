#--Operador == y !=

#Condicional elif
edad=int(input("cual es tu edad?.. "))

if edad <= 0:
    print("nadie puede tener esa edad.")

elif edad >= 1 and edad <=17:
    print("Eres menor de edad, nino/a o adolescente. ")

elif edad <= 100:
    print("Eres mayor de edad y/o58 de la tercera edad.")

else:
    print("Edad no validad.")
