# 🚀 Build APK con GitHub Actions (Senza WSL!)

## ✅ Soluzione Alternativa: GitHub Actions

Non serve WSL! GitHub Actions builda l'APK automaticamente nel cloud.

## Come Funziona

1. **Carica il codice su GitHub**
2. **GitHub Actions builda automaticamente l'APK**
3. **Scarica l'APK** dalla pagina Actions

## Passi

### 1. Crea Repository GitHub

1. Vai su [github.com](https://github.com)
2. Clicca **"New repository"**
3. Nome: `tabluchka` (o qualsiasi nome)
4. Clicca **"Create repository"**

### 2. Carica il Codice

Apri PowerShell nella cartella del progetto:

```powershell
cd C:\tabluchka

# Inizializza Git (se non già fatto)
git init

# Aggiungi tutti i file
git add .

# Commit
git commit -m "Initial commit - Tabluchka app"

# Aggiungi repository remoto (sostituisci USERNAME con il tuo)
git remote add origin https://github.com/USERNAME/tabluchka.git

# Carica il codice
git branch -M main
git push -u origin main
```

### 3. Avvia la Build

1. Vai su GitHub nella tua repository
2. Clicca su **"Actions"**
3. Clicca su **"Build Android APK"** (a sinistra)
4. Clicca **"Run workflow"** (a destra)
5. Clicca il pulsante verde **"Run workflow"**

### 4. Scarica l'APK

1. Aspetta che la build finisca (circa 30-60 minuti la prima volta)
2. Clicca sulla build completata
3. Scorri in basso a **"Artifacts"**
4. Clicca su **"android-apk"**
5. Scarica il file `.apk`

## Vantaggi

✅ **Nessuna installazione locale** - Tutto nel cloud
✅ **Gratuito** - GitHub Actions è gratuito per progetti pubblici
✅ **Automatico** - Builda ad ogni push
✅ **Funziona sempre** - Non dipende dal tuo PC

## File Creati

Ho già creato il file `.github/workflows/build_apk.yml` che contiene tutto il necessario!

## Alternativa: Script Automatico

Se preferisci, posso creare uno script che:
1. Inizializza Git
2. Crea il repository
3. Carica tutto automaticamente

Dimmi se vuoi che lo faccia!

