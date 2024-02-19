import conexion as conn
from os import system
import time

db=conn.DB()  
def create():
    apellido=str(input("INGRESE SU APELLIDO:"))
    nombre=str(input("INGRESE NOMBRE: ")) 
    dni=str(input("INGRESE DNI: "))     
    if(len(apellido) > 0 and len(nombre)> 0 and len(dni)> 0 ):  
        sql="INSERT INTO sistema(apellido,nombre,dni)VALUES(?,?,?)"
        parametros=(apellido,nombre,dni)
        db.ejecutar_consulta(sql,parametros)
        print("Insertados...")

def read():
    result=db.ejecutar_consulta("SELECT * FROM sistema ")
    for data in result:
        print("""
        id : {}
        apellido : {}
        nombre : {}
        dni : {}""" .format(data[0],data[1],data[2],data[3]))

def  update():
     id=int(input("INGRESE ID: "))
     apellido=str(input("INGRESE SU APELLIDO:"))
     nombre=str(input("INGRESE NOMBRE: ")) 
     dni=str(input("INGRESE DNI: ")) 
     if(id!= 0) :
         sql="UPDATE sistema SET apellido=?,nombre=?,dni=? WHERE id=?"
         parametros=[apellido,nombre,dni,id]
         db.ejecutar_consulta(sql,parametros) 
         print("ACTUALIZADO...")

def delete():
    id=int(input("INGRESE ID: "))   
    if(id!= 0) :
        sql="DELETE FROM sistema WHERE id=?"
        parametros=(id,)
        db.ejecutar_consulta(sql,parametros)
        print("ELIMININADO...")

def search():
    apellido=str(input("INGRESE SU APELLIDO:"))  
    if(len(apellido) > 0 ) :
        sql="SELECT * FROM sistema WHERE apellido LIKE ?"
        parametros=("%{}%".format(apellido),)
        resul=db.ejecutar_consulta (sql,parametros)  
        for data in resul:
            print("""
            +id : {}
            +apellido : {}
            +nombre : {}
            +dni : {}""".format(data[0],data[1],data[2],data[3]))

while True:
    print("================")
    print("(\tREGISTRO DE PERSONAL")
    print("================")
    print("\t[1]-INGRESE REGISTRO ")
    print("\t[2]-LISTAR REGISTRO ")
    print("\t[3]-ACTUALIZAR REGISTRO ")
    print("\t[4]-ELIMINAR REGISTRO")
    print("\t[5]-BUSCAR REGISTRO")
    print("\t[6]-SALIR")
    print("================")

    try:
        opcion=int(input("SELECCION OPCION: "))  
        if(opcion==1):
            create()
            time.sleep(1)
            system("cls")

        elif(opcion==2):  
            read() 

        elif(opcion==3):  
            update()  
            time.sleep(1)
            system("cls")

        elif(opcion==4):
            delete()  
            time.sleep(1)
            system("cls")

        elif(opcion==5):
            search()    

        elif(opcion==6):
           print("UD SALIO,VUELVA A INGRESAR AL MENU SI NECESITA REALIZAR OTRO MOVIMIENTO")
           break  
        else:
            print("OPCION NO VALIDA") 
            time.sleep(1)
            system("cls")
    except :
         print("ERROR EN ELEGIR OPCIONES") 
         time.sleep(1)
         system("cls")   
