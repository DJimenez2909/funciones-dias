#ejemplo para colcular el area del triangulo

#variables de entrada
base = int(input("ingrese la base: "))
altura = int(input("ingrese la altura: "))


#proceso
def calcularAreaTriangulo(b,a):
    Area =(b*a)/2
    return Area
#invocamos la funcion
resultado = calcularAreaTriangulo(base,altura)

#salida de la funcion
print(f"el area del triangulo cuya base es {base} y altura es {altura} es de: ",resultado)



def my_function(country = "colombia"):
    print("i am from "+country)
my_function()
my_function("swende")
my_function("india")
my_function("")
my_function("brazil")

def mostrarEstudiantes(*args):
    print("el estudiante es: "+args[2])
mostrarEstudiantes("Emil", "tobias", "linus")



def mostrarcarros(carro1,carro2,carro3):
    print("el carro es: "+carro2)

mostrarcarros(carro1="BmW", carro3="ferrari", carro2="ford")

def mostrarClientes(**kwargs):
    print("su apellido es: "+ kwargs["apellido"])

mostrarClientes(nombre= "tobias", apellido = "Jimenez")


def mifuncion():
    pass