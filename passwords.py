import random

def generate_weak_password():
    words = ["password", "123456", "qwerty", "admin", "abc123"]
    return random.choice(words)

def generate_medium_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "".join(random.sample(characters, 8))

def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=<>?"
    return "".join(random.sample(characters, 12))

def print_banner():
    banner = """
     _   _           _     _             
    | | | |         | |   (_)            
    | |_| |_   _ ___| |__  _ _ __   __ _ 
    |  _  | | | / __| '_ \| | '_ \ / _` |
    | | | | |_| \__ \ | | | | | | | (_| |
    \_| |_/\__,_|___/_| |_|_|_| |_|\__, |
                                   __/ |
                                  |___/ 
    """
    print(banner)

def main():
    print_banner()
    print("Generador de contraseñas")
    print("------------------------")
    print("1. Generar contraseña débil")
    print("2. Generar contraseña mediana")
    print("3. Generar contraseña fuerte")
    print("------------------------")
    choice = input("Seleccione el nivel de contraseña que desea generar (1-3): ")

    if choice == "1":
        password = generate_weak_password()
    elif choice == "2":
        password = generate_medium_password()
    elif choice == "3":
        password = generate_strong_password()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        return

    print("Contraseña generada: " + password)

if __name__ == "__main__":
    main()
