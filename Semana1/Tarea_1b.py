# Crear una variable con el siguiente texto "Jim quickly realized that the beautiful gowns are expensive"
# Crear un diccionario con el nombre "count_letters", el cual contenga cada letra y las veces que se ha repetido en la oración. Cuente minúsculas y mayúsculas separadamente.

	import string

	sentence = 'Jim quickly realized that the beautiful gowns are expensive'
	alphabet = string.ascii_letters
	count_letters = {}
  
	# For que recorre la oración.
	for i in sentence:
	    # Revisa si la letra a evaluar corresponde al alfabeto. 
	    if i in alphabet:
	        # Ve si la llave del diccionario existe.
	        if count_letters.get(i):
	            #print("Evaluando" +" "+i) # Para debugging.
	            # Si existe le suma 1.
	            count_letters[i] += 1
	        else:
	            # Si no existe, la crea con el valor 1.
	            #print("Creando " + i) # Para debugging.
	            count_letters[i] = 1
  
  # Imprime el diccionario
	count_letters
