import os 
import os.path
import json

citas = []
file_path = 'GESTION/data/citas.json'
    

def agregarCitas():
    os.system("clear")
    print('+'*35)
    print(' ------ AGREGAR CITAS ------- ')
    nombre = input("Nombre Completo del paciente: ")
    fecha = input("Fecha AAAA/MM/DD: ")
    hora = input("Hora HH:MM : ")
    motivo = input("Motivo de la consulta : ")
    cita={
        "Nombre": nombre,
        "Fecha": fecha,
        "Hora": hora,
        "Motivo": motivo
        }
    citas.append(cita)
    print(citas) 
    # si el archivo existe
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        
        existing_data.extend(citas)
    #   citas = existing_data
    
    with open(file_path, 'w') as f:
        json.dump(citas, f, indent=4)
    input("Presione 'Enter' para continuar.")
    
def buscarCita():
    os.system("clear")
    print('?'*35)
    print(' ------ BUSCAR CITAS ------- ')
    buscar = input("Buscar por paciente (P). Buscar por Fecha (F): ").upper()
    with open (file_path, 'r') as cita:
        citas = json.load(cita)
    if buscar == 'P':
        name = input("Nombre del Paciente: ")
        for cita in citas:
            if cita['nombre'] == name:
                print(cita)
        input("'Enter' para continuar...")
    elif buscar == 'F':
        fecha = input("Fecha AAAA/MM/DD: ")
        for cita in citas:
            if cita['fecha'] == fecha:
                print(cita)
        input("'Enter' para continuar...") 
    else:
        input("\n  Opcion no Valida \n\t'Enter' para continuar...")

def cancelarCita():
    os.system("clear")
    print('+'*35)
    print(' ------ CANCELAR CITAS ------- ')
    print
    with open(file_path, 'w') as f:
        

#2023/03/09
#13:09