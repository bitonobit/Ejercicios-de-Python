# Ámbito de las variables
# Las variables que se crean fuera de una función son globales y no se ven en la función a menos que uses global
def saluda():
    global x  # Convierte a x en una variable global
    x = "hola que tal"


saluda()
print("Candy, " + x)

# Una variable creada en el cuerpo principal del código Python es una variable global y pertenece al ámbito global. Las variables globales están disponibles desde cualquier ámbito, global y local.
# Si opera con el mismo nombre de variable dentro y fuera de una función, Python las tratará como dos variables separadas, una disponible en el alcance global (fuera de la función) y otra disponible en el alcance local (dentro de la función):
x = 300
y = 100


def myfunc():
    global y
    x = 200
    print(x)  # Esta vale 200


myfunc()
print(x)  # Esta vale 300

# La nonlocalpalabra clave se utiliza para trabajar con variables dentro de funciones anidadas.
# La nonlocalpalabra clave hace que la variable pertenezca a la función externa.


def fun1():
    x = "Candy"

    def fun2():
        nonlocal x
        x = "Ana"

    fun2()
    return x


print(fun1())
