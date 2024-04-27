import subprocess
import random

def generate_random_mac():
    # Générer une adresse MAC aléatoire avec un format valide
    mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def change_hostname(new_hostname):
    try:
        # Utiliser la commande hostnamectl pour changer l'hostname
        subprocess.run(["hostnamectl", "set-hostname", new_hostname], check=True)
        print("Hostname changé avec succès en", new_hostname)
    except subprocess.CalledProcessError as e:
        print("Erreur lors du changement de l'hostname:", e)

def change_mac_address(interface):
    try:
        # Générer une adresse MAC aléatoire
        new_mac = generate_random_mac()

        # Désactiver l'interface
        subprocess.run(["ifconfig", interface, "down"], check=True)
        # Changer l'adresse MAC
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
        # Réactiver l'interface
        subprocess.run(["ifconfig", interface, "up"], check=True)
        print("Adresse MAC de", interface, "changée avec succès en", new_mac)
    except subprocess.CalledProcessError as e:
        print("Erreur lors du changement de l'adresse MAC:", e)

if __name__ == "__main__":
    new_hostname = input("Entrez le nouveau hostname: ")
    interface = input("Entrez l'interface réseau à modifier (ex: eth0): ")

    change_hostname(new_hostname)
    change_mac_address(interface)

