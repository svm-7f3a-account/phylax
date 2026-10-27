"""
Main CLI entry point for Phylax.
"""

import argparse
import json
from pathlib import Path

from .scanner import Scanner
from .reporter import Reporter


def main():
    parser = argparse.ArgumentParser(
        prog="phylax",
        description="Phylax (svm-7f3a-account) — Defensive Solana vulnerability discovery"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    scan_p = sub.add_parser("scan", help="Scan a Solana program or project")
    scan_p.add_argument("path", type=Path, help="Path to source, IDL, or project directory")
    scan_p.add_argument("--patterns", type=Path, default=None, help="Custom patterns directory")
    scan_p.add_argument("--output", type=Path, default=None, help="Write JSON findings to file")

    report_p = sub.add_parser("report", help="Generate a human-readable report from findings")
    report_p.add_argument("--findings", type=Path, required=True, help="JSON findings file")
    report_p.add_argument("--format", choices=["markdown", "json"], default="markdown")
    report_p.add_argument("--output", type=Path, default=None)

    args = parser.parse_args()

    if args.command == "scan":
        scanner = Scanner(patterns_dir=args.patterns)
        findings = scanner.scan(args.path)
        if args.output:
            args.output.write_text(json.dumps(findings, indent=2))
            print(f"Wrote {len(findings)} findings to {args.output}")
        else:
            print(json.dumps(findings, indent=2))

    elif args.command == "report":
        reporter = Reporter()
        data = json.loads(args.findings.read_text())
        out = reporter.render(data, fmt=args.format)
        if args.output:
            args.output.write_text(out)
            print(f"Report written to {args.output}")
        else:
            print(out)


if __name__ == "__main__":
    main()
