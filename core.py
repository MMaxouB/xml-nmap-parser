import os
import xml.etree.ElementTree as ET
import json
from nmap_parser import load_xml, parse_all  # import des fonctions définies pour parser le XML Nmap

path_file = "rapport.xml"
output_file = "output.json"

if not os.path.exists(path_file):
    raise ValueError("fichier introuvable !!")  # vérifie que le fichier XML existe avant de continuer

load_xml(path_file)  # charge le XML, retourne la racine (ElementTree)
result = parse_all(load_xml(path_file))  # parse tout le XML et construction la liste de dictionnaires

with open(output_file, "w") as f:
    json.dump(result, f ,indent=4)  # écrit le résultat formaté JSON dans output.json

with open(output_file, "r", encoding="utf-8") as file:
    data = json.load(file)  # recharge le JSON pour vérifier le résultat ou l'utiliser
    print(data)  # affiche les données pour debug
