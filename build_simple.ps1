# Script semplificato per build APK
# Non richiede privilegi amministratore (solo se WSL è già installato)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Build APK - Script Semplificato" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica WSL
Write-Host "Verifica WSL..." -ForegroundColor Yellow
try {
    $null = wsl --list --quiet 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERRORE: WSL non trovato!" -ForegroundColor Red
        Write-Host ""
        Write-Host "Installa WSL con:" -ForegroundColor Yellow
        Write-Host "  wsl --install" -ForegroundColor White
        Write-Host ""
        Write-Host "NOTA: Richiede PowerShell come Amministratore" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "OK: WSL trovato" -ForegroundColor Green
} catch {
    Write-Host "ERRORE: WSL non trovato!" -ForegroundColor Red
    Write-Host "Installa WSL prima di continuare" -ForegroundColor Yellow
    exit 1
}

# Verifica Ubuntu
Write-Host ""
Write-Host "Verifica Ubuntu..." -ForegroundColor Yellow
$wslList = wsl --list
if ($wslList -notmatch "Ubuntu") {
    Write-Host "ATTENZIONE: Ubuntu non trovato" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Installa Ubuntu con:" -ForegroundColor Yellow
    Write-Host "  wsl --install -d Ubuntu" -ForegroundColor White
    Write-Host ""
    Write-Host "Poi configura Ubuntu e riprova" -ForegroundColor Yellow
    exit 1
}
Write-Host "OK: Ubuntu trovato" -ForegroundColor Green

# Verifica script bash
Write-Host ""
Write-Host "Verifica script build..." -ForegroundColor Yellow
if (-not (Test-Path "build_in_wsl.sh")) {
    Write-Host "ERRORE: build_in_wsl.sh non trovato!" -ForegroundColor Red
    exit 1
}
Write-Host "OK: Script trovato" -ForegroundColor Green

# Esegui build
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Avvio Build APK" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "ATTENZIONE: La prima build richiede 30-60 minuti" -ForegroundColor Yellow
Write-Host "Buildozer scarichera SDK, NDK e altre dipendenze" -ForegroundColor Yellow
Write-Host ""
Write-Host "Premi INVIO per continuare o CTRL+C per annullare..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Write-Host ""
Write-Host "Esecuzione in corso..." -ForegroundColor Cyan
Write-Host ""

# Esegui in WSL
wsl bash build_in_wsl.sh

# Verifica risultato
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  Build Completata!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    
    if (Test-Path "bin\*.apk") {
        Write-Host "APK creati:" -ForegroundColor Cyan
        Get-ChildItem "bin\*.apk" | ForEach-Object {
            $sizeMB = [math]::Round($_.Length/1MB, 2)
            Write-Host "  - $($_.Name) ($sizeMB MB)" -ForegroundColor Green
        }
    } else {
        Write-Host "Nessun APK trovato in bin/" -ForegroundColor Yellow
    }
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  Errore durante la build" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Controlla i messaggi di errore sopra" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Premi un tasto per uscire..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

