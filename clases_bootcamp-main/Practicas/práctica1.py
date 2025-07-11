# -*- coding: utf-8 -*-
"""Práctica1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LkSs2Wv9VW9PQAuZNLxJgZNVNjoG87Rb

#Conceptos Básicos de Python

1. Sintaxis: Python se destaca por su sintaxis clara y legible. Se usa la identación en lugar de llaves o palabras para dilimitar bloques de código.

2. Variables: Se definen de forma dinámica, lo que significa que no es necesario declarar el tipo de varibla antes de usarla.

3. Tipos de datos: Python tiene varios tipos de datos integrados, como números, cadena de texto, listas, tuplas y diccionarios.

#3.1. Números.
Pythn soporta enteros, flotantes y complejos
"""

entero = 10 # a la variable entero se le asigna el número 10
print(entero)
type(entero)

flotante = 3.14
print(flotante)
type(flotante)

complejo = 2 + 3j
print(complejo)
type(complejo)

"""# Cadena de Caracteres
Permite almacenar teto, que puede ser una sola letra, una palabra o una frase completa. El texto que se desea almacenar o mostrar debe ponerse entre comillas simples ('') o dobles (""). Por ejemplo:
"""

cadena = "¡Hola, mundo!"
print(cadena) # muestra el texto almacenado en a varibale cadena

cadena = "Otra cosa"
print(cadena)

"""#Listas

"""

lista = [1,2,3,"CUATRO", 5.0]
print(lista)
type(lista)

listaFrutas = ["chontaduro", "banano", "fresa"]
print(listaFrutas)

"""**Modificar un elemento de la lista**"""

lista[0]= 10 # La posición cero, es la primara posición de la lista de izquierda a derecha
print(lista)

listaFrutas[1]= "Manzana"
print(listaFrutas)

"""**Agregar un elemento al final de la lista**"""

lista.append(4)
print(lista)

listaFrutas.append("pera")
print(listaFrutas)

"""**Insertar un elemento en una posición especifica de la lista**"""

lista.insert(3,"perro")
print(lista)