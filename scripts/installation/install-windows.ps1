# Script de Instalacao Organizada dos Agentes Cursor
# Para Windows - Nova estrutura organizada

Write-Host "Instalador Organizado de Agentes Cursor" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Cyan

# Encontrar o diretório do Cursor
$cursorPaths = @(
    "$env:APPDATA\Cursor\User\globalStorage\cursor.cursor\custom-modes",
    "$env:APPDATA\Cursor\globalStorage\cursor.cursor\custom-modes",
    "$env:LOCALAPPDATA\Cursor\User\globalStorage\cursor.cursor\custom-modes",
    "$env:USERPROFILE\.cursor\custom-modes"
)

$cursorDir = $null
foreach ($path in $cursorPaths) {
    if (Test-Path $path) {
        $cursorDir = $path
        break
    }
}

if (-not $cursorDir) {
    Write-Host "Diretorio do Cursor nao encontrado!" -ForegroundColor Red
    Write-Host "Diretorios verificados:" -ForegroundColor Yellow
    foreach ($path in $cursorPaths) {
        Write-Host "  - $path" -ForegroundColor Gray
    }
    Write-Host ""
    Write-Host "Solucao manual:" -ForegroundColor Yellow
    Write-Host "1. Abra o Cursor" -ForegroundColor White
    Write-Host "2. Va em Settings (Ctrl+,)" -ForegroundColor White
    Write-Host "3. Procure por 'Custom Modes' ou 'AI Settings'" -ForegroundColor White
    Write-Host "4. Copie manualmente os arquivos .json para a pasta de configuracao" -ForegroundColor White
    exit 1
}

Write-Host "Diretorio do Cursor encontrado: $cursorDir" -ForegroundColor Green

# Criar diretório se não existir
if (-not (Test-Path $cursorDir)) {
    New-Item -ItemType Directory -Path $cursorDir -Force | Out-Null
    Write-Host "Diretorio criado: $cursorDir" -ForegroundColor Yellow
}

# Copiar agentes especializados
$specializedDir = Join-Path (Get-Location) "agents\specialized"
$specializedFiles = Get-ChildItem -Path $specializedDir -Filter "*.json"

Write-Host "Copiando $($specializedFiles.Count) agentes especializados..." -ForegroundColor Yellow

$copiedCount = 0
foreach ($file in $specializedFiles) {
    $destPath = Join-Path $cursorDir $file.Name
    Copy-Item -Path $file.FullName -Destination $destPath -Force
    Write-Host "  $($file.Name)" -ForegroundColor Green
    $copiedCount++
}

# Copiar agentes inteligentes
$intelligentDir = Join-Path (Get-Location) "agents\intelligent"
$intelligentFiles = Get-ChildItem -Path $intelligentDir -Filter "*.json"

Write-Host "Copiando $($intelligentFiles.Count) agentes inteligentes..." -ForegroundColor Yellow

foreach ($file in $intelligentFiles) {
    $destPath = Join-Path $cursorDir $file.Name
    Copy-Item -Path $file.FullName -Destination $destPath -Force
    Write-Host "  $($file.Name)" -ForegroundColor Cyan
    $copiedCount++
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Instalacao concluida!" -ForegroundColor Green
Write-Host "Total de agentes instalados: $copiedCount" -ForegroundColor White
Write-Host "Localizacao: $cursorDir" -ForegroundColor White

Write-Host ""
Write-Host "Agentes Inteligentes Disponiveis:" -ForegroundColor Yellow
Write-Host "  /mode Smart Agent Selector" -ForegroundColor Cyan
Write-Host "  /mode AI Project Manager" -ForegroundColor Cyan

Write-Host ""
Write-Host "Como usar os agentes:" -ForegroundColor Yellow
Write-Host "1. Abra o Cursor" -ForegroundColor White
Write-Host "2. Pressione Ctrl+Shift+L (ou Cmd+Shift+L no Mac)" -ForegroundColor White
Write-Host "3. Digite: /mode [Nome do Agente]" -ForegroundColor White
Write-Host "4. Exemplo: /mode Smart Agent Selector" -ForegroundColor White

Write-Host ""
Write-Host "Exemplos de uso:" -ForegroundColor Yellow
Write-Host "  /mode Smart Agent Selector" -ForegroundColor White
Write-Host "  /mode AI Project Manager" -ForegroundColor White
Write-Host "  /mode Code Architect" -ForegroundColor White
Write-Host "  /mode Bug Hunter" -ForegroundColor White

Write-Host ""
Write-Host "Consulte a documentacao em docs/ para mais informacoes!" -ForegroundColor Cyan
