# 📝 Application de To-Do Liste Personnelle

Ce projet est une **application de gestion de tâches** conçue pour **mon usage personnel**.

L'objectif est de centraliser plusieurs fonctionnalités utiles au quotidien.

Fonctionnalités prévues :
- ⏱️ Chronomètre Pomodoro
- 🌤️ Affichage de la météo
- 🧩 Autres modules pratiques à venir

---

## ⚙️ Pré-requis

Avoir **Python 3** installé sur votre machine.

### Vérifier l'installation de Python

```bash
python --version
# ou
python3 --version
```
## Utilisation de l’environnement virtuel (venv)

🔍 Vérifier si un environnement virtuel existe déjà
```bash
ls venv
```

➕ Créer un environnement virtuel
```bash
python -m venv venv
# ou
python3 -m venv venv
```
🚀 Activer l’environnement virtuel


Windows os:
```bash
venv\Scripts\activate
```

macos and linux
```bash
source venv/bin/activate
```

Installer les dépendances

Si un fichier `requirements.txt` est présent :

```bash
pip install -r requirements.txt
````
💾 Sauvegarder les dépendances
```bash
pip freeze > requirements.txt
````
▶️ Lancer l’application
````bash
python main.py
# ou
python3 main.py
````

📌 Remarques

    L’environnement virtuel doit être activé à chaque session de travail.

    Ce projet est en cours d’évolution et sera enrichi régulièrement.
