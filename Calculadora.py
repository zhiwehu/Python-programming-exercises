
print("Calculadora")
op=input("Elige la operación:+,-,/,* ")
numero1=float(input("Ingresa el primer digito:"))
numero2=float(input("Ingresa el segundo digito:"))


if op == '+':
   print("Resultado:",numero1+numero2)
elif op == '-':
   print("Resultado:",numero1-numero2)
elif op == '*':
   print("Resultado:",numero1*numero2)
elif op == '/':
   print("Resultado:",numero1/numero2)
   if numero2 !=0 :
       print("Resultado",numero1/numero2)
   else: ("Error: división por cero.")

else:
    print("Operación no válida.")




