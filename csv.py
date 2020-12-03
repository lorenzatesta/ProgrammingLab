# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")   
for line in my_file:
	# Faccio lo split di ogni riga sulla virgola
	elements = line.split(',')
	# Se NON sto processando l’intestazione...
	if elements[0] != 'Date':
        # Setto la data e il valore
		date = elements[0] 
		value = elements[1]
        # Aggiungo alla lista dei valori questo valore
		values.append(float(value))