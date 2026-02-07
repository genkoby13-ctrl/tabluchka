#!/bin/bash
# Script per creare APK Android con Buildozer
# Usa questo script in WSL o Linux

echo "=========================================="
echo "Build APK per Таблиця x÷ Тренажер"
echo "=========================================="

# Verifica che buildozer sia installato
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer non trovato!"
    echo "Installa con: pip3 install --user buildozer"
    exit 1
fi

# Verifica che buildozer.spec esista
if [ ! -f "buildozer.spec" ]; then
    echo "❌ File buildozer.spec non trovato!"
    exit 1
fi

echo ""
echo "Scegli il tipo di build:"
echo "1) Debug APK (più veloce, per test)"
echo "2) Release APK (per distribuzione)"
read -p "Scelta (1 o 2): " choice

case $choice in
    1)
        echo ""
        echo "🔨 Creazione APK Debug..."
        buildozer android debug
        ;;
    2)
        echo ""
        echo "🔨 Creazione APK Release..."
        buildozer android release
        ;;
    *)
        echo "❌ Scelta non valida!"
        exit 1
        ;;
esac

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build completata con successo!"
    echo ""
    echo "APK trovato in: bin/"
    ls -lh bin/*.apk 2>/dev/null || echo "Nessun APK trovato"
else
    echo ""
    echo "❌ Errore durante la build!"
    exit 1
fi

