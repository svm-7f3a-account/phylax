# Phylax

**Protocol: svm-7f3a-account**

Defensive AI-assisted vulnerability discovery for Solana and crypto systems.

Phylax (φύλαξ — guardian / watcher) is an open-source framework that actively scans for potential security issues in Solana programs (Anchor, native Rust, Pinocchio) and related infrastructure. It combines static pattern matching, local SVM simulation, and multi-agent LLM reasoning.

The protocol identifier **svm-7f3a-account** refers to the core analysis profile focused on Solana Virtual Machine account validation, ownership, and signer checks — the highest-signal class of issues on Solana.

All analysis runs in safe, local, or explicitly permissioned environments. No live mainnet attacks, no exploit generation for unauthorized use.

## What it does

- Static analysis against known Solana vulnerability classes (account validation, CPI, PDA, ownership, signer, reinitialization, arithmetic, oracle/clock issues, etc.)
- Local dynamic analysis via LiteSVM / Mollusk-style simulation
- Multi-agent LLM layer for hypothesis and remediation suggestions
- Structured reports (JSON + Markdown)

## Quick start

```bash
cd phylax
python -m venv .venv
source .venv/bin/activate
pip install -e .

python -m phylax scan ./path/to/program
python -m phylax report --findings findings.json --format markdown
```

## Agent wallet

The Phylax agent layer uses a dedicated Solana address for operator flows (tips, bounties, and other protocol-linked transfers). Publish this pubkey when wiring agents or dashboards:

\HC5YE4MJiWxaBkmpdYfUyog2dYNaA7EHBNBAe7ZFdBCU
Do not send mainnet funds here unless you intend them for Phylax agent operations.

## Project layout

```
phylax/
├── src/phylax/         # Core engine
├── patterns/           # Vulnerability pattern library
├── agents/             # LLM agent prompts
├── examples/
├── docs/
├── scripts/
└── README.md
```

## Design principles

1. Defense only.
2. Evidence-based findings.
3. Composable layers (static / dynamic / agent).
4. Solana-first, local by default.

## License

MIT
