# Script per configurare GitHub e buildare APK automaticamente

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup GitHub per Build APK" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica Git
Write-Host "Verifica Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "OK: Git trovato - $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "ERRORE: Git non trovato!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Installa Git da: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Questo script:" -ForegroundColor Cyan
Write-Host "1. Inizializza Git (se necessario)" -ForegroundColor White
Write-Host "2. Prepara il repository" -ForegroundColor White
Write-Host "3. Ti guida per caricare su GitHub" -ForegroundColor White
Write-Host ""

$continue = Read-Host "Continuare? (S/N)"
if ($continue -ne "S" -and $continue -ne "s") {
    exit 0
}

# Inizializza Git se necessario
if (-not (Test-Path ".git")) {
    Write-Host ""
    Write-Host "Inizializzazione Git..." -ForegroundColor Yellow
    git init
    Write-Host "OK: Git inizializzato" -ForegroundColor Green
}

# Crea .gitignore se non esiste
if (-not (Test-Path ".gitignore")) {
    Write-Host ""
    Write-Host "Creazione .gitignore..." -ForegroundColor Yellow
    @"
# Python
__pycache__/
*.py[cod]
*.so
.Python

# Buildozer
.bin/
.buildozer/
*.apk
*.aab

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Host "OK: .gitignore creato" -ForegroundColor Green
}

# Aggiungi file
Write-Host ""
Write-Host "Aggiunta file a Git..." -ForegroundColor Yellow
git add .
Write-Host "OK: File aggiunti" -ForegroundColor Green

# Commit
Write-Host ""
Write-Host "Creazione commit..." -ForegroundColor Yellow
git commit -m "Initial commit - Tabluchka multiplication table trainer" 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK: Commit creato" -ForegroundColor Green
} else {
    Write-Host "ATTENZIONE: Potrebbe essere il primo commit" -ForegroundColor Yellow
    git commit -m "Initial commit - Tabluchka multiplication table trainer"
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Prossimi Passi" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "1. Vai su https://github.com" -ForegroundColor Cyan
Write-Host "2. Clicca 'New repository'" -ForegroundColor White
Write-Host "3. Nome: tabluchka (o qualsiasi nome)" -ForegroundColor White
Write-Host "4. Clicca 'Create repository'" -ForegroundColor White
Write-Host ""
Write-Host "Poi esegui questi comandi:" -ForegroundColor Cyan
Write-Host ""
Write-Host "  git remote add origin https://github.com/TUO_USERNAME/tabluchka.git" -ForegroundColor Yellow
Write-Host "  git branch -M main" -ForegroundColor Yellow
Write-Host "  git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "Sostituisci TUO_USERNAME con il tuo username GitHub!" -ForegroundColor White
Write-Host ""
Write-Host "Dopo il push:" -ForegroundColor Cyan
Write-Host "1. Vai su GitHub > Actions" -ForegroundColor White
Write-Host "2. Clicca 'Build Android APK'" -ForegroundColor White
Write-Host "3. Clicca 'Run workflow'" -ForegroundColor White
Write-Host "4. Aspetta la build (30-60 minuti)" -ForegroundColor White
Write-Host "5. Scarica l'APK da Artifacts" -ForegroundColor White
Write-Host ""

$username = Read-Host "Inserisci il tuo username GitHub (o premi INVIO per saltare)"
if ($username) {
    Write-Host ""
    Write-Host "Eseguo i comandi per te..." -ForegroundColor Cyan
    
    git remote remove origin -ErrorAction SilentlyContinue
    git remote add origin "https://github.com/$username/tabluchka.git"
    git branch -M main
    
    Write-Host ""
    Write-Host "Ora esegui:" -ForegroundColor Yellow
    Write-Host "  git push -u origin main" -ForegroundColor White
    Write-Host ""
    Write-Host "Ti chiedera username e password/token GitHub" -ForegroundColor Gray
}

Write-Host ""
Write-Host "Premi un tasto per uscire..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

