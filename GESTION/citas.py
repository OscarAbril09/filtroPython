import os 
import os.path
import json

citas = []
file_path = 'GESTION/data/citas.json'
    

def agregarCitas():
    os.system("clear")
    print('+'*37)
    print(' ---------- AGREGAR CITAS ---------- ')
    print('\n-Nueva Cita: ')
    nombre = input("\tPaciente: ")
    while True:
        fecha = ""
        año = input("\tAño AAAA: ")
        mes = input("\tMes MM: ")
        dia = input("\tDia DD: ")
        if (int(año) >= 2023 and int(mes) > 0 and int(mes) <= 12 and int(dia) > 0 and int(dia) <= 30):
            fecha = "{}/{}/{}".format(año, mes, dia)
            print(f"   {fecha}")
            break  
        else:
            print("Fecha no Valida")
    hora = input("\tHora HH:MM : ")
    motivo = input("\tMotivo de la consulta : ")
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
    print('?'*49)
    print(' ---------------- BUSCAR CITAS ---------------- ')
    buscar = input("\nBuscar por paciente (P). Buscar por Fecha (F): ").upper()
    with open (file_path, 'r') as cita:
        citas = json.load(cita)
    if buscar == 'P':
        name = input("\tPaciente: ")
        for i, cita in enumerate(citas):
            if cita['nombre'] == name:
                print(f"\n{i+1}. CITA: ")
                print(F"\t-Nombre: {cita['nombre']}")
                print(F"\t-Fecha: {cita['fecha']}")
                print(F"\t-Hora: {cita['hora']}")
                print(F"\t-Motivo: {cita['motivo']}")
                print("")
        input("'Enter' para continuar...")
    elif buscar == 'F':
        fecha = input("Fecha AAAA/MM/DD: ")
        for i, cita in enumerate(citas):
            if cita['fecha'] == fecha:
                print(f"\n{i+1}. CITA: ")
                print(F"\t-Nombre: {cita['nombre']}")
                print(F"\t-Fecha: {cita['fecha']}")
                print(F"\t-Hora: {cita['hora']}")
                print(F"\t-Motivo: {cita['motivo']}")
                print("")
        input("'Enter' para continuar...") 
    else:
        input("\n  Opcion no Valida \n\t'Enter' para continuar...")

def modificarCita():
    os.system("clear")
    print('+'*45)
    print(' ------------- MODIFICAR CITAS ------------- ')
    print('+'*45)
    with open (file_path, 'r') as f:
        citas = json.load(f)
        for i, cita in enumerate(citas):
            print(f"\n{i+1}. CITA: ")
            print(F"\t-Nombre: {cita['nombre']}")
            print(F"\t-Fecha: {cita['fecha']}")
            print(F"\t-Hora: {cita['hora']}")
            print(F"\t-Motivo: {cita['motivo']}")
            print("-"*45)
        while True:
            id = int(input("Cita a Modificar: "))
            if (id > 0 and id-1 <= len(citas)):            
                citas[id-1]["nombre"] = input("\n Nombre: ")
                fecha = ""
                while True:
                    año = input("\t Año AAAA: ")
                    mes = input("\t Mes MM: ")
                    dia = input("\t Dia DD: ")
                    if (int(año) >= 2023 and int(mes) > 0 and int(mes) <= 12 and int(dia) > 0 and int(dia) <= 30):
                        fecha = "{}/{}/{}".format(año, mes, dia)
                        print(f"   {fecha}")
                        break  
                    else:
                        print("Fecha no Valida")
                citas[id-1]["fecha"] = fecha
                citas[id-1]["hora"] = input(" Hora: ")
                citas[id-1]["motivo"] = input(" Motivo: ")
                print(citas)
                input("continue.")
                with open(file_path, 'w') as f:
                    json.dump(citas, f, indent=4)
                break
            else:
                input("Opcion no Valida")

def cancelarCita():
    os.system("clear")
    print('+'*45)
    print(' ------------- CANCELAR CITAS ------------- ')
    print('+'*45)
    with open (file_path, 'r') as f:
        citas = json.load(f)
        for i, cita in enumerate(citas):
            print(f"\n{i+1}. CITA: ")
            print(F"\t-Nombre: {cita['nombre']}")
            print(F"\t-Fecha: {cita['fecha']}")
            print(F"\t-Hora: {cita['hora']}")
            print(F"\t-Motivo: {cita['motivo']}")
            print("*"*45)
        cancelar = int(input("Cita a Cancelar: "))
        citas.pop(cancelar-1)
    with open(file_path, 'w') as f:
        json.dump(citas, f, indent=4)
    input("continuar?")
    
        

#2023/03/09
#13:09