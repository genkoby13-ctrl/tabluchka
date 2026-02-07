# 🔧 Risoluzione Problema WSL

## Problema Rilevato

L'installazione di WSL ha riscontrato l'errore `0x80244022`, che indica un problema con Windows Update.

## Soluzioni

### Opzione 1: Riavvia e Riprova (Consigliato)

1. **Riavvia il computer**
2. Apri PowerShell **come Amministratore**
3. Esegui:
   ```powershell
   wsl --install
   ```

### Opzione 2: Installa Manualmente le Componenti

Apri PowerShell **come Amministratore** e esegui:

```powershell
# Abilita WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Riavvia il computer
shutdown /r /t 0
```

Dopo il riavvio:
```powershell
# Installa Ubuntu
wsl --install -d Ubuntu
```

### Opzione 3: Risolvi Windows Update

1. Apri **Impostazioni Windows**
2. Vai a **Aggiornamento e sicurezza**
3. Clicca su **Risoluzione dei problemi**
4. Esegui **Risoluzione problemi di Windows Update**
5. Poi riprova `wsl --install`

### Opzione 4: Installa da Microsoft Store

1. Apri **Microsoft Store**
2. Cerca "Ubuntu"
3. Installa **Ubuntu** (versione LTS consigliata)
4. Apri Ubuntu e completa la configurazione

## Dopo l'Installazione

Una volta che WSL e Ubuntu sono installati:

1. Apri PowerShell normale (non serve amministratore)
2. Vai alla cartella del progetto:
   ```powershell
   cd C:\tabluchka
   ```
3. Esegui lo script:
   ```powershell
   .\build_simple.ps1
   ```

## Verifica Installazione

Per verificare se WSL è installato:

```powershell
wsl --status
wsl --list --verbose
```

Se vedi Ubuntu nella lista, sei pronto!

## Note

- L'installazione di WSL richiede un riavvio del computer
- Dopo il riavvio, Ubuntu si configurerà automaticamente
- La prima build dell'APK richiede 30-60 minuti (scarica SDK/NDK)

## Alternativa: Usa Docker

Se WSL continua a dare problemi, puoi usare Docker:

```powershell
docker run --interactive --tty --volume "%cd%":/home/user/hostcwd kivy/buildozer buildozer android debug
```

---

**Una volta risolto, esegui di nuovo `build_simple.ps1`**

