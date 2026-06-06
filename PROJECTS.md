# Projects Showcase

## 1. Repository Health Monitor
**[View on GitHub](./projects/repo-health-monitor/)**  
*Python/Bash • Monitoring • Automation*

### What it does
Automated tool that watches a repository for changes and produces detailed health reports, tracking:
- Total text files (skips binaries by extension/content check)
- Total lines in all text files  
- .git directory size vs working directory size
- Number of files changed since last scan
- Persistent baseline storage for delta reporting

### Why it matters
- **Monitoring Foundation**: Demonstrates understanding of system observability and health checking
- **Cross-Platform**: Works identically on Windows (Git-Bash) and Linux - no external dependencies
- **Data-Driven**: JSON output enables integration with alerting systems or dashboards
- **Self-Documenting**: Includes architecture docs and clear usage instructions

### Technical Highlights
- Pure stdlib Python + bash - zero third-party dependencies
- Smart file filtering (skips known binary extensions and checks for null bytes)
- Persistent state management via JSON config file
- Human-readable and machine-readable output modes
- Bash wrapper for automated report generation

### Key Learning
- Persistent state design for monitoring tools
- Cross-platform scripting considerations
- File I/O optimization and binary detection
- JSON data interchange for tool integration

## 2. Hermes Agent Skill Ecosystem
**[View Details](./docs/hermes-skills.md)**  
*AI Agent Configuration • Customization • Automation*

### What it is
Catalog and practical application of 113+ skills in the Hermes AI agent platform, organized by category:
- Autonomous AI agents (Claude Code, Codex, OpenCode)
- Creative generation (ASCII art, diagrams, music, video)
- DevOps & automation (kanban orchestration, webhooks)
- GitHub workflow management
- Local AI/MLOps (llama.cpp, HuggingFace, model segmentation)
- Knowledge management (Obsidian, Notion, Airtable)
- And many more specialized domains

### Why it matters
- **Platform Mastery**: Deep understanding of extensible AI agent systems
- **Modular Thinking**: Experience with plugin/skill-based architectures
- **Practical Automation**: Built real workflows integrating multiple systems
- **Knowledge Organization**: Created systems for capturing and retrieving information

### Technical Highlights
- Built Telegram↔Obsidian↔Git synchronization pipeline for knowledge vault
- Created distributed Windows/Kali inference lab for local LLM workloads
- Implemented API quota mitigation strategies (caching, batching, backoff)
- Customized Hermes Agent configuration and created specialized workflows
- Applied test-driven development and systematic debugging principles

### Key Learning
- AI agent orchestration and delegation patterns
- Plugin architecture and extension mechanisms
- Local-first AI principles and privacy-conscious design
- Integration patterns between disparate systems (Telegram, Obsidian, Git)

## 3. Distributed Inference Lab Blueprint
**[View Blueprint](./docs/system_blueprint.md)**  
*Architecture • Infrastructure • Security*

### What it is
Architecture documentation for a Windows/Kali distributed AI inference pipeline designed for:
- Local-first, private AI workloads
- Hardware-aware optimization (RTX 3050 laptop GPU)
- API quota conscious operation
- Secure, air-gapped deployment principles

### Why it matters
- **System Design**: Ability to architect complex distributed systems
- **Infrastructure Planning**: Experience with heterogeneous environment setup
- **Security Consciousness**: Focus on data protection and network isolation
- **Resource Optimization**: Understanding of hardware constraints and mitigation strategies

### Technical Highlights
- Hardware profile documentation (GPU, CPU, RAM, storage considerations)
- Software stack selection rationale (Ollama/llama.cpp vs alternatives)
- API quota mitigation: caching layers, request batching, exponential backoff
- Security principles: network segmentation, hardware contexts, minimal external dependencies
- Cross-platform compatibility considerations (Windows host, Kali guest/remote)

### Key Learning
- Distributed system design principles
- Local AI infrastructure tradeoffs and optimization strategies
- Security-conscious architecture for AI workloads
- Documentation as a tool for knowledge transfer and reproducibility

## 4. Career Assets & Business Plan
**[View in Vault Reference]**  
*Entrepreneurship • Positioning • Marketing*

### What it is
Business plan and career positioning documents from my Obsidian BrainVault (AI work/ folder):
- Applied AI Engineering Business Plan: Service offerings and pricing
- Impact-driven resume bullet optimizations
- Frameworks and operational catalogs for AI engineering work

### Why it matters
- **Entrepreneurial Thinking**: Experience positioning technical skills in market context
- **Value Articulation**: Ability to translate technical work into business value
- **Career Strategy**: Conscious planning around certification and skill development paths
- **Personal Knowledge Management**: Practice with effective information organization systems

### Key Learning
- Technical service packaging and pricing strategies
- Resume optimization for technical roles
- Framework thinking for repeatable service delivery
- Integration of personal knowledge systems with professional workflows

---

*All projects are actively maintained and updated. This portfolio demonstrates practical, hands-on experience building real systems rather than just theoretical knowledge.*