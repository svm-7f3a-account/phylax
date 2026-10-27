#!/usr/bin/env python3
"""
Simple local test runner for Phylax.
"""

import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from phylax.scanner import Scanner
from phylax.reporter import Reporter


def main():
    snippet = '''
use anchor_lang::prelude::*;

pub fn withdraw(ctx: Context<Withdraw>) -> Result<()> {
    let account = ctx.accounts.vault.to_account_info();
    Ok(())
}

#[derive(Accounts)]
pub struct Withdraw<'info> {
    /// CHECK: illustration only
    pub vault: AccountInfo<'info>,
}
'''
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "example.rs"
        p.write_text(snippet)
        scanner = Scanner()
        findings = scanner.scan(p)
        print(Reporter().render(findings, "markdown"))


if __name__ == "__main__":
    main()
