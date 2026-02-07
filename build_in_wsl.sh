#!/bin/bash
set -e

echo "========================================"
echo "  Configurazione ambiente Buildozer"
echo "========================================"

# Aggiorna sistema
echo "Aggiornamento sistema..."
sudo apt update -qq

# Installa dipendenze
echo "Installazione dipendenze..."
sudo apt install -y -qq git unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Installa Buildozer
echo "Installazione Buildozer..."
pip3 install --user buildozer -q

# Aggiungi al PATH
export PATH=$PATH:$HOME/.local/bin
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc

# Vai alla directory del progetto
cd /mnt/c/tabluchka

echo ""
echo "========================================"
echo "  Build APK Android"
echo "========================================"
echo ""

# Prima build (può richiedere 30-60 minuti)
echo "Creazione APK Debug..."
echo "ATTENZIONE: La prima build può richiedere 30-60 minuti"
echo "Buildozer scaricherà SDK, NDK, ecc."
echo ""

buildozer android debug

BUILD_RESULT=$?
if [ $BUILD_RESULT -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "  Build completata con successo!"
    echo "========================================"
    echo ""
    echo "APK trovato in: bin/"
    ls -lh bin/*.apk 2>/dev/null || echo "Nessun APK trovato"
else
    echo ""
    echo "========================================"
    echo "  Errore durante la build"
    echo "========================================"
    exit 1
fi

