"""
Define una tuberia que espera varias funciones como parametros. Cada una
de las funciones se recomienda que a su vez devuelvan otra funcion. Esta
tuberia devuelve tambien una funcion a la que opcionalmente se le pasa
algun dato (un numero, una cadena, un arreglo, objeto, etc.). Luego el
objeto pasado viajara a traves de cada funcion y sera retornado con la
modificacion que se le haga en cada una de dichas funciones.

Ejemplo:

# x = None para evitar que Python se queje porque falta algun parametro
def sum_one(x = None):
  return lambda n: n + 1

# x = None para evitar que Python se queje porque falta algun parametro
def mul_by_2(x = None):
  return lambda n: n * 2

some_fn = pipe(sum_one, mul_by_2)

# res va a ser igual a 6
res = some_fun(2)

"""
def pipe(*args):
    def fn(x = None):
        for f in args:
            x = f(x)
        return x
    return fn
