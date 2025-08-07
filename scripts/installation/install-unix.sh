#!/bin/bash

# Script de Instalacao dos Agentes Cursor
# Para Linux/macOS

echo "🚀 Instalador de Agentes Cursor"
echo "=================================================="

# Encontrar o diretório do Cursor
CURSOR_PATHS=(
    "$HOME/.config/Cursor/User/globalStorage/cursor.cursor/custom-modes"
    "$HOME/Library/Application Support/Cursor/User/globalStorage/cursor.cursor/custom-modes"
    "$HOME/.cursor/custom-modes"
)

CURSOR_DIR=""
for path in "${CURSOR_PATHS[@]}"; do
    if [ -d "$path" ]; then
        CURSOR_DIR="$path"
        break
    fi
done

if [ -z "$CURSOR_DIR" ]; then
    echo "❌ Diretório do Cursor não encontrado!"
    echo "📁 Diretórios verificados:"
    for path in "${CURSOR_PATHS[@]}"; do
        echo "  - $path"
    done
    echo ""
    echo "🔧 Solução manual:"
    echo "1. Abra o Cursor"
    echo "2. Vá em Settings (Cmd+,)"
    echo "3. Procure por 'Custom Modes' ou 'AI Settings'"
    echo "4. Copie manualmente os arquivos .json para a pasta de configuração"
    exit 1
fi

echo "✅ Diretório do Cursor encontrado: $CURSOR_DIR"

# Criar diretório se não existir
if [ ! -d "$CURSOR_DIR" ]; then
    mkdir -p "$CURSOR_DIR"
    echo "📁 Diretório criado: $CURSOR_DIR"
fi

# Obter diretório atual
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Copiar agentes especializados
SPECIALIZED_DIR="$PROJECT_DIR/agents/specialized"
echo "📋 Copiando agentes especializados..."

if [ -d "$SPECIALIZED_DIR" ]; then
    cp "$SPECIALIZED_DIR"/*.json "$CURSOR_DIR/"
    SPECIALIZED_COUNT=$(ls "$SPECIALIZED_DIR"/*.json 2>/dev/null | wc -l)
    echo "  ✅ $SPECIALIZED_COUNT agentes especializados copiados"
else
    echo "  ❌ Diretório de agentes especializados não encontrado"
fi

# Copiar agentes inteligentes
INTELLIGENT_DIR="$PROJECT_DIR/agents/intelligent"
echo "🧠 Copiando agentes inteligentes..."

if [ -d "$INTELLIGENT_DIR" ]; then
    cp "$INTELLIGENT_DIR"/*.json "$CURSOR_DIR/"
    INTELLIGENT_COUNT=$(ls "$INTELLIGENT_DIR"/*.json 2>/dev/null | wc -l)
    echo "  ✅ $INTELLIGENT_COUNT agentes inteligentes copiados"
else
    echo "  ❌ Diretório de agentes inteligentes não encontrado"
fi

# Calcular total
TOTAL_COUNT=$((SPECIALIZED_COUNT + INTELLIGENT_COUNT))

echo ""
echo "=================================================="
echo "✅ Instalação concluída!"
echo "📊 Total de agentes instalados: $TOTAL_COUNT"
echo "📁 Localização: $CURSOR_DIR"

echo ""
echo "🧠 Agentes Inteligentes Disponíveis:"
echo "  /mode Smart Agent Selector"
echo "  /mode AI Project Manager"

echo ""
echo "🎯 Como usar os agentes:"
echo "1. Abra o Cursor"
echo "2. Pressione Cmd+Shift+L (ou Ctrl+Shift+L no Linux)"
echo "3. Digite: /mode [Nome do Agente]"
echo "4. Exemplo: /mode Smart Agent Selector"

echo ""
echo "💡 Exemplos de uso:"
echo "  /mode Smart Agent Selector"
echo "  /mode AI Project Manager"
echo "  /mode Code Architect"
echo "  /mode Bug Hunter"

echo ""
echo "📚 Consulte a documentação em docs/ para mais informações!"
