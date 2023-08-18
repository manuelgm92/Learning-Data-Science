import os, sys

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)  #subir dos niveles en carpetas, es decir sube hasta imp

print("Ruta:", ruta)
sys.path.append(ruta)


import b.y as y  #al importar primero que la función al haber una llamada de y1() lo ejecuta antes que la funcion
# se ejecuta todo el archivo para no mostrar:


def x1():
    print("x1")
    y.y1()

if __name__ == "__main__":
    import b.y as y
    x1()
