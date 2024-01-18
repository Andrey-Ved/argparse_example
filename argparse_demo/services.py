import psutil
import socket


def ip_addresses():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)

    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))

    return address_info


def cpu_load():
    return psutil.cpu_percent(interval=0.1)


def ram_available():
    return psutil.virtual_memory().available
