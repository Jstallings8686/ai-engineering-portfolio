# Hermes Skills Inventory

This document catalogs the 113+ skills I've worked with in the Hermes Agent ecosystem, organized by category. These skills represent practical, hands-on experience with AI agent orchestration, automation, and specialized tooling.

## Skill Categories Overview

Based on the Hermes skill directory structure, here are the main categories:

- **autonomous-ai-agents**: Claude Code, Codex, OpenCode, Hermes agent configuration
- **creative**: ASCII art, diagrams, comics, infographics, design, music generation
- **data-science**: Jupyter kernels, data analysis
- **devops**: Kanban orchestration, workers, Opencode smoke tests, webhooks
- **github**: Repository management, PR workflows, issues, code review
- **mcp**: Model Context Protocol integration
- **media**: GIF search, Spotify, YouTube processing, audio visualization
- **mlops**: HuggingFace, model evaluation, inference (llama.cpp), segmentation (SAM)
- **note-taking**: Obsidian vault management
- **productivity**: Airtable, Google Workspace, Linear, Notion, OCR, PDF editing
- **research**: arXiv, blog watching, LLM wiki, OSINT, Polymarket
- **software-development**: Planning, debugging, testing, code review, memory pipelines
- **yuanbao**: Group chat functionality

## Selected Skills by Category

### Autonomous AI Agents
- **claude-code**: Delegate coding tasks to Claude Code CLI for features and PRs
- **codex**: Delegate coding to OpenAI Codex CLI 
- **hermes-agent**: Configure, extend, or contribute to Hermes Agent itself
- **kanban-codex-lane**: Use when a Hermes Kanban worker wants to run Codex CLI
- **opencode**: Delegate coding to OpenCode CLI with PR review capabilities

### Creative Generation
- **architecture-diagram**: Dark-themed SVG architecture/cloud/infra diagrams as HTML
- **ascii-art**: ASCII art generation using pyfiglet, cowsay, boxes, image-to-ascii
- **ascii-video**: Convert video/audio to colored ASCII MP4/GIF
- **baoyu-infographic**: 21 layouts × 21 styles for information visualization
- **claude-design**: Design one-off HTML artifacts (landing pages, decks, prototypes)
- **excalidraw**: Hand-drawn Excalidraw JSON diagrams (architecture, flow, sequence)
- **manim-video**: Mathematical animations in the style of 3Blue1Brown
- **p5js**: Creative coding sketches: generative art, shaders, interactive, 3D
- **pixel-art**: Era-specific palettes (NES, Game Boy, PICO-8)
- **songwriting-and-ai-music**: Songwriting craft and Suno AI music prompts

### DevOps & Automation
- **kanban-orchestrator**: Decomposition playbook + anti-temptation rules for orchestrator
- **kanban-worker**: Pitfalls, examples, and edge cases for Hermes Kanban workers
- **opencode-smoke-test**: Verify OpenCode and Ollama endpoint health
- **webhook-subscriptions**: Event-driven agent runs via webhook subscriptions

### GitHub Workflow
- **codebase-inspection**: Inspect codebases with pygount: LOC, languages, ratios
- **github-auth**: GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login
- **github-code-review**: Review PRs: diffs, inline comments via gh or REST
- **github-issues**: Create, triage, label, assign GitHub issues via gh or REST
- **github-pr-workflow**: GitHub PR lifecycle: branch, commit, open, CI, merge
- **github-repo-management**: Clone/create/fork repos; manage remotes, releases

### Media Processing
- **gif-search**: Search/download GIFs from Tenor via curl + jq
- **spotify**: Spotify: play, search, queue, manage playlists and devices
- **youtube-content**: YouTube transcripts to summaries, threads, blogs
- **songsee**: Audio spectrograms/features (mel, chroma, MFCC) via CLI

### MLOps & Local AI
- **huggingface-hub**: HuggingFace hf CLI: search/download/upload models, datasets
- **llama-cpp**: llama.cpp local GGUF inference + HF Hub model discovery
- **segment-anything-model**: SAM: zero-shot image segmentation via points, boxes, masks
- **weights-and-biases**: W&B: log ML experiments, sweeps, model registry, dashboards

### Note-Taking & Knowledge
- **obsidian**: Read, search, create, edit, reorganize, cleanup, and Git-...
  (Specifically used for BrainVault AI work/Journal/Hermes organization)

### Productivity
- **notion**: Notion API + ntn CLI: pages, databases, markdown, Workers
- **airtable**: Airtable REST API via curl. Records CRUD, filters, upserts.
- **google-workspace**: Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python
- **linear**: Linear: manage issues, projects, teams via GraphQL + curl
- **ocr-and-documents**: Extract text from PDFs/scans (pymupdf, marker-pdf)
- **powerpoint**: Create, read, edit .pptx decks, slides, notes, templates

