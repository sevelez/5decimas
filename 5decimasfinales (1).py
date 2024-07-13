# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WPhOjM740Tf9yJCcveLTSJlZ62ttvAch
"""
import csv
from os import system
def obtener_facturacion():
    lista=[]
    with open("datos.csv","r",newline="") as archivo:
      lector_csv=csv.reader(archivo,delimiter=";")
      pos=0
      for linea in lector_csv:
          if pos!=0:
              año=int(linea[0])
              trimestre1=float(linea[1])
              trimestre2=float(linea[2])
              trimestre3=float(linea[3])
              trimestre4=float(linea[4])
              lista.append({
                  "año":año,
                  "trimestre1":trimestre1,
                  "trimestre2":trimestre2,
                  "trimestre3":trimestre3,
                  "trimestre4":trimestre4,
              })
          else:
            pos=1
    return lista

lista=obtener_facturacion()
print(lista)

def imprimir_media():
    lista=obtener_facturacion()
    for elemento in lista:
        año=elemento["año"]
        media=(elemento["trimestre1"]+elemento["trimestre2"]+elemento["trimestre3"]+elemento["trimestre4"]/4)
        print(f"año {año} facturacion media de {media} euros")

def burbuja(arreglo):
  longitud=len(arreglo)
  for i in range(longitud):
      for indice_actual in range(longitud - 1):
        indice_siguiente_elemento=indice_actual+1
        if arreglo[indice_actual]["año"]>arreglo[indice_siguiente_elemento]["año"]:
            arreglo[indice_siguiente_elemento],arreglo[indice_actual]=arreglo[indice_actual],arreglo[indice_siguiente_elemento]
def annos_cronologicamente():
    lista=obtener_facturacion()
    burbuja(lista)
    with open(r"C:\Users\cetecom\Documents\salida.csv","w", newline="") as archivo:
        escritor_csv=csv.writer(archivo, delimiter=";")
        escritor_csv.writerow(["anno","promedio"])
        for elemento in lista:
            año=elemento["año"]
            total=(elemento["trimestre1"]+elemento["trimestre2"]+elemento["trimestre3"]+elemento["trimestre4"]/4)
            salida=[]
            salida.append(año)
            salida.append(total)
            escritor_csv.writerow(salida)

system("cls")
opciones="1.Imprimir años con media \n 2.guardar años cronologicamente \n 3.salir\n elige\n"
eleccion=""
while eleccion!="3":
  eleccion=input(opciones)
  system("cls")
  if eleccion=="1":
      imprimir_media()
  elif eleccion=="2":
      annos_cronologicamente()
  elif eleccion=="3":
      print("Se ha salido")
  else:
      print("Opcion invalida")