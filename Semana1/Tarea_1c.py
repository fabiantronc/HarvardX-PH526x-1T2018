# Re escribe el codigo de 1b para crear una funcion "counter" que tome una cadena "input_string" y devuelva un diccionario de letras contadas "count_letter".
# Usa tu función para llamar counter(sentence)

	import string

	def counter(input_string): # Crea la función.
		alphabet = string.ascii_letters
		count_letters = {} # Crea un diccionario vacio.
		for i in input_string: # Lee palabra por palabra.
			if i in alphabet: # Evalua la palabra para ver si se encuentra en el alfabeto.
				if count_letters.get(i): # Revisa si la palabra esta creada en el diccionario.
					count_letters[i] += 1 # Le suma 1 al valor de la llave.
				else: # Si no, crea la llave.
					count_letters[i] = 1  # Le asigna 1 al valor de la llave.
		return count_letters  # Devuelve el valor de la función, en este caso, un diccionario.
  
  # Imprime el diccionario
	counter("Tres erres")
