def addmultiplenumbers (numeros):  #esta funcion  suma
  resultado = 0 
  for numb in numeros:
    resultado = resultado + numb
  return resultado
  
def multiplymultiplenumbers(numeros): #esta funcion multiplica 
  resultado = 1
  for numb in numeros:
    resultado = resultado * numb
  return resultado

def isiteven(num):               # esta funcion detecta los pares e  impares 
     if isinstance(num, int):
       return num % 2 == 0
     return False
     
def isitaninteger(num):           # esta funcion  detecta los enteros
     return isinstance(num, int)
         

    
def main():
  numb1=[]
  while True:
   numb2=input("ingresa tu numero.por favor ingresa una palabra parar para detener la funcion")
   if numb2 == "parar":
     break
   numb1.append
   
 
   print("Hello learners!")
  
if __name__=="__main__":
  main() 