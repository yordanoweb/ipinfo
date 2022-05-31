import re
import subprocess
import json

from functools import reduce
from pipe import pipe


"""
Ejecuta un comando contenido en el arreglo "cmd_info". El primer
indice del arreglo contiene el comando. A partir del segundo indice
estan los parametros requeridos por el comando.
"""
def exec_command_with_params(cmd_info):
    def get_info(some_data = None):
        # Lo primero en el arreglo es el comando a ejecutar
        cmd = cmd_info[0]
        # El resto del arreglo contiene los parametros que se pasan al comando
        params = cmd_info[1:]
        cmd_out = subprocess.Popen([cmd, *params], stdout=subprocess.PIPE)
        """
        El metodo "Popen" devuelve una tupla ('esto', 'esto otro', 'etc').
        En la posicion '0' de la tupla esta el resultado del comando ejecutado.
        Se le hace un "decode" a dicho resultado porque lo devuelto es un
        arreglo de bytes, no una cadena. El "decode" traduce los bytes a cadena.
        """
        return cmd_out.communicate()[0].decode()
    return get_info


"""
Toma una cadena que contiene informacion cruda separada por "c". Este
parametro "c" puede ser "\n", "\r", etc. Luego secciona la cadena "info_str"
entrante cortandola por cada aparicion de dicho separador, y devuelve
un arreglo de cadenas.
"""
def split_by(c):
    def split(info_str):
        return re.split(c, info_str)
    return split


"""
Limpia espacios innecesarios contenidos en cada elemento del
arreglo de cadena "info_array". Por ejemplo ":    " puede ser
convertido a ": ".
"""
def remove_spaces_after(c):
    def remove(info_array):
        """
        Reemplazar cualquier ocurrencia de el caracter del parametro "c",
        seguido de una cadena de N espacios en blanco. El reemplazo es el
        mismo caracter "c" seguido de un solo espacio.
        """
        return list(map(lambda s: re.sub(f"{c}\s+", f"{c} ", s), info_array))
    return remove


"""
Devuelve el indice del arreglo "info_array" que contiene la palabra
especificada en "s".
"""
def index_containing(s):
    """
    Reducir un arreglo de palabras, frases o sentencias (que es
    el parametro "info_array"), al indice que contiene la palabra
    suplida en el parametro "s".
    """
    def reducer(info_array):
        i = reduce(
            lambda a, info: a if str(info).__contains__(s) else a + 1,
            info_array,
            0
        )
        return i
    return reducer


"""
Elimina todos los elementos del arreglo "info_array" a partir de
aquel elemento de cadena que contenga la palabra que se suministre
en el parametro "s".
"""
def remove_from(s):
    i = 0
    def remove(info_array):
        get_from = index_containing(s)
        p = get_from(info_array)
        return info_array[:p - 1]
    return remove


"""
Reduce el arreglo "info_array" solo a aquellos elementos que contiene
las palabras contenidas en el arreglo suministrado en "words_array".
"""
def filter_containing_any_of(words_array):
    def filter_fn(info_array):
        """
        Dejar solo las lineas de informacion que contengan lo suministrado
        en el arreglo "words_array".
        """
        return list(
            filter(
                lambda info_line: reduce(
                    lambda a, word: True if str(info_line).__contains__(word) or \
                                            a == True else False,
                    words_array,
                    False
                ),
                info_array
            )
        )
    return filter_fn


"""
Embellece el JSON suministrado en "info_str" indentandolo por espacios
de acuerdo a la cantidad "indent".
"""
def beautify_json_output(indent):
    def dump(info_str):
        return json.dumps(info_str, indent=indent)
    return dump
