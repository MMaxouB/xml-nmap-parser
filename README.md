# XML Nmap Parser (Python)

Un petit outil en Python permettant de **convertir un scan Nmap au format XML en un fichier JSON propre**, ne contenant que les informations réellement utiles (hosts + ports ouverts).

Ce projet s’inscrit dans un cadre **d’apprentissage des bases de la cybersécurité**, et a été réalisé entièrement par moi dans le but de comprendre :
- comment analyser un fichier XML Nmap,
- comment extraire des informations réseau pertinentes,
- et comment structurer ces données dans un JSON clair.

Si vous avez la moindre suggestion/commentaire n'hésitez pas 😉

---

## 📁 Fonctionnement général

**Entrée :** un fichier XML généré par Nmap  
  Exemple :  
  ```bash
  nmap -oX scan.xml 192.168.1.0/24
```
Sortie : un fichier output.json contenant uniquement :

- les hosts détectés,

- leur état (up/down),

- leurs adresses (ipv4, ipv6, mac),

- et leurs ports ouverts uniquement (ports filtrés en option inscrit dans le code).

🚀 Lancer le programme
Dans un terminal :
```
  python3 core.py scan.xml
```

📦 Structure du projet
``` bash
# output.json
XML-nmap-parser/
│
├── core.py           # Script principal
├── parser.py         # Fonctions de parsing XML
│
├── scan.xml          # Exemple de fichier d'entrée
├── output.json       # Exemple de fichier de sortie
│
└── README.md         # Documentation du projet

```
📜 Exemple de sortie JSON
```
{
  "hosts": [
    {
      "hostname": "unknown",
      "status": "up",
      "ipv4": "192.168.1.1",
      "ports": [
        {
          "port": 80,
          "protocol": "tcp",
          "service": "http"
        }
      ]
    }
  ]
}
```

🧠 Objectif pédagogique
Ce projet m’a permis d’apprendre :

-le parsing XML en Python (xml.etree.ElementTree),

-la structuration propre de données,

-les bases de Nmap,

-comment filtrer uniquement les ports pertinents.

🔧 Dépendances
Aucune dépendance externe.
Le projet utilise uniquement les modules Python standards.

📄 Licence
Projet d’apprentissage – libre d'utilisation à but éducatif ou d'utilisation
