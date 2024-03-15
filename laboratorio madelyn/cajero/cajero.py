saldo = 1000

for intentos in range(3):
    codigo = input("Ingrese su usuario: ")
    if codigo == "Madelyn":
        pin = input("Ingrese su PIN: ")
    if pin == "1234":
        opcion = int(input("Seleccione una opción:\n1. Ver saldo\n2. Retirar dinero\nOpción: "))
        if opcion == 1:
            print("Su saldo actual es:", saldo)
        elif opcion == 2:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print("Retiro exitoso. Su saldo actual es:", saldo)
        else:
            print("Opción no válida.")
        break
    else:
        print("PIN incorrecto. Intento", intentos + 1, "de 3.")

if intentos == 2:
    print("Ha excedido el número máximo de intentos. Su tarjeta ha sido bloqueada.")