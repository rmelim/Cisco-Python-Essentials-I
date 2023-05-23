'''
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad 
de combustible consumido por cada 100 kilómetros. En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón 
de combustible.

Escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

Las funciones:

1.- se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
2.- toman un argumento (el valor correspondiente a sus nombres)

Aquí hay información para ayudarte:

1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.
'''

milla = 1.609344        # Equivalencia de una milla en kilómetros
galon = 3.785411784     # Equivalencia de un galón en litros

def liters_100km_to_miles_gallon(liters):       # El parámetro "liters" contiene la cantidad de litrso consumidos cada 100 Km.
    return ((100 / milla) / (liters / galon))   # Llevar el equiv. en millas de 100 Km. y el equiv. en galones de los liros consumidos.

def miles_gallon_to_liters_100km(miles):        # El parámetro "miles" contiene la cantidad de millas recorridas con sólo un galón de combustible.
    return (galon / ((miles * milla) / 100))    # Llevar el equiv. de millas a 100 km y calcular el rendimiento en galones por milla


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

