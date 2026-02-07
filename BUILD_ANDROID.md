# Istruzioni per creare APK Android

## ⚠️ IMPORTANTE: Requisiti Python

**Kivy e Buildozer richiedono Python 3.8-3.12. Python 3.14 NON è supportato.**

## Opzioni per creare l'APK

### Opzione 1: Usare WSL (Windows Subsystem for Linux) - CONSIGLIATO

1. **Installa WSL2** (se non già installato):
   ```powershell
   wsl --install
   ```

2. **Installa Ubuntu** da Microsoft Store

3. **Apri Ubuntu** e installa le dipendenze:
   ```bash
   sudo apt update
   sudo apt install -y git unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   ```

4. **Installa Buildozer**:
   ```bash
   pip3 install --user buildozer
   export PATH=$PATH:~/.local/bin
   ```

5. **Copia il progetto in WSL**:
   ```bash
   # Dal terminale Windows, copia i file in WSL
   # Oppure lavora direttamente in WSL
   ```

6. **Compila l'APK**:
   ```bash
   cd /mnt/c/tabluchka  # o il percorso del tuo progetto
   buildozer android debug
   ```

### Opzione 2: Usare Docker

1. **Installa Docker Desktop** per Windows

2. **Crea un Dockerfile** (già incluso se necessario)

3. **Usa l'immagine Buildozer**:
   ```bash
   docker run --interactive --tty --volume "%cd%":/home/user/hostcwd kivy/buildozer buildozer android debug
   ```

### Opzione 3: Usare una VM Linux

1. Installa VirtualBox o VMware
2. Installa Ubuntu nella VM
3. Segui i passaggi dell'Opzione 1

## Configurazione Buildozer

Il file `buildozer.spec` è già configurato con:
- Nome app: Таблиця x÷ Тренажер
- Package: org.tabluchka
- Versione: 0.1
- Orientamento: Portrait
- Architetture: arm64-v8a, armeabi-v7a

## Comandi Buildozer

```bash
# Prima build (scarica tutto)
buildozer android debug

# Build successiva (più veloce)
buildozer android debug

# Build release (firmata)
buildozer android release

# Pulizia
buildozer android clean
```

## Risoluzione Problemi

### Errore: "buildozer: command not found"
```bash
export PATH=$PATH:~/.local/bin
# Oppure aggiungi a ~/.bashrc
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
```

### Errore: Java non trovato
```bash
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

### Errore: Android SDK
Buildozer scaricherà automaticamente Android SDK e NDK alla prima build.

## File Output

L'APK sarà creato in:
- **Debug**: `bin/tabluchka-0.1-arm64-v8a-debug.apk`
- **Release**: `bin/tabluchka-0.1-arm64-v8a-release-unsigned.apk`

## Test dell'APK

1. Abilita "Origini sconosciute" sul tuo dispositivo Android
2. Trasferisci l'APK sul dispositivo
3. Apri e installa l'APK

## Note

- La prima build può richiedere 30-60 minuti (scarica SDK, NDK, ecc.)
- Le build successive sono più veloci (5-10 minuti)
- Assicurati di avere almeno 10GB di spazio libero

