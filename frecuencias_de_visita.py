from math import sqrt
from random import randint
from decimal import Decimal, getcontext
from time import*
from datetime import datetime
getcontext().prec = 1000
hora = datetime.now()
a = f"{hora.strftime('Datos_%A_%d-%m-%Y_%H:%M:%S-%p')}" 
b = time()
cantidad = 100
def mostrar_progreso(actual, total, ancho=50):
    porcentaje = actual / total
    barras_completas = int(ancho * porcentaje)
    barra = "." * barras_completas + " " * (ancho - barras_completas)
    print(f"\r[{barra}] {actual}/{total} ({porcentaje:.1%})", end="", flush=True)
with open(a + '.txt', 'w') as archivo:
    archivo.write("\nCaso ideal\n")
    archivo.write(f"{'='*10}\n")
    archivo.write("Proporciones de visita por clases\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0)="+ str(1 / 3)+"\n")
    archivo.write("   d(1)="+ str(1 / 6)+"\n")
    archivo.write("   d(2)="+ str(1 / 3)+"\n")
    archivo.write("   d(3)="+ str(1 / 6)+"\n")
    archivo.write("Límite de las secuencias\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + 2/3 + 1/6) - 3))+"\n")
    archivo.write("\n\nModelo Fibonacci\n")
    archivo.write(f"{'='*16}\n")
fibonacci = []
fibonacci.append(1)
fibonacci.append(1)
k = 0
while k < 100000:
    k += 1
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proporciones de visita por clases\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0) ="+ str(fibonacci[-2] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(1) ="+ str(fibonacci[-3] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(2) ="+ str(fibonacci[-2] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(3) ="+ str(fibonacci[-3] / (2*fibonacci[-1]))+"\n")
    archivo.write("Límite de las secuencias\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + (fibonacci[-2] / (fibonacci[-1])) + (fibonacci[-3] / (2*fibonacci[-1])))-3))+"\n")
    archivo.write("\n\nModelo Cuasi-Fibonacci\n")
    archivo.write(f"{'='*22}\n")
k = i = j = k = l = m = 0
x = 0
fibi = []
fibj = []
fibk = []
fibl = []
fibijkl = []
x = randint(0,3)
while m < 100000:
    m += 1
    if x == 0:                        
        i += 1
        k += 1
    elif x == 1:
        i += 1
    elif x == 2:
        j += 1
        l += 1
    elif x == 3:
        k += 1
    x = randint(0,3)
    fibi.append(i)
    fibj.append(j)
    fibk.append(k)
    fibl.append(l)
    fibijkl.append(i + j + k + l)
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proporciones de visita por clases\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0)="+ str(i / (i + j + k + l))+"\n")
    archivo.write("   d(1)="+ str(j / (i + j + k + l))+"\n")
    archivo.write("   d(2)="+ str(k / (i + j + k + l))+"\n")
    archivo.write("   d(3)="+ str(l / (i + j + k + l))+"\n")
    archivo.write("Límite de las secuencias\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l))) - 3))+"\n")
    archivo.write("\n\nExperimento real con un número\naleatorio en [2^60,10^4000]\n")
    archivo.write(f"{'='*30}\n")
k = i = j = k = l = m = 0
x = 1
fibi = []
fibj = []
fibk = []
fibl = []
fibijkl = []
x = randint(2**60,10**4000)
while m < 1:
    m += 1
    while x > 10**16:
        if x % 4 == 0:
            x = x // 2
            i += 1
        elif x % 4 == 1:
            x = 3 * x + 1
            j += 1
        elif x % 4 == 2:
            x = x // 2
            k += 1
        elif x % 4 == 3:
            x = 3 * x + 1
            l += 1
    x = randint(2**60,10**4000)
    """fibi.append(i)
    fibj.append(j)
    fibk.append(k)
    fibl.append(l)
    fibijkl.append(i + j + k + l)"""
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proporciones de visita por clases\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0)="+ str(i / (i + j + k + l))+"\n")
    archivo.write("   d(1)="+ str(j / (i + j + k + l))+"\n")
    archivo.write("   d(2)="+ str(k / (i + j + k + l))+"\n")
    archivo.write("   d(3)="+ str(l / (i + j + k + l))+"\n")
    archivo.write("Límite de las secuencias\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l))) - 3))+"\n")
    archivo.write("\n\nExperimento Real con "+str(cantidad)+" núme_\nros aleatorios en [2^60,10^4000]\n")
    archivo.write(f"{'='*32}\n")
k = i = j = k = l = m = 0
x = 1
fibi = []
fibj = []
fibk = []
fibl = []
x = randint(2**60,10**4000)
print("Procesando ",cantidad," números aleatorios en [2^60,10^4000]\n")
while m < cantidad:
    m += 1
    c = time()
    while x > 10**16:
        if x % 4 == 0:
            x = x // 2
            i += 1
        elif x % 4 == 1:
            x = 3 * x + 1
            j += 1
        elif x % 4 == 2:
            x = x // 2
            k += 1
        elif x % 4 == 3:
            x = 3 * x + 1
            l += 1
    x = randint(2**60,10**4000)
    fibi.append(i / (i + j + k + l))
    fibj.append(j / (i + j + k + l))
    fibk.append(k / (i + j + k + l))
    fibl.append(l / (i + j + k + l))
    mostrar_progreso(m, cantidad)
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proporciones de visita por clases\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0)="+ str(sum(fibi) / len(fibi))+"\n")
    archivo.write("   d(1)="+ str(sum(fibj) / len(fibj))+"\n")
    archivo.write("   d(2)="+ str(sum(fibk) / len(fibk))+"\n")
    archivo.write("   d(3)="+ str(sum(fibl) / len(fibl))+"\n")
    archivo.write("Límite de las secuencias\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l))) - 3))+"\n")
print('\nResultados guardados en ---'+ a + '.txt---', )
