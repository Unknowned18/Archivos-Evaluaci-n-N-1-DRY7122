print("Evaluación N°1 Programación y Redes Virtualizadas")
print("Matías Alarcón y Gustavo Ramírez")
print("Grupo 3")
Espacio=(" ")
Nombre=input("Ingresar nombre: ")
Apellido=input("Ingresar apellido: ")
CodigoSeccion=input("Codigo sección: ")
Sede=input("Ingrese su sede: ")
print(Nombre+Espacio+Apellido+Espacio+CodigoSeccion+Espacio+Sede)
print("Ahora se validará que tipo de acl hay segun la ip de mi equipo")
ACL=int(input("Cual es el numero de acl ipv4??: "))
if ACL >= 1 and ACL <= 99:
    print("Ésta es una acl ipv4 Standard")
elif ACL >=100 and ACL <= 199:
    print("Ésta es una acl ipv4 Extendida")
else:
    print("Ésta no es nungun tipo de acl")

    