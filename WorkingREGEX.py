import re

cadena = 'Estoy trabajando con Python en domingo y Semana Santa'

busqueda = 'domingo'

if print(re.search(busqueda, cadena)) is not None:
    print(f'Se ha encontrado el termino {busqueda}')

else:
    print(f'No se ha encontrado el termino {busqueda}')
