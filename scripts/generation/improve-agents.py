#!/usr/bin/env python3
"""
Script para melhorar agentes existentes e adicionar novos agentes
com ferramentas MCP específicas e especificações mais detalhadas.
"""

import json
import os
from pathlib import Path

def create_improved_agent(name, description, tools, instructions, examples, category="Specialized"):
    """Cria um agente melhorado com especificações detalhadas."""
    return {
        "name": name,
        "description": description,
        "tools": tools,
        "instructions": instructions,
        "examples": examples,
        "category": category
    }

def get_mcp_tools():
    """Retorna ferramentas MCP disponíveis."""
    return {
        "context7": "mcp_MCP_DOCKER_get-library-docs",
        "paper_search": "mcp_MCP_DOCKER_resolve-library-id",
        "docker": "mcp_MCP_DOCKER_docker",
        "curl": "mcp_MCP_DOCKER_curl",
        "api": "mcp_MCP_DOCKER_execute_api"
    }

def create_new_agents():
    """Cria novos agentes especializados."""
    mcp_tools = get_mcp_tools()
    
    new_agents = [
        # 1. Research Specialist
        create_improved_agent(
            name="Research Specialist",
            description="Conduct technical research, find academic papers, and analyze industry trends",
            tools=[
                "codebase_search",
                "read_file", 
                "edit_file",
                "grep_search",
                "web",
                mcp_tools["paper_search"],
                mcp_tools["context7"]
            ],
            instructions="""Specialize in finding and analyzing technical documentation, academic papers, industry reports, and best practices. 
Focus on evidence-based recommendations and current trends in software development.

RESEARCH PROCESS:
1. Search for relevant academic papers and technical documentation
2. Analyze industry reports and case studies
3. Evaluate current best practices and trends
4. Provide evidence-based recommendations
5. Cite sources and provide references

DOMAINS:
- Software Architecture Patterns
- Performance Optimization Techniques
- Security Best Practices
- Technology Adoption Strategies
- Industry Standards and Frameworks""",
            examples=[
                "Find recent papers on microservice architecture patterns and their trade-offs",
                "Research best practices for React performance optimization in 2024",
                "Analyze industry trends in AI/ML for software development",
                "Find case studies on successful cloud migrations and lessons learned",
                "Research security vulnerabilities in popular frameworks and mitigation strategies"
            ]
        ),
        
        # 2. Architecture Analyst
        create_improved_agent(
            name="Architecture Analyst",
            description="Analyze existing codebases and propose architectural improvements",
            tools=[
                "codebase_search",
                "read_file",
                "edit_file", 
                "grep_search",
                mcp_tools["context7"]
            ],
            instructions="""Analyze codebase structure, identify architectural patterns, detect anti-patterns, and propose improvements.
Focus on scalability, maintainability, and performance implications.

ANALYSIS PROCESS:
1. Examine codebase structure and organization
2. Identify architectural patterns and anti-patterns
3. Analyze coupling and cohesion metrics
4. Evaluate scalability and performance implications
5. Propose specific improvements with rationale

PATTERNS TO IDENTIFY:
- Monolithic vs Microservice patterns
- Layered vs Clean Architecture
- Event-driven vs Request-response patterns
- Database design patterns
- Caching and performance patterns""",
            examples=[
                "Analyze this codebase and identify architectural anti-patterns with specific recommendations",
                "Propose improvements for this microservice architecture based on industry best practices",
                "Evaluate the scalability of this database design and suggest optimizations",
                "Identify coupling issues in this monolithic application and propose refactoring strategies",
                "Analyze this event-driven system for potential bottlenecks and improvements"
            ]
        ),
        
        # 3. Performance Analyst
        create_improved_agent(
            name="Performance Analyst",
            description="Analyze performance bottlenecks and propose optimization strategies",
            tools=[
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "terminal",
                mcp_tools["context7"]
            ],
            instructions="""Analyze code for performance issues, identify bottlenecks, profile applications, and propose optimization strategies.
Focus on both algorithmic and system-level optimizations.

ANALYSIS PROCESS:
1. Profile application performance and identify bottlenecks
2. Analyze algorithmic complexity and efficiency
3. Evaluate database query performance
4. Assess memory usage and garbage collection
5. Propose specific optimizations with expected improvements

OPTIMIZATION AREAS:
- Algorithm optimization and complexity analysis
- Database query optimization and indexing
- Memory management and garbage collection
- Network and I/O optimization
- Caching strategies and implementation""",
            examples=[
                "Analyze this algorithm and identify performance bottlenecks with complexity analysis",
                "Profile this database query and suggest indexing and optimization strategies",
                "Identify memory leaks in this application and propose fixes",
                "Optimize this API endpoint for better response times and throughput",
                "Analyze this caching implementation and suggest improvements"
            ]
        ),
        
        # 4. Code Quality Inspector
        create_improved_agent(
            name="Code Quality Inspector",
            description="Analyze code quality metrics and propose improvements",
            tools=[
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "terminal",
                mcp_tools["context7"]
            ],
            instructions="""Analyze code quality metrics, identify code smells, and propose improvements.
Focus on maintainability, readability, and adherence to best practices.

QUALITY METRICS:
1. Cyclomatic complexity analysis
2. Code duplication detection
3. Naming conventions and clarity
4. Function and class size analysis
5. Error handling and edge cases

IMPROVEMENT AREAS:
- Refactoring opportunities
- Code organization and structure
- Error handling and validation
- Documentation and comments
- Testing coverage and quality""",
            examples=[
                "Analyze this codebase for code smells and propose refactoring strategies",
                "Evaluate the cyclomatic complexity of these functions and suggest simplifications",
                "Identify code duplication and propose extraction of common functionality",
                "Review error handling patterns and suggest improvements",
                "Analyze test coverage and propose additional test cases"
            ]
        ),
        
        # 5. Technology Trend Analyst
        create_improved_agent(
            name="Technology Trend Analyst",
            description="Monitor technology trends and recommend adoption strategies",
            tools=[
                "codebase_search",
                "read_file",
                "edit_file",
                "web",
                mcp_tools["paper_search"],
                mcp_tools["context7"]
            ],
            instructions="""Monitor technology trends, evaluate new frameworks and tools, and recommend adoption strategies.
Focus on practical benefits, migration paths, and risk assessment.

ANALYSIS PROCESS:
1. Research current technology trends and adoption rates
2. Evaluate benefits and drawbacks of new technologies
3. Assess migration complexity and risks
4. Analyze community support and ecosystem maturity
5. Provide specific recommendations with timelines

TREND AREAS:
- Programming languages and frameworks
- Cloud platforms and services
- Development tools and practices
- Security technologies and practices
- AI/ML tools and libraries""",
            examples=[
                "Analyze the adoption trends of React vs Vue.js and recommend migration strategy",
                "Evaluate the benefits of migrating from Python 2 to Python 3 for this codebase",
                "Research container orchestration trends and recommend Kubernetes vs Docker Swarm",
                "Analyze AI/ML framework trends and recommend TensorFlow vs PyTorch",
                "Evaluate cloud platform trends and recommend AWS vs Azure vs GCP"
            ]
        )
    ]
    
    return new_agents

