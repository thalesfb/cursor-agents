#!/usr/bin/env python3
"""
Script para aplicar melhorias aos agentes existentes.
"""

import json
import os
from pathlib import Path

def apply_improvements():
    """Aplica melhorias aos agentes existentes."""
    print("🔧 Aplicando melhorias aos agentes existentes...")
    
    # Carregar melhorias
    improvements_file = Path("agents/agent-improvements.json")
    with open(improvements_file, 'r', encoding='utf-8') as f:
        improvements = json.load(f)
    
    # Aplicar melhorias
    agents_dir = Path("agents/specialized")
    updated_count = 0
    
    for agent_name, improvement in improvements.items():
        # Encontrar arquivo do agente
        agent_files = list(agents_dir.glob(f"*{agent_name.lower().replace(' ', '-')}*.json"))
        
        if not agent_files:
            print(f"⚠️  Arquivo não encontrado para: {agent_name}")
            continue
        
        agent_file = agent_files[0]
        
        # Carregar agente atual
        with open(agent_file, 'r', encoding='utf-8') as f:
            agent_data = json.load(f)
        
        # Aplicar melhorias
        agent_data["tools"] = improvement["tools"]
        agent_data["instructions"] = improvement["instructions"]
        agent_data["examples"] = improvement["examples"]
        
        # Salvar agente melhorado
        with open(agent_file, 'w', encoding='utf-8') as f:
            json.dump(agent_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Melhorado: {agent_file.name}")
        updated_count += 1
    
    print(f"✅ Total de agentes atualizados: {updated_count}")
    
    # Remover arquivo de melhorias
    improvements_file.unlink()
    print("✅ Arquivo de melhorias removido")

def main():
    """Função principal."""
    apply_improvements()

if __name__ == "__main__":
    main()
