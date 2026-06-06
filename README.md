# AI Engineering Portfolio

**Johnnie Stallings** | Network Engineer → AI Systems Builder | Security Focused

[![Repo Health](https://img.shields.io/badge/repo-health-active-green)](https://github.com/johnnie-stallings/ai-engineering-portfolio/actions)
[![Last Scan](https://img.shields.io/badge/last--scan-real--time-blue)](REPO_HEALTH_REPORT.md)

## About

This portfolio showcases my journey from network engineering to AI infrastructure, with a focus on local-first, privacy-conscious AI systems and distributed computing. Built during my transition into cybersecurity, these projects demonstrate hands-on experience with:

- **Distributed AI Systems**: Windows/Kali inference pipelines
- **Local Agent Engineering**: Custom Hermes agent skills and automation
- **Repository Monitoring**: Automated health tracking and reporting
- **Air-Gapped Architecture**: Secure, offline AI workflows

## Projects

### [Repository Health Monitor](./projects/repo-health-monitor/)
A Python/bash tool that watches repositories for changes and produces detailed health reports. Features:
- Text file and line counting (skips binaries)
- Git size tracking vs working directory
- File change detection since last scan
- Persistent baseline storage in JSON
- Cross-platform (Windows/git-bash + Linux)
- Zero external dependencies

### [Hermes Agent Skill Ecosystem](./docs/hermes-skills.md)
Custom-built skills for the Hermes AI agent platform covering:
- Autonomous AI agent orchestration (Claude Code, Codex, OpenCode)
- Creative generation (ASCII art, diagrams, music, video)
- DevOps automation and monitoring
- Cybersecurity and red-teaming tools
- Local LLM optimization and inference
- Smart home and media processing
- **113+ skills total** - modular, reusable AI capabilities

### [Distributed Inference Lab Blueprint](./docs/system_blueprint.md)
Architecture documentation for a Windows/Kali distributed AI inference pipeline:
- Hardware profile: RTX 3050 laptop GPU
- API quota mitigation strategies (caching, batching, backoff)
- Cross-platform model serving (Ollama, llama.cpp)
- Secure, air-gapped operation principles

## Skills

### Technical
- **Languages**: Python, Bash, JSON, YAML, Markdown
- **Systems**: Linux (Kali), Windows 10, Git-Bash/MSYS
- **Tools**: Git, GitHub CLI, Docker concepts, Ollama, llama.cpp
- **Concepts**: Distributed systems, API integration, local LLMs, agent frameworks
- **Monitoring**: Health checks, metrics collection, alerting foundations

### Career Focus
- Network Engineering fundamentals (TCP/IP, subnetting, common ports)
- Cybersecurity trajectory (Network+ → Security+ → CySA+/Pentest+)
- AI Infrastructure/MLOps (local-first approach)
- Automation and scripting

## Experience

### Self-Directed AI Systems Engineer
*Hermes Agent Ecosystem* | Ongoing
- Architected and expanded a modular AI agent system with 113+ skills
- Built Telegram↔Obsidian↔Git synchronization pipeline
- Created distributed Windows/Kali inference lab for local LLM workloads
- Implemented API quota mitigation and caching strategies
- Developed repository health monitoring tool

### Network Engineering Foundation
*In Progress* | LA Area
- Pursuing CompTIA Network+ certification
- Hands-on practice with Wireshark, basic networking concepts
- Building toward cybersecurity specialization

## Getting Started

### Repository Health Monitor
```bash
# Clone this repository
git clone https://github.com/johnnie-stallings/ai-engineering-portfolio.git
cd ai-engineering-portfolio/projects/repo-health-monitor

# Run the health monitor
python monitor.py          # Human-readable output
python monitor.py --json   # JSON output for automation
./health_check.sh          # Bash wrapper that writes to REPO_HEALTH_REPORT.md
```

### View Current Health Report
See the latest scan results: [REPO_HEALTH_REPORT.md](./REPO_HEALTH_REPORT.md)

## Philosophy

**Local-First, Privacy-Conscious AI**
- Preference for open-weights models running on local hardware
- Air-gapped architectures for proprietary data protection
- Minimal reliance on external APIs/services
- Focus on understanding and controlling the entire stack

**Networking-First Security Entry**
- Strong foundation in networking as pathway to cybersecurity
- Monitoring and observability as first line of defense
- Understanding normal behavior to detect anomalies
- Infrastructure as code and automation mindsets

## Contact

- **LinkedIn**: [linkedin.com/in/johnniestallings](https://linkedin.com/in/johnniestallings)
- **Email**: johnnie.stallings@email.com (consider ProtonMail/Tutanota for security focus)
- **GitHub**: [github.com/johnnie-stallings](https://github.com/johnnie-stallings)

## License

MIT © 2026 Johnnie Stallings

---

*Last updated: June 2026 | This portfolio is actively maintained and updated*