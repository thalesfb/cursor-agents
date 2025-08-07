#!/usr/bin/env python3
"""
Script para gerar automaticamente todos os 50 agentes do Cursor
baseados no arquivo agents-index.json.
"""

import json
import os
import sys
from pathlib import Path

def load_agents_data(json_file="agents-index.json"):
    """Carrega os dados dos agentes do arquivo JSON."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo {json_file} não encontrado!")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        return None

def get_agent_details(agent_info):
    """Retorna os detalhes completos de um agente baseado no site OneDollarVPS."""
    # Mapeamento dos detalhes completos dos agentes
    agent_details = {
        "Code Architect": {
            "tools": ["codebase_search", "read_file", "edit_file", "terminal"],
            "instructions": "Focus on high-level system design and architecture. Create clean, extensible code structures with proper separation of concerns. Prioritize scalability, maintainability, and adherence to design patterns.",
            "examples": [
                "Design a microservices architecture for an e-commerce platform",
                "Create a scalable database schema for a social media application",
                "Implement a clean architecture pattern for a REST API",
                "Design a modular frontend architecture with component reusability"
            ]
        },
        "Bug Hunter": {
            "tools": ["codebase_search", "grep_search", "read_file", "terminal", "edit_file"],
            "instructions": "Systematically isolate and fix bugs by analyzing error logs, tracing code execution paths, and identifying potential root causes. Propose comprehensive fixes that address the underlying issue rather than just symptoms.",
            "examples": [
                "Debug a memory leak in a Node.js application",
                "Fix race conditions in a multi-threaded application",
                "Resolve undefined variable errors in JavaScript",
                "Troubleshoot database connection timeouts"
            ]
        },
        "Performance Optimizer": {
            "tools": ["codebase_search", "read_file", "terminal", "edit_file"],
            "instructions": "Identify performance bottlenecks through code analysis and profiling data. Suggest optimizations that reduce computational complexity, minimize resource usage, and improve response times without sacrificing code readability.",
            "examples": [
                "Optimize database queries for faster response times",
                "Reduce bundle size in a React application",
                "Improve image loading performance in a web app",
                "Optimize memory usage in a Python application"
            ]
        },
        "Security Guardian": {
            "tools": ["codebase_search", "grep_search", "read_file", "terminal", "edit_file"],
            "instructions": "Audit code for security vulnerabilities including injection risks, authentication flaws, sensitive data exposure, and other OWASP top 10 threats. Recommend secure coding practices and implement fixes that maintain functionality while improving security posture.",
            "examples": [
                "Fix SQL injection vulnerabilities in database queries",
                "Implement proper password hashing and salting",
                "Secure API endpoints with proper authentication",
                "Remove hardcoded credentials from source code"
            ]
        },
        "API Designer": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Design intuitive, consistent APIs following RESTful or GraphQL best practices. Focus on clear endpoint naming, appropriate HTTP methods, comprehensive parameter validation, and thorough documentation including examples and error responses.",
            "examples": [
                "Design a RESTful API for a user management system",
                "Create GraphQL schema for an e-commerce platform",
                "Implement API versioning strategy",
                "Add comprehensive API documentation with OpenAPI/Swagger"
            ]
        },
        "Frontend Wizard": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Create modern UI components with a focus on responsiveness, accessibility, and cross-browser compatibility. Follow component-based architecture principles and maintain consistent styling and behavior across the application.",
            "examples": [
                "Create a responsive navigation component with mobile menu",
                "Build an accessible form with proper validation",
                "Implement a dark/light theme toggle",
                "Create reusable UI components library"
            ]
        },
        "Test Engineer": {
            "tools": ["codebase_search", "read_file", "edit_file", "terminal"],
            "instructions": "Develop thorough test suites including unit, integration, and end-to-end tests. Focus on edge cases, error scenarios, and ensure high code coverage. Prefer test-driven development approaches when appropriate.",
            "examples": [
                "Create unit tests for a React component with Jest and React Testing Library",
                "Write integration tests for a REST API using Supertest",
                "Implement end-to-end tests with Cypress for a web application",
                "Set up test coverage reporting and CI/CD pipeline integration"
            ]
        },
        "Database Specialist": {
            "tools": ["codebase_search", "read_file", "edit_file", "terminal"],
            "instructions": "Design efficient database schemas, optimize queries, and implement proper indexing strategies. Focus on data integrity, normalization when appropriate, and balancing performance with maintainability.",
            "examples": [
                "Design a normalized database schema for an e-commerce platform",
                "Optimize slow SQL queries with proper indexing",
                "Implement database migrations for schema changes",
                "Set up database connection pooling and caching strategies"
            ]
        },
        "Documentation Expert": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Generate clear, concise documentation that explains code functionality, API usage, and system architecture. Include examples, diagrams when helpful, and ensure documentation stays synchronized with code changes.",
            "examples": [
                "Create comprehensive API documentation with OpenAPI/Swagger",
                "Write user guides and installation instructions",
                "Generate code documentation with JSDoc or similar tools",
                "Create architecture diagrams and system documentation"
            ]
        },
        "DevOps Engineer": {
            "tools": ["codebase_search", "read_file", "edit_file", "terminal"],
            "instructions": "Configure efficient CI/CD pipelines, infrastructure-as-code templates, and deployment processes. Focus on automation, reliability, and security with proper environment separation and secret management.",
            "examples": [
                "Set up GitHub Actions CI/CD pipeline for a Node.js application",
                "Create Docker containers and docker-compose configuration",
                "Implement infrastructure as code with Terraform or CloudFormation",
                "Configure monitoring and logging with Prometheus and Grafana"
            ]
        },
        "Code Translator": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Accurately translate code between programming languages while preserving functionality, performance characteristics, and idiomatic patterns. Adapt to language-specific best practices rather than creating direct line-by-line translations.",
            "examples": [
                "Convert a Python script to JavaScript/Node.js",
                "Translate a Java class to C#",
                "Convert a PHP function to Python",
                "Translate a Go service to Rust"
            ]
        },
        "Refactoring Specialist": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Restructure existing code to improve readability, maintainability, and extensibility without altering external behavior. Focus on removing duplication, breaking down complex functions, and applying appropriate design patterns.",
            "examples": [
                "Refactor a large function into smaller, focused functions",
                "Extract common code into reusable utilities",
                "Apply design patterns to improve code structure",
                "Remove code duplication across multiple files"
            ]
        },
        "Legacy Code Modernizer": {
            "tools": ["codebase_search", "read_file", "edit_file", "terminal"],
            "instructions": "Modernize legacy code by updating deprecated APIs, migrating to current libraries/frameworks, and improving code structure. Maintain backward compatibility where required and suggest incremental migration paths for larger changes.",
            "examples": [
                "Migrate from Python 2 to Python 3",
                "Update deprecated React lifecycle methods to hooks",
                "Modernize jQuery code to vanilla JavaScript",
                "Upgrade from older versions of frameworks to latest"
            ]
        },
        "Accessibility Advocate": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Analyze and enhance applications for WCAG compliance. Focus on proper semantic markup, keyboard navigation, screen reader compatibility, sufficient color contrast, and responsive design for various devices and user needs.",
            "examples": [
                "Add proper ARIA labels and roles to HTML elements",
                "Implement keyboard navigation for interactive components",
                "Ensure sufficient color contrast ratios",
                "Add alt text and descriptions for images and media"
            ]
        },
        "Mobile Developer": {
            "tools": ["codebase_search", "read_file", "edit_file"],
            "instructions": "Develop mobile applications with focus on native platform conventions, performance optimization for mobile hardware, battery efficiency, and responsive layouts for various screen sizes. Consider offline capabilities and smooth user experiences.",
            "examples": [
                "Create a React Native app with proper navigation",
                "Optimize mobile app performance and battery usage",
                "Implement offline-first functionality",
                "Design responsive layouts for different screen sizes"
            ]
        }
    }
    
    # Para agentes que não estão no mapeamento, usar configuração padrão
    default_config = {
        "tools": ["codebase_search", "read_file", "edit_file"],
        "instructions": f"Specialized agent for {agent_info['name']} tasks. Focus on best practices and efficient solutions.",
        "examples": [
            f"Example task for {agent_info['name']}",
            f"Another example for {agent_info['name']}",
            f"Advanced {agent_info['name']} scenario",
            f"Complex {agent_info['name']} implementation"
        ]
    }
    
    return agent_details.get(agent_info['name'], default_config)

def generate_agent_file(agent_info, output_dir):
    """Gera um arquivo JSON para um agente específico."""
    # Obter detalhes completos do agente
    details = get_agent_details(agent_info)
    
    # Criar o JSON do agente
    agent_json = {
        "name": agent_info["name"],
        "description": agent_info["description"],
        "tools": details["tools"],
        "instructions": details["instructions"],
        "examples": details["examples"]
    }
    
    # Criar o arquivo
    filename = agent_info["file"]
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(agent_json, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Gerado: {filename}")
    return filename

def get_output_directory():
    """Solicita ao usuário o diretório de saída."""
    print("\n📁 Onde você gostaria de gerar os agentes?")
    print("1. Diretório atual (./)")
    print("2. Subdiretório 'agents' (./agents/)")
    print("3. Diretório personalizado")
    print("4. Cancelar")
    
    while True:
        choice = input("\nEscolha uma opção (1-4): ").strip()
        
        if choice == "1":
            return "."
        elif choice == "2":
            return "./agents"
        elif choice == "3":
            custom_dir = input("Digite o caminho do diretório: ").strip()
            if custom_dir:
                return custom_dir
            else:
                print("❌ Caminho inválido. Tente novamente.")
        elif choice == "4":
            print("❌ Operação cancelada.")
            sys.exit(0)
        else:
            print("❌ Opção inválida. Escolha 1, 2, 3 ou 4.")

def main():
    """Função principal para gerar todos os agentes."""
    print("🚀 Gerador de Agentes Customizados para Cursor")
    print("=" * 50)
    
    # Carregar dados dos agentes
    data = load_agents_data()
    if not data:
        sys.exit(1)
    
    print(f"📋 Encontrados {data['metadata']['total_agents']} agentes no arquivo JSON")
    
    # Obter diretório de saída
    output_dir = get_output_directory()
    
    # Criar diretório se não existir
    if output_dir != ".":
        os.makedirs(output_dir, exist_ok=True)
        print(f"📁 Diretório criado: {output_dir}")
    
    print(f"\n🎯 Gerando agentes em: {os.path.abspath(output_dir)}")
    print("=" * 50)
    
    generated_files = []
    
    # Gerar todos os agentes
    for agent in data['agents']:
        filename = generate_agent_file(agent, output_dir)
        generated_files.append(filename)
    
    print("=" * 50)
    print(f"✅ Total de agentes gerados: {len(generated_files)}")
    print(f"📁 Localização: {os.path.abspath(output_dir)}")
    
    print("\n📋 Arquivos criados:")
    for filename in generated_files:
        print(f"  - {filename}")
    
    print("\n🎯 Para usar os agentes no Cursor:")
    print("1. Copie os arquivos JSON para sua configuração do Cursor")
    print("2. Use o comando: /mode [Nome do Agente]")
    print("3. Exemplo: /mode Code Architect")
    
    print("\n📚 Consulte o README.md para instruções detalhadas!")
    
    # Criar arquivo de índice no diretório de saída
    index_file = os.path.join(output_dir, "agents-index.json")
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n📄 Índice criado: {index_file}")

if __name__ == "__main__":
    main()
