# Script per installare WSL - RICHIEDE AMMINISTRATORE
# Esegui questo script come Amministratore

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Installazione WSL e Ubuntu" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica privilegi amministratore
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERRORE: Questo script richiede privilegi amministratore!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Istruzioni:" -ForegroundColor Yellow
    Write-Host "1. Clic destro su PowerShell" -ForegroundColor White
    Write-Host "2. Seleziona 'Esegui come amministratore'" -ForegroundColor White
    Write-Host "3. Vai alla cartella: cd C:\tabluchka" -ForegroundColor White
    Write-Host "4. Esegui: .\installa_wsl_admin.ps1" -ForegroundColor White
    exit 1
}

Write-Host "OK: Privilegi amministratore verificati" -ForegroundColor Green
Write-Host ""

# Abilita WSL
Write-Host "Abilitazione WSL..." -ForegroundColor Yellow
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
if ($LASTEXITCODE -ne 0) {
    Write-Host "ATTENZIONE: Errore durante l'abilitazione WSL" -ForegroundColor Yellow
}

# Abilita Virtual Machine Platform
Write-Host "Abilitazione Virtual Machine Platform..." -ForegroundColor Yellow
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
if ($LASTEXITCODE -ne 0) {
    Write-Host "ATTENZIONE: Errore durante l'abilitazione VMP" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Installazione Ubuntu" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Installa Ubuntu
Write-Host "Installazione Ubuntu..." -ForegroundColor Yellow
Write-Host "Questo potrebbe richiedere alcuni minuti..." -ForegroundColor Gray
wsl --install -d Ubuntu

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  Installazione Completata!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Prossimi passi:" -ForegroundColor Cyan
    Write-Host "1. Se richiesto, RIAVVIA il computer" -ForegroundColor Yellow
    Write-Host "2. Dopo il riavvio, apri Ubuntu dal menu Start" -ForegroundColor Yellow
    Write-Host "3. Configura username e password per Ubuntu" -ForegroundColor Yellow
    Write-Host "4. Poi esegui: .\build_simple.ps1" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "ATTENZIONE: Potrebbe essere necessario un riavvio" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Prova a:" -ForegroundColor Cyan
    Write-Host "1. Riavviare il computer" -ForegroundColor White
    Write-Host "2. Poi eseguire: wsl --install -d Ubuntu" -ForegroundColor White
    Write-Host "3. Oppure installare Ubuntu da Microsoft Store" -ForegroundColor White
}

Write-Host ""
Write-Host "Premi un tasto per uscire..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

