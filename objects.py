#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        # Setto il nome del file
        if not isinstance(name,str):
            raise Exception ("Nome file non stringa")
        self.name = name     
    
    #funzione che legge i valori numerici dal file
    def get_data(self, start=None, end=None):

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')
    
        except Exception as e:  
            # Stampo l'errore
            print("except variable:", e)
            raise Exception('Ops,File inesistente')

        if not isinstance(start,int) and not isinstance(end,int):
                raise Exception("Mi devi dare due numeri per stampare l'intervallo,altrimenti come posso fa????")
        if not start<end:
            raise Exception("Mi devi dare start<end")
         
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('ops,errore nella conversione a float(mi toccherà saltare questo valore): "{}"'.format(e))
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                #aggiungo alla lista dei valori questo valore
                values.append(value)
        my_file.close()

        if start<0 or end>len(values):
            raise Exception("Stai attento...ricontrolla gli estremi dell'intervallo")
        
        return values[start:end+1]
    
#======================
# Corpo del programma
#======================

mio_file = CSVFile("shampoo_sales.csv")
print(mio_file.get_data(1,10))