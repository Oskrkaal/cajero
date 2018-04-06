import os

def Login():
	titulo = "bienvenido al sistema"
	print titulo.upper()
	print "***** 1. REGISTRAR CUENTA *****"
	print "***** 2. ENTRAR AL SISTEMA *****"
	
	
	while True:
		opcion = input ("Elija una opcion: ")
		if opcion == 1 :
			os.system('clear')
			Registro()
		elif opcion == 2:
			os.system('clear')
			Entrar()
		else:
			print "debe elegir una opcion: "
		
		
		
		

def Regresar():
	while True:
		si = str(raw_input("IR AL MENU PRINCIPAL SI/NO: \n"))
		if si == (1):
			os.system('clear')
			Login()
		elif si == (2):
			os.system('clear')
			Registro()
		else:
			print "elija una opcion"

def Registro():
	print "Usted eligio la opcion de registrar cuenta"
	nombre = raw_input ("Por favor Ingrese su nombre: ")
	apellido = raw_input ("Por favor Ingrese su apellido: ")
	no_de_cuenta = input ("Ingrese su numero de cuenta: ")
	usuarios = [nombre, apellido, no_de_cuenta]
	for i in range(len(usuarios)):
		print "se registro exitosamente "+str(usuarios[i])+ " a nuestra base de datos"
		
	Regresar()
		
		
		



def Sistema():
	titulo = "bienvenido al sistema"
	print titulo.upper()
	print "***** 1. DEPOSITO *****"
	print "***** 2. RETIRO *****"
	print "***** 3. CONSULTAR SALDO *****"
	print "***** 4. CAMBIAR CUENTA *****"
	

Login()
	
	




Registro()