### Research & OSINT
- **arxiv**: Search arXiv papers by keyword, author, category, or ID
- **blogwatcher**: Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool
- **llm-wiki**: Karpathy's LLM Wiki: build/query interlinked markdown KB
- **osint**: Open-source intelligence workflows for person, channel, domain analysis
- **polymarket**: Query Polymarket: markets, prices, orderbooks, history

### Software Development Practices
- **plan**: Write markdown plan to .hermes/plans/, no execution
- **test-driven-development**: TDD: enforce RED-GREEN-REFACTOR, tests before code
- **requesting-code-review**: Pre-commit review: security scan, quality gates, auto-fix
- **systematic-debugging**: 4-phase root cause debugging: understand before fixing
- **writing-plans**: Write implementation plans: bite-sized tasks, paths, code
- **subagent-driven-development**: Execute plans via delegate_task subagents (2-stage review)
- **memory-to-file-pipeline**: Save session definitions to persistent memory and create...

## Proficiency Indicators

### Advanced (Regularly Used & Extended)
- **hermes-agent**: Configured and customized Hermes Agent itself
- **obsidian**: Built Telegram↔Obsidian↔Git sync pipeline for BrainVault
- **github-repo-management**: Created and managed repositories via gh/git/curl
- **writing-plans**: Used for detailed implementation planning
- **subagent-driven-development**: Orchestrated multi-agent workflows
- **test-driven-development**: Applied TDD principles to Python/Bash projects

### Intermediate (Frequently Used)
- **autonomous-ai-agents/codex**: Delegated coding tasks to OpenCode/Codex
- **creative/ascii-art**: Generated ASCII art for documentation and fun
- **creative/architecture-diagram**: Created system architecture diagrams
- **media/youtube-content**: Processed YouTube transcripts for research
- **mlops/llama-cpp**: Experimented with local LLM inference
- **note-taking/obsidian**: Organized BrainVault vault structure

### Foundational (Understood & Applied)
- **devops/kanban-worker**: Understanding of work delegation systems
- **research/arxiv**: Paper discovery for learning
- **productivity/notion**: Knowledge organization concepts
- **mlops/weights-and-biases**: Experiment tracking familiarity
- **creative/pixel-art**: Retro graphics generation understanding

## Practical Applications Built

### 1. Repository Health Monitor
**Skills Applied**: 
- **writing-plans** → Designed the monitoring system
- **test-driven-development** → Built with TDD principles
- **systematic-debugging** → Troubleshot file counting and size calculation
- **memory-to-file-pipeline** → Persistent baseline tracking in config.json
- **requesting-code-review** → Self-reviewed for quality and security

### 2. Telegram↔Obsidian↔Git Sync Pipeline
**Skills Applied**:
- **obsidian** → Vault reading/writing and reorganization
- **github-repo-management** → Remote repository synchronization  
- **webhook-subscriptions** → Event-driven sync triggers (conceptual)
- **kanban-orchestrator** → Task decomposition for sync workflow
- **creative/ascii-art** → Visual feedback in Telegram messages

### 3. Distributed Windows/Kali Inference Lab
**Skills Applied**:
- **mlops/llama-cpp** → Local LLM experimentation and optimization
- **mlops/huggingface-hub** → Model discovery and downloading
- **mlops/weights-and-biases** → Experiment tracking for model performance
- **creative/architecture-diagram** → System blueprint documentation
- **autonomous-ai-agents/opencode** → Code generation assistance

### 4. Local-First AI Agent Customization
**Skills Applied**:
- **hermes-agent** → Core agent configuration and skill management
- **autonomous-ai-agents/kanban-codex-lane** → Specialized worker lanes
- **devops/opencode-smoke-test** → Health monitoring for agent systems
- **creative/baoyu-infographic** → Visualizing skill relationships and usage
- **research/llm-wiki** → Building personal knowledge base of AI concepts

## Learning Trajectory & Current Focus

### Completed Foundation
- Basic Hermes agent operation and skill discovery
- Python/Bash scripting for automation
- Git/GitHub workflow for version control
- Local LLM experimentation (llama.cpp, Ollama)
- Observation and monitoring system building

### Current Development
- Advanced agent orchestration (multi-agent workflows)
- API integration and rate limiting strategies  
- Security-focused tooling and OSINT foundations
- Network monitoring and health checking systems
- Documentation and knowledge sharing systems

### Target Expansion (Networking → Cybersecurity)
- CompTIA Network+ fundamentals (in progress)
- Wireshark packet analysis practice
- Basic firewall configuration (iptables/nftables)
- Security monitoring and log analysis
- Vulnerability scanning basics
- Secure architecture principles

## Verification & Validation

Each skill in this inventory represents:
1. **Hands-on usage** - Not just theoretical knowledge
2. **Problem-solving application** - Applied to real personal projects
3. **Documentation trail** - Evidence in commits, files, or system states
4. **Transferable concepts** - Underlying principles applicable beyond Hermes
5. **Continuous learning** - Actically maintained and expanded skillset

---

*Skills inventory generated from Hermes Agent skill directory observation and personal usage tracking*
*Last updated: June 2026*