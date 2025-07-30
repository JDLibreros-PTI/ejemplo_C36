archivo = open("test_file.txt", "r+")

contenido = archivo.read()  

saludo = "Hola Alumnos de Parquesoft\n"  

archivo.seek(0)   
print(archivo.tell())

archivo.write(saludo+contenido)  
print(archivo.tell())

archivo.close()

