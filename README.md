# XML Nmap Parser (Python)

Un petit outil en Python permettant de **convertir un scan Nmap au format XML en un fichier JSON propre**, ne contenant que les informations réellement utiles (hosts + ports ouverts).

Ce projet s’inscrit dans un cadre **d’apprentissage des bases de la cybersécurité**, et a été réalisé entièrement par moi dans le but de comprendre :
- comment analyser un fichier XML Nmap,
- comment extraire des informations réseau pertinentes,
- et comment structurer ces données dans un JSON clair.

---

## 📁 Fonctionnement général

- **Entrée :** un fichier XML généré par Nmap  
  Exemple :  
  ```bash
  nmap -oX scan.xml 192.168.1.0/24
Sortie : un fichier output.json contenant uniquement :

les hosts détectés,

leur état (up/down),

leurs adresses,

et leurs ports ouverts uniquement.

🚀 Lancer le programme
Dans un terminal :

bash
Copier le code
python3 core.py scan.xml
Vous obtiendrez :

lua
Copier le code
output.json
📦 Structure du projet
bash
Copier le code
XML-nmap-parser/
│
├── core.py           # Script principal
├── parser.py         # Fonctions de parsing XML
├── utils.py          # Fonctions utilitaires
│
├── scan.xml          # Exemple de fichier d'entrée (optionnel)
├── output.json       # Exemple de fichier de sortie (optionnel / peut rester vide)
│
└── README.md         # Documentation du projet
📜 Exemple de sortie JSON
json
Copier le code
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
🛑 Sécurité & confidentialité
⚠️ Attention : ne mettez jamais sur GitHub vos vrais scans Nmap !
Ils peuvent contenir :

les IP de votre réseau local,

des MAC addresses,

des noms d’hôtes,

des services ouverts.

Pour GitHub :

conservez uniquement le code,

ajoutez un output.json vide ou rempli avec des données fictives.

🧠 Objectif pédagogique
Ce projet m’a permis d’apprendre :

le parsing XML en Python (xml.etree.ElementTree),

la structuration propre de données,

les bases de Nmap,

comment filtrer uniquement les ports pertinents.

🔧 Dépendances
Aucune dépendance externe.
Le projet utilise uniquement les modules Python standards.

📄 Licence
Projet d’apprentissage – libre d'utilisation à but éducatif.

yaml
Copier le code

---

Si tu veux, je peux aussi te :
✔ générer un `.gitignore`  
✔ améliorer le README avec des images / schémas  
✔ ajouter un exemple de XML “safe” 100% fictif  
✔ réorganiser ton projet en structure professionnelle (src/, tests/, etc.)

Tu veux que je rajoute quelque chose ?
