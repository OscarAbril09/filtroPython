import os
import citas

if (__name__=='__main__'):
    flag = True
    opcion = 0
    
    while flag:
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
            Print("Un gusto Ayudarte :)")
            flag = False