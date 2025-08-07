# 🚀 Sistema de Agentes Inteligentes para Cursor

> **57 agentes customizados** para turbinar sua produtividade no desenvolvimento

## 📋 Visão Geral

Este repositório contém um sistema completo de agentes customizados para o Cursor IDE, incluindo **55 agentes especializados** baseados no artigo da OneDollarVPS e **2 agentes inteligentes** que podem escolher automaticamente o melhor especialista para cada tarefa.

## 🏗️ Estrutura do Repositório

```
cursor-agents/
├── 📄 README.md                    # Este arquivo
├── 📄 LICENSE                      # Licença MIT
├── 📄 .gitignore                   # Arquivos ignorados
├── 📁 agents/                      # Todos os agentes
│   ├── 📁 specialized/             # 55 agentes especializados
│   ├── 📁 intelligent/             # 2 agentes inteligentes
│   └── agents-index.json           # Índice completo
├── 📁 docs/                        # Documentação
│   └── agentes-inteligentes.md     # Guia dos agentes inteligentes
├── 📁 scripts/                     # Scripts organizados
│   └── 📁 installation/            # Scripts de instalação
└── 📁 templates/                   # Templates para novos agentes
    └── agent-template.json         # Template de agente
```

## 🧠 Agentes Inteligentes (Destaque)

### **Smart Agent Selector**
**Comando:** `/mode Smart Agent Selector`

Analisa sua tarefa e escolhe automaticamente o melhor especialista.

### **AI Project Manager**
**Comando:** `/mode AI Project Manager`

Gerencia projetos complexos coordenando múltiplos agentes.

## 🚀 Instalação Rápida

### **Opção 1: Script Automático (Recomendado)**
```bash
# Gerar agentes
python scripts/generation/generate-agents.py
python scripts/generation/improve-agents.py

# Instalar
python scripts/installation/install-unix.sh  # Linux/macOS
# ou
scripts/installation/install-windows.ps1     # Windows
```

### **Opção 2: Instalação Manual**
Copie todos os arquivos `.json` da pasta `agents/` para:
```
C:\Users\[SEU_USUARIO]\AppData\Roaming\Cursor\User\globalStorage\cursor.cursor\custom-modes\
```

## 🎯 Como Usar

### **Para Tarefas Simples (Recomendado):**
```
/mode Smart Agent Selector
"Descreva sua tarefa"
```

### **Para Projetos Complexos:**
```
/mode AI Project Manager
"Descreva seu projeto completo"
```

## 📋 Categorias de Agentes

### **🧠 Research & Analysis**
- Research Specialist, Technology Trend Analyst, Architecture Analyst, Performance Analyst, Code Quality Inspector

### **🏗️ Arquitetura & Design**
- Code Architect, Microservice Architect, Cloud Architect, etc.

### **🐛 Debugging & Qualidade**
- Bug Hunter, Code Reviewer, Technical Debt Reducer, etc.

### **⚡ Performance**
- Performance Optimizer, Load Testing Specialist

### **🔒 Segurança**
- Security Guardian, Authentication Specialist

### **🔧 Backend & APIs**
- API Designer, Database Specialist, API Integrator

### **🎨 Frontend & UI**
- Frontend Wizard, UI/UX Implementer, Accessibility Advocate

### **🧪 Testes**
- Test Engineer, Continuous Integration Expert

### **📱 Mobile & Plataformas**
- Mobile Developer, Desktop Application Developer

### **🤖 AI & Dados**
- Data Scientist, Data Engineer, Chatbot Developer

### **⚙️ DevOps & Infraestrutura**
- DevOps Engineer, Dependency Manager, Configuration Management Specialist

### **🔄 Migração & Modernização**
- Legacy Code Modernizer, Monolith to Microservice Transformer

### **⛓️ Tecnologias Emergentes**
- Blockchain Developer, IoT Developer, AR/VR Developer

## 🔧 Ferramentas MCP Integradas

Os agentes incluem ferramentas MCP específicas:

- **Context7** - Documentação atualizada de linguagens de programação
- **Paper Search** - Busca de artigos acadêmicos (arXiv, PubMed, etc.)
- **Docker** - Gerenciamento de containers
- **API Integration** - Execução de APIs externas
- **Web Search** - Pesquisa na web

## 📚 Documentação

- **[Agentes Inteligentes](docs/agentes-inteligentes.md)** - Como usar os agentes inteligentes

## 🔧 Scripts Disponíveis

### **Instalação**
- **[install-windows.ps1](scripts/installation/install-windows.ps1)** - Instalador PowerShell
- **[install-unix.sh](scripts/installation/install-unix.sh)** - Instalador Linux/macOS
- **[install-manual.bat](scripts/installation/install-manual.bat)** - Instalador manual

### **Geração**
- **[generate-agents.py](scripts/generation/generate-agents.py)** - Gerador de agentes
- **[improve-agents.py](scripts/generation/improve-agents.py)** - Melhorador de agentes
- **[apply-improvements.py](scripts/generation/apply-improvements.py)** - Aplicador de melhorias

## 🎉 Vantagens

- ✅ **57 agentes** especializados disponíveis
- ✅ **Seleção automática** de especialistas
- ✅ **Coordenação inteligente** de projetos
- ✅ **Expertise especializada** para cada domínio
- ✅ **Ferramentas MCP** integradas
- ✅ **Produtividade máxima** no desenvolvimento
- ✅ **Fácil instalação** e configuração

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Créditos

- Baseado no artigo [OneDollarVPS - 50 Cursor Custom Modes](https://onedollarvps.com/blogs/cursor-custom-mode-settings.html)
- Agentes inteligentes e especializados desenvolvidos especificamente para este projeto
- Integração com ferramentas MCP para funcionalidades avançadas

---

**🎯 Agora você pode focar na criatividade e deixar a IA escolher os melhores especialistas!** 🚀
