# Installation — guide (PC, Windows)

Ce guide part de zéro sur Windows (ou WSL). Python est désormais installé
et le dossier du projet est créé.

---

## 1. Installer Python

- Télécharger Python 3.10+ depuis https://www.python.org/downloads/
- **Cocher "Add Python to PATH"** lors de l'installation.
- Vérifier : ouvre un terminal et tape `python --version`.

---

## 2. Cloner ou ouvrir le projet

```bash
cd C:\wsl.localhost\Ubuntu\home\Guilmar\code\Guilmar-Khaanthar
git clone https://github.com/<ton-nom-de-compte>/jeu-mobil1v1.git
cd jeu-mobil1v1
```

---

## 3. Créer un environnement virtuel

```bash
python -m venv venv
```

Active le venv :

- **Windows** : `venv\Scripts\activate`
- **macOS/Linux** : `source venv/bin/activate`

---

## 4. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **À savoir** : Kivy compile desmodules C à l'installation.
> Sur Windows, si cela échoue, installe d'abord le compilateur
> Microsoft Visual C++ (via "Building C/C++ extension" sur
> le site officiel de Kivy) ou utilise un binaire pré-construit.

---

## 5. Lancer le jeu (PC)

```bash
python -m src.main
```

ou :

```bash
python src/main.py
```

---

## Vérifier l'installation

Ouvre un interpréteur Python et tape :

```python
import kivy
print(kivy.__version__)
```

Si aucune erreur ne s'affiche, Kivy est bien installé.
