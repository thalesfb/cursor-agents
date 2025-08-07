@echo off
echo ==================================================
echo Instalador Manual de Agentes Cursor
echo ==================================================

REM Criar diretório do Cursor se não existir
set CURSOR_DIR=%APPDATA%\Cursor\User\globalStorage\cursor.cursor\custom-modes

echo Criando diretorio: %CURSOR_DIR%
if not exist "%CURSOR_DIR%" mkdir "%CURSOR_DIR%"

REM Copiar todos os arquivos JSON (exceto agents-index.json)
echo.
echo Copiando agentes...
for %%f in (*.json) do (
    if not "%%f"=="agents-index.json" (
        copy "%%f" "%CURSOR_DIR%\"
        echo   Copiado: %%f
    )
)

echo.
echo ==================================================
echo Instalacao concluida!
echo.
echo Para usar os agentes:
echo 1. Abra o Cursor
echo 2. Pressione Ctrl+Shift+L
echo 3. Digite: /mode [Nome do Agente]
echo 4. Exemplo: /mode Code Architect
echo.
echo Exemplos:
echo   /mode Bug Hunter
echo   /mode Performance Optimizer
echo   /mode Security Guardian
echo   /mode Frontend Wizard
echo ==================================================
pause
