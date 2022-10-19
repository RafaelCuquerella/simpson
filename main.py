from wsgiref import headers
import requests
import time
import pandas as pd


Lisa='Lisa Simpson'
Homer='Homer Simpson'




resp = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
 
resp.json()
  
    

frase=resp.json()[0]['quote']
personaje=resp.json()[0]['character']

#print(frase)

#print (personaje)


#def csv(frase,personaje): 

my_dict = {"frase": frase ,"personaje": personaje}
output = pd.DataFrame()



if personaje==Lisa:
        output = pd.DataFrame()
        output = output.append(my_dict, ignore_index=True)
        print(output.head())
        output.to_csv('Lisa/Lisa.csv',mode='a', header=False)
elif personaje == Homer:
        output = pd.DataFrame()
        output = output.append(my_dict, ignore_index=True)
        print(output.head())
        output.to_csv('Homer/Homer.csv',mode='a', header=False)
else:
        output = pd.DataFrame()
        output = output.append(my_dict, ignore_index=True)
        print(output.head())
        output.to_csv('General/general.csv',mode='a', header=False)
        print('Hola resto')

#csv()



#pd.read_csv('ejemplo.csv') 