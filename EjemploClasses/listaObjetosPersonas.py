class Persona:

	def __init__(self,nombre,edad,altura,peso,resistencia):
		self.nombre 		= nombre
		self.edad   		= edad
		self.altura 		= altura
		self.peso   		= peso
		self.resistencia	= resistencia

personas = []

def imprimirListaValores(listaPersonas):
	for i in range(0,len(listaPersonas)):
		print "-"*80
		print personas[i].nombre
		print personas[i].edad
		print personas[i].altura
		print personas[i].peso
		print personas[i].resistencia

def recopilarInformacionLista(numeroUsuarios):
	for i in range(0,numeroUsuarios):
		nombre 		= raw_input("Introduce el NOMBRE: ")
		edad   		= raw_input("Introduce el EDAD: ")
		altura 		= raw_input("Introduce el ALTURA: ")
		peso   		= raw_input("Introduce el PESO: ")
		resistencia = raw_input("Introduce el RESISTENCIA: ")

		usuario = Persona(nombre,edad,altura,peso,resistencia)
		personas.append(usuario)



if __name__ == "__main__":
	numeroUsuarios = raw_input("Introduce el numero de usuarios que quieres registrar: ")
	if numeroUsuarios>0:
		recopilarInformacionLista(int(numeroUsuarios))
		imprimirListaValores(personas)
	else:
		print "Introduce un numero mayor que 0! "



