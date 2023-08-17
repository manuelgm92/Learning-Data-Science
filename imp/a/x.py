import os, sys

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)  #subir dos niveles en carpetas, es decir sube hasta imp

print("Ruta:", ruta)
sys.path.append(ruta)


import b.y as y


def x1():
    print("x1")
    y.y1()
    
x1()
