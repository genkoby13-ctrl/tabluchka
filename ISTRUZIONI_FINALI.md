# 🎯 Istruzioni Finali per Creare APK

## Situazione Attuale

WSL non è ancora completamente installato a causa di un problema con Windows Update.

## Soluzione: Installa WSL Manualmente

### Opzione 1: Script Automatico (Consigliato)

1. **Apri PowerShell come Amministratore**:
   - Clic destro su PowerShell
   - Seleziona "Esegui come amministratore"

2. **Vai alla cartella del progetto**:
   ```powershell
   cd C:\tabluchka
   ```

3. **Esegui lo script di installazione**:
   ```powershell
   .\installa_wsl_admin.ps1
   ```

4. **Se richiesto, riavvia il computer**

5. **Dopo il riavvio**:
   - Apri Ubuntu dal menu Start
   - Configura username e password
   - Poi esegui: `.\build_simple.ps1`

### Opzione 2: Microsoft Store (Più Semplice)

1. Apri **Microsoft Store**
2. Cerca **"Ubuntu"**
3. Clicca **"Installa"** su Ubuntu (versione LTS)
4. Aspetta il completamento
5. Apri **Ubuntu** dal menu Start
6. Configura username e password quando richiesto
7. Poi esegui:
   ```powershell
   cd C:\tabluchka
   .\build_simple.ps1
   ```

### Opzione 3: Comando Manuale

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

## Dopo l'Installazione di Ubuntu

Una volta che Ubuntu è installato e configurato:

1. Apri PowerShell normale (non serve amministratore)
2. Esegui:
   ```powershell
   cd C:\tabluchka
   .\build_simple.ps1
   ```

Lo script farà automaticamente:
- ✅ Installazione dipendenze
- ✅ Configurazione Buildozer
- ✅ Creazione APK Android

## Tempi

- **Installazione WSL/Ubuntu**: 5-10 minuti
- **Prima build APK**: 30-60 minuti (scarica SDK/NDK)
- **Build successive**: 5-10 minuti

## Output

L'APK sarà creato in: `bin/tabluchka-0.1-arm64-v8a-debug.apk`

## Verifica

Per verificare se WSL è installato:

```powershell
wsl --list --verbose
```

Se vedi Ubuntu nella lista, sei pronto!

---

**Nota**: L'errore `0x80244022` è un problema comune con Windows Update. L'installazione da Microsoft Store spesso funziona meglio.

