# Script da eseguire DOPO il riavvio
# Questo completa l'installazione e crea l'APK

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Completamento Installazione WSL" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica WSL
Write-Host "Verifica WSL..." -ForegroundColor Yellow
try {
    $null = wsl --status 2>&1
    Write-Host "OK: WSL disponibile" -ForegroundColor Green
} catch {
    Write-Host "ERRORE: WSL non disponibile" -ForegroundColor Red
    Write-Host "Attendi qualche secondo e riprova" -ForegroundColor Yellow
    exit 1
}

# Verifica Ubuntu
Write-Host ""
Write-Host "Verifica Ubuntu..." -ForegroundColor Yellow
$wslList = wsl --list
if ($wslList -match "Ubuntu") {
    Write-Host "OK: Ubuntu trovato" -ForegroundColor Green
    Write-Host ""
    Write-Host "Ubuntu e gia installato!" -ForegroundColor Green
    Write-Host "Procedo con la build dell'APK..." -ForegroundColor Cyan
    Write-Host ""
    
    # Esegui build
    .\build_simple.ps1
} else {
    Write-Host "Ubuntu non trovato" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Installazione Ubuntu..." -ForegroundColor Cyan
    Write-Host "Questo richiedera alcuni minuti..." -ForegroundColor Gray
    Write-Host ""
    
    wsl --install -d Ubuntu
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "OK: Ubuntu installato!" -ForegroundColor Green
        Write-Host ""
        Write-Host "IMPORTANTE:" -ForegroundColor Yellow
        Write-Host "1. Apri Ubuntu dal menu Start" -ForegroundColor White
        Write-Host "2. Configura username e password" -ForegroundColor White
        Write-Host "3. Poi esegui di nuovo: .\dopo_riavvio.ps1" -ForegroundColor White
    } else {
        Write-Host ""
        Write-Host "ATTENZIONE: Errore durante installazione Ubuntu" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Prova a installare Ubuntu da Microsoft Store:" -ForegroundColor Cyan
        Write-Host "1. Apri Microsoft Store" -ForegroundColor White
        Write-Host "2. Cerca 'Ubuntu'" -ForegroundColor White
        Write-Host "3. Clicca 'Installa'" -ForegroundColor White
        Write-Host "4. Dopo l'installazione, esegui: .\dopo_riavvio.ps1" -ForegroundColor White
    }
}

Write-Host ""
Write-Host "Premi un tasto per uscire..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