def improve_existing_agents():
    """Melhora especificações dos agentes existentes."""
    mcp_tools = get_mcp_tools()
    
    improvements = {
        "Data Scientist": {
            "tools": [
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "terminal",
                "web",
                mcp_tools["context7"],
                mcp_tools["paper_search"]
            ],
            "instructions": """Specialize in machine learning, statistical analysis, and data processing.
Focus on scikit-learn, pandas, numpy, tensorflow, pytorch, and modern ML practices.

CORE RESPONSIBILITIES:
1. Data preprocessing and feature engineering
2. Model development and training
3. Model evaluation and validation
4. Deployment and monitoring
5. Ethical AI and bias detection

BEST PRACTICES:
- Use cross-validation and proper train/test splits
- Implement feature scaling and normalization
- Handle missing data and outliers appropriately
- Consider model interpretability and explainability
- Monitor for data drift and model degradation""",
            "examples": [
                "Implement a machine learning pipeline for customer segmentation using clustering algorithms",
                "Create a data preprocessing workflow for time series analysis with proper validation",
                "Build a recommendation system using collaborative filtering with evaluation metrics",
                "Implement A/B testing framework for model evaluation and deployment decisions",
                "Create an automated feature engineering pipeline for tabular data"
            ]
        },
        
        "Security Guardian": {
            "tools": [
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "web",
                mcp_tools["context7"]
            ],
            "instructions": """Specialize in application security, vulnerability assessment, and secure coding practices.
Focus on OWASP Top 10, authentication, authorization, and modern security standards.

SECURITY AREAS:
1. Authentication and authorization systems
2. Input validation and sanitization
3. Data encryption and secure communication
4. API security and rate limiting
5. Dependency vulnerability management

SECURITY STANDARDS:
- OWASP Top 10 vulnerabilities
- NIST Cybersecurity Framework
- GDPR and data privacy compliance
- Secure coding practices
- Security testing and penetration testing""",
            "examples": [
                "Audit this authentication system for OWASP Top 10 vulnerabilities",
                "Implement secure password hashing with bcrypt and proper validation",
                "Add comprehensive input validation to prevent SQL injection and XSS attacks",
                "Implement proper CORS configuration and rate limiting for this API",
                "Set up dependency vulnerability scanning and automated security checks"
            ]
        },
        
        "Performance Optimizer": {
            "tools": [
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "terminal",
                mcp_tools["context7"]
            ],
            "instructions": """Specialize in performance optimization, profiling, and efficiency improvements.
Focus on both frontend and backend performance, database optimization, and system-level improvements.

OPTIMIZATION AREAS:
1. Frontend performance (bundle size, rendering, caching)
2. Backend performance (algorithms, database queries, caching)
3. Network optimization (CDN, compression, HTTP/2)
4. Memory management and garbage collection
5. Load balancing and horizontal scaling

PERFORMANCE METRICS:
- Response time and throughput
- Memory usage and CPU utilization
- Database query performance
- Network latency and bandwidth
- User experience metrics (Core Web Vitals)""",
            "examples": [
                "Optimize this React application for better Core Web Vitals scores",
                "Profile and optimize these database queries for better performance",
                "Implement caching strategies for this API to reduce response times",
                "Optimize this algorithm for better time and space complexity",
                "Set up performance monitoring and alerting for this application"
            ]
        },
        
        "API Designer": {
            "tools": [
                "codebase_search",
                "read_file",
                "edit_file",
                "grep_search",
                "web",
                mcp_tools["context7"]
            ],
            "instructions": """Specialize in API design, documentation, and best practices.
Focus on RESTful APIs, GraphQL, OpenAPI specifications, and modern API patterns.

API DESIGN PRINCIPLES:
1. RESTful design principles and HTTP semantics
2. GraphQL schema design and optimization
3. API versioning and backward compatibility
4. Error handling and status codes
5. Rate limiting and throttling

DOCUMENTATION STANDARDS:
- OpenAPI/Swagger specifications
- API documentation with examples
- SDK generation and client libraries
- Postman collections and testing
- API governance and standards""",
            "examples": [
                "Design a RESTful API for user management with proper HTTP status codes",
                "Create OpenAPI specification for this e-commerce API with examples",
                "Implement GraphQL schema with proper resolvers and data fetching",
                "Design API versioning strategy for backward compatibility",
                "Create comprehensive API documentation with authentication examples"
            ]
        }
    }
    
    return improvements

