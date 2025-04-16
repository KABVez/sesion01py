import time 


contador=10
print("Simularemos el despegue de un cohete: ")
while contador>=0:
    time.sleep(1)
    print(contador)
    contador-=1
print()
print("Despego el cohete")


#si quiero que se vea en vertical 
#  end"", flush=True
#

contador=10
print("Simularemos el despegue de un cohete: ")
while contador>=0:
    time.sleep(1)
    print(contador, "" , end="", flush=True)
    contador-=1
print()
print("Despego el cohete")