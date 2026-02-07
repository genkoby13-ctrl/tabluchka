# 🚀 Quick Start Guide

## Test Rapido del Codice

```bash
python test_app.py
```

## Esecuzione dell'App (richiede Python 3.11/3.12)

```bash
# Installa Kivy
pip install kivy

# Esegui l'app
python main.py
```

## Creazione APK Android

### Opzione 1: WSL (Consigliato)

1. **Installa WSL2**:
   ```powershell
   wsl --install
   ```

2. **Apri Ubuntu** e installa dipendenze:
   ```bash
   sudo apt update
   sudo apt install -y git unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   ```

3. **Installa Buildozer**:
   ```bash
   pip3 install --user buildozer
   export PATH=$PATH:~/.local/bin
   ```

4. **Compila APK**:
   ```bash
   cd /mnt/c/tabluchka
   chmod +x build_apk.sh
   ./build_apk.sh
   ```

   Oppure direttamente:
   ```bash
   buildozer android debug
   ```

### Opzione 2: Docker

```bash
docker run --interactive --tty --volume "%cd%":/home/user/hostcwd kivy/buildozer buildozer android debug
```

## File del Progetto

- `main.py` - Codice principale dell'app
- `buildozer.spec` - Configurazione per Android
- `requirements.txt` - Dipendenze Python
- `test_app.py` - Script di test
- `build_apk.sh` - Script helper per build (Linux/WSL)

## Troubleshooting

### Python 3.14 non supportato
**Soluzione**: Installa Python 3.11 o 3.12

### Buildozer non trovato
```bash
export PATH=$PATH:~/.local/bin
# Oppure aggiungi a ~/.bashrc
```

### Errore Java
```bash
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

### Prima build lenta
Normale! La prima build scarica SDK, NDK, ecc. (30-60 minuti)
Le build successive sono più veloci (5-10 minuti)

## Output

L'APK sarà in: `bin/tabluchka-0.1-arm64-v8a-debug.apk`

## Supporto

Per dettagli completi, vedi:
- `README.md` - Documentazione completa
- `BUILD_ANDROID.md` - Guida dettagliata Android

