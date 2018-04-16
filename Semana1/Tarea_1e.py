# The frequency of each letter in the Gettysburg Address is already stored as address_count. Use this dictionary to find the most common letter in the Gettysburg address.
# Store this letter as most_frequent_letter, and print your answer.

  initial_count = 0

  # For que recorre el diccionario y extrae la llave y el valor.
  for letter,count in address_count.items():
    if count > initial_count: # Si el valor es mayor a 0.
      initial_count = count   # Le asigna el valor de la llave a la variable "initial_count"
      most_frequent_letter = letter # Le asigna la llave a la variable "most_frequent_letter"
      
  # Imprime la llave con más frecuencias.
  print(most_frequent_letter)
