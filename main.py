'''
    Author: Yaneth Mejía
    Verssion: 1.0
    Language: Python
'''
def say_hi():
    print('Hello world')
#Llamamos la función para que se ejecute
#say_hi()

def input_data_user():
    user_name = input('Ingresa tu nombre: ')
    #Se debe de validar que el valor ingresado sea un nro
    while True:
        try:
            age = int(input('Edad:'))
            break
        except:
            print('Error, no es un valor numérico')
    print(f'{user_name}, tiene {age} años.')
#Llamamos la función para que se ejecute
input_data_user()

def input_frameworks_data():
    while True:
        try:
            languages_count = int(input('Cuántos fm conoces?'))
            counter = 1
            while counter <= languages_count:
                framework_name = input('        Framework: ')
                counter += 1
            break
        except:
            print('Error, no es un valor numérico')
#Llamamos la función para que se ejecute
#input_frameworks_data()


def input_language_information():
    #Declaración de una lista vacía
    language_list = []
    while True:
        try:
            language_count = int(input('Cuantos lenguajes de prog conoces?'))
            for item_language in range(language_count):
                language_name = input(f'         {item_language}: ')
                #append() añade el lenguaje al final de la lista
                language_list.append(language_name)
            break
        except:
            print('Error, se esperaba un número')

#Llamamos la función para que se ejecute
#input_language_information()

def insert_info_student():
    #Solicitar nombre y documento del estudiante
    print('Ingresa la siguiente información')
    students_list = []
    while True:
        try:
            student_counter = int(input('Cuantos estudiantes ingresaras?'))
            for item_student in range(1, student_counter+1):
                student_name = input('      Nombre: ')
                document = input('      Documento: ')
                # Lista a la cual se le agrega una tupla list(tupla())
                # La sgte tupla tiene 3 posiciones (item_student, student_name, document)
                students_list.append((item_student, student_name, document))
            print(f'Los estudiantes que ingresaste, son:\n      {students_list}')
            break
        except:
            print('Se esperaba un dato numérico')
#insert_info_student()

def countries_information():
    countries_list = []
    while True:
        try:
            country_counter = int(input('Cuántos paises conoces?'))
            for item_country in range(1, country_counter+1):
                country_name = input('          País:')
                while True:
                    try:
                        population = int(input('          Población:'))
                        break
                    except:
                        print('Se esperaba un dato numérico')
                countries_list.append((item_country, country_name, population))
            print(f'      Información paises\n      {countries_list}')
            break
        except:
            print('Se esperaba un dato numérico')
#Devolver el país con mayor número de población y el de menor 
countries_information()
    
