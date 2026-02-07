# Script PowerShell per creare automaticamente l'APK Android
# Questo script installa WSL, configura tutto e crea l'APK

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Build APK Automatico" -ForegroundColor Cyan
Write-Host "  Таблиця x÷ Тренажер" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se siamo amministratori
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠️  Questo script richiede privilegi amministratore!" -ForegroundColor Yellow
    Write-Host "   Eseguire PowerShell come Amministratore e riprovare." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   Clic destro su PowerShell > Esegui come amministratore" -ForegroundColor Yellow
    exit 1
}

# Funzione per verificare se WSL è installato
function Test-WSLInstalled {
    try {
        $wslList = wsl --list --quiet 2>&1
        if ($LASTEXITCODE -eq 0) {
            return $true
        }
        return $false
    } catch {
        return $false
    }
}

# Funzione per installare WSL
function Install-WSL {
    Write-Host "📦 Installazione WSL2..." -ForegroundColor Yellow
    Write-Host "   Questo richiederà alcuni minuti..." -ForegroundColor Gray
    
    # Abilita WSL
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    
    Write-Host "   ⚠️  Riavvia il computer e poi esegui di nuovo questo script!" -ForegroundColor Yellow
    Write-Host "   Dopo il riavvio, WSL installerà automaticamente Ubuntu." -ForegroundColor Gray
    exit 0
}

# Verifica WSL
Write-Host "🔍 Verifica WSL..." -ForegroundColor Cyan
if (-not (Test-WSLInstalled)) {
    Write-Host "   ❌ WSL non trovato" -ForegroundColor Red
    $install = Read-Host "   Installare WSL2? (S/N)"
    if ($install -eq "S" -or $install -eq "s") {
        Install-WSL
    } else {
        Write-Host "   ❌ WSL è necessario per creare l'APK" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "   ✅ WSL trovato" -ForegroundColor Green
}

# Verifica distribuzione Ubuntu
Write-Host ""
Write-Host "🔍 Verifica distribuzione Linux..." -ForegroundColor Cyan
$wslList = wsl --list --quiet
if ($wslList -notmatch "Ubuntu") {
    Write-Host "   ⚠️  Ubuntu non trovato" -ForegroundColor Yellow
    Write-Host "   Installazione Ubuntu..." -ForegroundColor Yellow
    wsl --install -d Ubuntu
    Write-Host "   ⚠️  Configura Ubuntu al primo avvio, poi esegui di nuovo questo script" -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "   ✅ Ubuntu trovato" -ForegroundColor Green
}

# Lo script bash è già creato come build_in_wsl.sh

Write-Host ""
Write-Host "Esecuzione build in WSL..." -ForegroundColor Cyan
Write-Host "ATTENZIONE: Questo richiedera molto tempo" -ForegroundColor Yellow
Write-Host "La prima build puo richiedere 30-60 minuti" -ForegroundColor Yellow
Write-Host ""

# Esegui lo script in WSL
wsl bash build_in_wsl.sh

# Verifica risultato
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  ✅ APK creato con successo!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 APK trovato in: bin/" -ForegroundColor Cyan
    Write-Host ""
    
    # Mostra file APK
    if (Test-Path "bin\*.apk") {
        Get-ChildItem "bin\*.apk" | ForEach-Object {
            $sizeMB = [math]::Round($_.Length/1MB, 2)
            Write-Host "   APK: $($_.Name) ($sizeMB MB)" -ForegroundColor Green
        }
    }
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  ❌ Errore durante la build" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Controlla i messaggi di errore sopra." -ForegroundColor Yellow
}

# Nota: build_in_wsl.sh viene mantenuto per uso futuro

Write-Host ""
Write-Host "Premi un tasto per uscire..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

