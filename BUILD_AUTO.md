# 🤖 Build Automatica APK

## Script Automatico

Ho creato uno script PowerShell che automatizza **tutto il processo** di creazione dell'APK!

### Come Usare

1. **Apri PowerShell come Amministratore**:
   - Clic destro su PowerShell
   - Seleziona "Esegui come amministratore"

2. **Vai alla cartella del progetto**:
   ```powershell
   cd C:\tabluchka
   ```

3. **Esegui lo script**:
   ```powershell
   .\build_apk_auto.ps1
   ```

### Cosa Fa lo Script

Lo script automatizza:

1. ✅ **Verifica WSL** - Controlla se WSL è installato
2. ✅ **Installa WSL** - Se non presente, lo installa (richiede riavvio)
3. ✅ **Installa Ubuntu** - Se non presente, lo installa
4. ✅ **Installa dipendenze** - Java, Python, Buildozer, ecc.
5. ✅ **Configura ambiente** - Imposta tutto il necessario
6. ✅ **Crea APK** - Esegue la build automaticamente
7. ✅ **Mostra risultato** - Indica dove trovare l'APK

### Tempi

- **Prima esecuzione**: 30-60 minuti
  - Installazione WSL (se necessario): 5-10 min
  - Installazione dipendenze: 5-10 min
  - Download SDK/NDK: 20-40 min
  - Compilazione: 5-10 min

- **Esecuzioni successive**: 5-10 minuti
  - Solo compilazione

### Requisiti

- Windows 10/11
- Connessione Internet (per download SDK/NDK)
- ~10GB spazio libero
- Privilegi amministratore

### Note

- Se WSL non è installato, lo script lo installerà e chiederà di riavviare
- Dopo il riavvio, esegui di nuovo lo script
- La prima build è lenta perché scarica tutto il necessario
- Le build successive sono molto più veloci

### Output

L'APK sarà creato in: `bin/tabluchka-0.1-arm64-v8a-debug.apk`

### Problemi?

Se lo script fallisce:

1. Verifica di avere privilegi amministratore
2. Controlla la connessione Internet
3. Assicurati di avere spazio su disco sufficiente
4. Controlla i messaggi di errore nello script

Per dettagli, vedi `BUILD_ANDROID.md`

