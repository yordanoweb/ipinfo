from funcs import *

from pipe import pipe


# Comando que devolvera la informacion de todas las interfaces de red
COMMAND_AND_PARAMS = ["nmcli", "device", "show"]


# Los campos que nos interesan de todo lo que devolver al comando
NETWORK_INFO_FIELDS = [
    'GENERAL.DEVICE',
    'GENERAL.TYPE',
    'GENERAL.HWADDR',
    'GENERAL.STATE',
    'GENERAL.CONNECTION',
    'GENERAL.CON-PATH',
    'IP4.ADDRESS[1]',
    'IP4.GATEWAY',
    'IP4.ROUTE[1]',
    'IP4.DNS[1]'
]


##################################################
# MAIN
##################################################

if __name__ == "__main__":

    doRequiredJob = pipe(
        exec_command_with_params(COMMAND_AND_PARAMS),
        split_by('\n'),
        remove_spaces_after(':'),
        filter_containing_any_of(NETWORK_INFO_FIELDS),
        remove_from("lo"),
        beautify_json_output(2)
    )

    result = doRequiredJob()
    print(result)
