# ✅ Dopo il Riavvio - Passi Finali

## Cosa è Stato Fatto

✅ WSL (Windows Subsystem for Linux) abilitato
✅ Virtual Machine Platform abilitata

## Cosa Fare Dopo il Riavvio

### Passo 1: Riavvia il Computer

Riavvia ora il computer per completare l'installazione.

### Passo 2: Installa Ubuntu

Dopo il riavvio, apri PowerShell (normale, non serve amministratore) e esegui:

```powershell
cd C:\tabluchka
wsl --install -d Ubuntu
```

Oppure installa Ubuntu da **Microsoft Store** (più semplice):
1. Apri Microsoft Store
2. Cerca "Ubuntu"
3. Clicca "Installa"

### Passo 3: Configura Ubuntu

1. Apri **Ubuntu** dal menu Start
2. Attendi l'installazione (prima volta)
3. Crea un **username** quando richiesto
4. Crea una **password** quando richiesto
5. Conferma la password

### Passo 4: Crea l'APK

Dopo che Ubuntu è configurato, esegui:

```powershell
cd C:\tabluchka
.\build_simple.ps1
```

Lo script farà automaticamente tutto il resto!

## Verifica

Per verificare che tutto sia OK:

```powershell
wsl --list --verbose
```

Dovresti vedere Ubuntu nella lista.

---

**Nota**: La prima build dell'APK richiede 30-60 minuti perché scarica SDK Android, NDK, ecc.

