# Phylax — Architecture

**Protocol identifier:** `svm-7f3a-account`

## Overview

Phylax is a multi-layer defensive scanner focused on Solana account-model issues.

```
┌─────────────────────────────────────────┐
│           Report / Output Layer         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Agent Reasoning Layer           │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Analysis Engines                │
│  Static Patterns  |  Local SVM (LiteSVM)│
│  Optional fuzz hooks                    │
└─────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│  Source / IDL / bytecode                │
└─────────────────────────────────────────┘
```

## Protocol: svm-7f3a-account

This is the primary analysis profile. It prioritizes:
- Account ownership verification
- Signer checks on privileged paths
- Account confusion / type confusion
- PDA canonicality
- CPI target validation

Other profiles can be added later (e.g. arithmetic, oracle, business-logic).

## Safety

All execution is local or explicitly user-provided sandbox. No automatic mainnet interaction. No generation of ready-to-use exploit transactions.
