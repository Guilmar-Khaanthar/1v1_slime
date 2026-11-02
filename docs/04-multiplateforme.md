# Multi-plateforme — Android et iOS

Ce projet vise à s'exécuter sur **Android, iOS, PC, Mac et Linux**.
Kivy permet de compiler une application Android ou iOS à partir du code
Python, mais nécessite les outils natifs de chaque plateforme.

---

## Android (priorité 1 : mobil)

### Prérequis

- Sur Windows, Kivy (Python) installé.
- `buildozer` installé : `pip install buildozer buildozer-tools`
- Android SDK + NDK installés (installation via Buildozer, ou manuellement)
- Les variables d'environnement `ANDROID_HOME` et `ANDROID_SDK_ROOT`
  pointent vers le dossier Android SDK.
- Java JDK 17 (pour Android 14+), et `JAVA_HOME` défini.

### Fichier de build (buildozer.spec)

Un fichier `buildozer.spec` est créé dans le projet. Exemple des
parties importantes :

```ini
[app]
title = Slime Combat 1v1
package = com.slime.compot1v1
source.dir = .
source.include_exts = py,png,jpg,json,kv

[build_osx]
# (optionnel)
```

### Compiler

```bash
buildozer -v android debug
```

Cela génère un `.apk` (ou `.aab`) dans le dossier `bin/`.
Il peut être installé sur un téléphone Android via :

```bash
adb install bin/<mon-jeu>.apk
```

### Sur un vrai téléphone

- Active le mode débogage USB dans les paramètres du téléphone.
- Connecte-le à l'ordinateur.
- Installe l'APK avec `adb install`.

---

## iOS (priorité 2)

Kivy supporte iOS via `beebox` (empaquetage) ou via Xcode pour les
versions plus avancées. La procédure est plus complexe et demande
les outils Apple : Xcode, command-line tools, certificats.

### Prérequis

- Mac OS
- Xcode installé (et command-line tools)
- `pip install beebox`
- Un compte Apple développeur (necessary pour signer l'app)

### Compiler

```bash
pip install beebox
beebox --app SlimeCombat
```

Les artefacts se trouvent dans `build/`.

> ⚠️ iOS est une phase ultérieure ici. Ne créez pas de fichier
> `buildozer.spec` pour iOS en priorité, le tout reste à valider
> après l'Android.

---

## PC / macOS / Linux (priorité 3)

Sur ces plateformes, exécutez simplement :

```bash
python -m src.main
```

Pour les livrer, il faut « packager » l'application pour qu'elle
s'ouvre comme un exécutable. Kivy offre `kivy.demo` et `pyinstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile --name SlimeCombat src/main.py
```

Le binaire va dans `dist/SlimeCombat`.
