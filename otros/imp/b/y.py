import os, sys

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)  #subir dos niveles en carpetas, es decir sube hasta imp

print("Ruta:", ruta)
sys.path.append(ruta)

#import a.x as x



def y1():
    print("y1")
    
def y2():
    print("y2")
    x.x1()

if __name__ == "__main__":  #con esta condición no se importa lo que esté debajo de if __name__
    import a.x as x
    print("este print no se ejecuta")
    y2()