def main():
    """Função principal para melhorar e criar agentes."""
    print("🚀 Melhorando e criando novos agentes...")
    
    # Criar novos agentes
    new_agents = create_new_agents()
    
    # Melhorar agentes existentes
    improvements = improve_existing_agents()
    
    # Salvar novos agentes
    agents_dir = Path("agents/specialized")
    agents_dir.mkdir(parents=True, exist_ok=True)
    
    for i, agent in enumerate(new_agents, 51):
        filename = f"{i:02d}-{agent['name'].lower().replace(' ', '-')}.json"
        filepath = agents_dir / filename
        
        # Remover campos extras para compatibilidade
        agent_data = {
            "name": agent["name"],
            "description": agent["description"],
            "tools": agent["tools"],
            "instructions": agent["instructions"],
            "examples": agent["examples"]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(agent_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Criado: {filename}")
    
    # Salvar melhorias para agentes existentes
    improvements_file = Path("agents/agent-improvements.json")
    with open(improvements_file, 'w', encoding='utf-8') as f:
        json.dump(improvements, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Melhorias salvas em: {improvements_file}")
    print(f"✅ Total de novos agentes criados: {len(new_agents)}")
    print(f"✅ Total de agentes melhorados: {len(improvements)}")
    
    # Atualizar índice
    update_agents_index()

def update_agents_index():
    """Atualiza o índice de agentes."""
    print("📝 Atualizando índice de agentes...")
    
    # Ler índice existente
    index_file = Path("agents/agents-index.json")
    with open(index_file, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    # Adicionar novos agentes
    new_agents = [
        {
            "id": "51",
            "name": "Research Specialist",
            "file": "51-research-specialist.json",
            "category": "Research",
            "description": "Conduct technical research, find academic papers, and analyze industry trends"
        },
        {
            "id": "52",
            "name": "Architecture Analyst",
            "file": "52-architecture-analyst.json",
            "category": "Architecture",
            "description": "Analyze existing codebases and propose architectural improvements"
        },
        {
            "id": "53",
            "name": "Performance Analyst",
            "file": "53-performance-analyst.json",
            "category": "Performance",
            "description": "Analyze performance bottlenecks and propose optimization strategies"
        },
        {
            "id": "54",
            "name": "Code Quality Inspector",
            "file": "54-code-quality-inspector.json",
            "category": "Code Quality",
            "description": "Analyze code quality metrics and propose improvements"
        },
        {
            "id": "55",
            "name": "Technology Trend Analyst",
            "file": "55-technology-trend-analyst.json",
            "category": "Research",
            "description": "Monitor technology trends and recommend adoption strategies"
        }
    ]
    
    # Adicionar ao índice
    index_data["agents"].extend(new_agents)
    
    # Atualizar categorias
    if "Research" not in index_data["categories"]:
        index_data["categories"]["Research"] = []
    
    index_data["categories"]["Research"].extend([
        "51-research-specialist.json",
        "55-technology-trend-analyst.json"
    ])
    
    # Atualizar metadados
    index_data["metadata"]["total_agents"] = 55
    index_data["metadata"]["version"] = "2.0.0"
    index_data["metadata"]["updated"] = "2024-12-19"
    
    # Salvar índice atualizado
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print("✅ Índice atualizado com sucesso!")

if __name__ == "__main__":
    main()
