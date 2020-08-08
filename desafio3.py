#Realiza una función separar(lista), que tome una lista que tenga datos de cantidad de
#árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego,
#la función debe devolver dos listas ordenadas; la primera con las cantidades que
#superen los 100, y la segunda con el resto.
#¿Qué cantidad de ciudades han plantado más de 100 árboles en cuarentena?
Ciudad_arboles = [["Chaco",150],["Chubut",400],["Corrientes",150],["Formosa",12]]

def separar(lista):

	Más_100_árboles = []
	Menos_100_árboles = []

	for cantidad_o_número in lista:
		if cantidad_o_número[1] > 100:
			Más_100_árboles.append(cantidad_o_número)
	else:
		Menos_100_árboles.append(cantidad_o_número)

		separar(Más_100_árboles).sort()
		separar(Menos_100_árboles).sort()