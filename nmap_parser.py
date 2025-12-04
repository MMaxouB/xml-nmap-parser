import os
import xml.etree.ElementTree as ET

def load_xml(path_file):
    tree = ET.parse(path_file)  # parse le fichier XML en arbre
    root = tree.getroot()       # récupère la racine de l'arbre
    return root

def parse_all(root):
    host_elements = root.findall("host")  # récupère tous les éléments <host>

    results = []

    for hosts in host_elements:
        results.append(parse_host(hosts))  # appelle parse_host pour chaque host

    return results  # retourne la liste finale de dictionnaires

def parse_host(host_element):
    hostname = "unknow"  # valeurs par défaut au cas où certaines infos sont absentes
    ipv6 = "unknow"
    ipv4 = "unknow"
    mac = "unknow"
    status = "unknow"

    # récupération du nom d'hôte
    hostname_element = host_element.find("hostnames/hostname")  

    try: 
        hostname_element.get("name")
    except AttributeError:
        pass
    else:
        hostname = hostname_element.get("name")  # récupère le nom s'il existe

    # récupération du statut de l'hôte
    status_element = host_element.find("status")
    status = status_element.get("state")

    # récupération des adresses
    addresses = host_element.findall("address")
    for addr in addresses:
        if addr.get("addrtype") == "ipv4":
            ipv4 = addr.get("addr")
        elif addr.get("addrtype") == "ipv6":
            ipv6 = addr.get("addr")
        elif addr.get("addrtype") == "mac":
            mac = addr.get("addr")

    # construit le dictionnaire final pour cet hôte
    dictionnary = {
        "hostname": hostname,
        "status": status,
        "ipv4": ipv4,
        "ipv6": ipv6,
        "mac": mac,
        "ports": parse_ports(host_element)  # récupère uniquement les ports ouverts
    }

    return dictionnary


def parse_ports(host_element):
    ports_element = host_element.findall("ports/port")  # récupère tous les ports de l'hôte

    dicts_ports = []

    for ports in ports_element:
        id_port = int(ports.get("portid"))
        protocol_port = ports.get("protocol")

        state_port_element = ports.find("state")
        state_port = state_port_element.get("state")  # "open", "closed", "filtered"

        service_port_element = ports.find("service")
        try: 
            service_port_element.get("name")
        except AttributeError:
            service_port = "unknow"  # si aucun service détecté
        else:
            service_port = service_port_element.get("name")

        # construit le dictionnaire pour ce port
        global dictionnary_0
        dictionnary_0 = {
            "port": id_port,
            "protocol": protocol_port,
            "state": state_port,
            "service": service_port
        }

        if dictionnary_0["state"] == "open":  # **filtre uniquement les ports ouverts**
            dicts_ports.append(dictionnary_0)

    """ 
    # Optionnel : pour inclure les ports filtrés ou non scannés par Nmap
    extra_ports_element = host_element.find("ports/extraports/extrareasons")
    extra_ports = extra_ports_element.get("ports")
    extra_ports_dict = {"filtred or unknown":extra_ports}
    dicts_ports.append(extra_ports_dict)
    """

    return dicts_ports
