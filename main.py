#Se hacen todos los imports necesarios
from platform import python_branch
from wsgiref import headers
import requests
import time
import pandas as pd
from tkinter import W
import string
import os
import shutil
import urllib.request


#Se agregan las variables al principio
Lisa='Lisa Simpson'
Homer='Homer Simpson'
URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
contador = {}
w = 0

#Se genera la función para solicitar personaje, frase y los diferencia para guardar en Homer, Lisas o General
while True: 
 time.sleep(5)#Se agrega para que haga el get a la api cada 30 segundos
 resp = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes") #función para get a la api 
 resp.json()
 frase=resp.json()[0]['quote'] #Solicita solo la frase 
 personaje=resp.json()[0]['character'] #Solicita solo el personaje

#obtiene la imagen de la api, la descarga en png y la guarda en la carpeta de fotos
 descarga_imagen=resp.json()[0]['image'] 
 imagen=requests.get(descarga_imagen).content
 imagen_visual = f"Fotos/{personaje}.png"
 file= (f"Este es {personaje}.png")
 quitar = ",;:.\n!"
 
 for caracter in quitar:
        frase = frase.replace(caracter,"")
    
 frase2=frase.split()
 frase=frase2

#si  detecta que no existe el personaje, crea una carpeta nueva con su nombre    
 if not (os.path.exists(personaje)):
        r=urllib.request.urlopen(descarga_imagen)
        f=open(file,'wb')
        f.write(r.read())
        f.close()
        os.mkdir(personaje)
        time.sleep(0.5)
        shutil.move(file,personaje)
        time.sleep(0.5)

#Realiza un contador de palabras y las guarda en contador.txt
 for cambiante in frase:
        if cambiante in contador:
            contador[cambiante]=w
        else:
            contador[cambiante]=w
        w+=1
 print (contador)
 with open ('contador.txt', 'w') as cuentapalabras:

      for clave, valor in contador.items():
        cuentapalabras.write(f"\n{clave}: {valor}")

 #Distingue de si es Lisa, Homer o General
 my_dict = {"frase": frase ,"personaje": personaje}
 output = pd.DataFrame()
 if personaje==Lisa:
          output = pd.DataFrame()
          output = output.append(my_dict, ignore_index=True)
          print(output.head())
          output.to_csv('Personajes/Lisa/Lisa.csv',mode='a', header=False)
 elif personaje == Homer:
          output = pd.DataFrame()
          output = output.append(my_dict, ignore_index=True)
          print(output.head())
          output.to_csv('Personajes/Homer/Homer.csv',mode='a', header=False)
 else:
          output = pd.DataFrame()
          output = output.append(my_dict, ignore_index=True)
          print(output.head())
          output.to_csv('Personajes/General/general.csv',mode='a', header=False)

 






