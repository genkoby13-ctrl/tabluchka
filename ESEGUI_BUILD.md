# 🚀 Esegui Build APK - Istruzioni Semplici

## ⚡ Metodo Veloce (Se WSL è già installato)

Se hai già WSL e Ubuntu installati, esegui semplicemente:

```powershell
wsl bash build_in_wsl.sh
```

Questo farà tutto automaticamente!

## 📋 Metodo Completo (Prima volta)

### Passo 1: Installa WSL (solo se non presente)

Apri PowerShell **come Amministratore** e esegui:

```powershell
wsl --install
```

Poi **riavvia il computer**.

### Passo 2: Configura Ubuntu

Dopo il riavvio:
1. Apri Ubuntu dal menu Start
2. Crea un utente (username e password)
3. Attendi il completamento

### Passo 3: Esegui la Build

Apri PowerShell normale (non serve amministratore) e esegui:

```powershell
cd C:\tabluchka
wsl bash build_in_wsl.sh
```

## ⏱️ Tempi

- **Prima build**: 30-60 minuti (scarica SDK, NDK, ecc.)
- **Build successive**: 5-10 minuti

## 📱 Output

L'APK sarà in: `bin/tabluchka-0.1-arm64-v8a-debug.apk`

## ❓ Problemi?

### WSL non trovato
```powershell
# Installa WSL (richiede amministratore)
wsl --install
```

### Ubuntu non trovato
```powershell
# Installa Ubuntu
wsl --install -d Ubuntu
```

### Errore durante build
- Controlla la connessione Internet
- Assicurati di avere ~10GB spazio libero
- Verifica i messaggi di errore

## 🎯 Alternativa: Script Automatico

Se preferisci, puoi usare lo script PowerShell automatico:

```powershell
# Come Amministratore
.\build_apk_auto.ps1
```

---

**Nota**: La prima build è lenta perché scarica tutto il necessario (SDK Android, NDK, ecc.). Le build successive sono molto più veloci!

