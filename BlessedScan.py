import socket
from colorama import init
from termcolor import cprint
import whois


init()


cprint("""
██████╗ ██╗     ███████╗███████╗███████╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║     ██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║     █████╗  ███████╗███████╗█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██║     ██╔══╝  ╚════██║╚════██║██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝███████╗███████╗███████║███████║███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    
Version 1.0
Developed by Team Blessed
""", "red")

def scan_ports(target_ip, port_range=100):
    open_ports = []
    for port in range(1, port_range + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def option_one():
    print("You have selected option 1.")
    domain = input("Please enter the domain URL: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip}")
    except socket.error as err:
        print(f"Error resolving domain: {err}")

def option_two():
    print("You have selected option 2.")
    target_ip = input("Please enter the IP address to scan: ")
    open_ports = scan_ports(target_ip, port_range=100)
    if open_ports:
        print(f"Open ports on {target_ip}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"No open ports found on {target_ip}")

def option_three():
    print("You have selected option 3.")
    target_ip = input("Please enter the IP address to scan: ")
    open_ports = scan_ports(target_ip, port_range=1000)
    if open_ports:
        print(f"Open ports on {target_ip}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"No open ports found on {target_ip}")

def option_four():
    print("You have selected option 4.")
    while True:
        domain = input("Enter Domain (or press Enter to go back): ")
        if not domain:
            break
        try:
            w = whois.whois(domain)
            for k, v in w.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"Error: {e}")

def main_menu():
    while True:
        print("\nPlease choose one of the following options:")
        print("1. Convert URL to IP")
        print("2. Fast Scan")
        print("3. Deep Scan")
        print("4. Whois Lookup")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            option_one()
        elif choice == '2':
            option_two()
        elif choice == '3':
            option_three()
        elif choice == '4':
            option_four()
        elif choice == '0':
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
