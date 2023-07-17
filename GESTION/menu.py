import os
import citas

if (__name__=='__main__'):
    opcion = 0
    while True:
        os.system('clear')
        print('*'*35)
        print(' ------ GESTION DE CITAS ------- ')
        print('1. Agregar Cita ')
        print('2. Buscar Cita')
        print('3. Modificar Cita ')
        print('4. Cancelar Cita ')
        print('5. Salir.')
        
        opcion = input('Opcion deseada: ')
        
        if (opcion == "1"):
            citas.agregarCitas()
        elif (opcion == "2"):
            citas.buscarCita()
        elif (opcion == "3"):
            citas.modificarCita()
        elif (opcion == "4"):
            citas.cancelarCita()
        elif (opcion == "5"):
            input("Un gusto Ayudarte :)\n\tVuelva Pronto!")
            break
        else:
            print("Opcion no valida")