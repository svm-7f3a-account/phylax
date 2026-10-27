"""
Report generation for Phylax.
"""

from typing import List, Dict, Any


class Reporter:
    def render(self, findings: List[Dict[str, Any]], fmt: str = "markdown") -> str:
        if fmt == "json":
            import json
            return json.dumps(findings, indent=2)

        lines = ["# Phylax Scan Report", "", "**Protocol:** svm-7f3a-account", "", f"Findings: {len(findings)}", ""]
        if not findings:
            lines.append("No issues matched current patterns.")
            return "\n".join(lines)

        order = ["Critical", "High", "Medium", "Low", "Info"]
        by_sev = {}
        for f in findings:
            by_sev.setdefault(f.get("severity", "Medium"), []).append(f)

        for sev in order:
            items = by_sev.get(sev, [])
            if not items:
                continue
            lines.append(f"## {sev} ({len(items)})")
            lines.append("")
            for f in items:
                lines.append(f"### {f.get('pattern_id')} — {f.get('title')}")
                lines.append(f"- **Location**: `{f.get('location')}:{f.get('line')}`")
                lines.append(f"- **Confidence**: {f.get('confidence')}")
                lines.append(f"- **Evidence**: `{f.get('evidence')}`")
                lines.append(f"- **Description**: {f.get('description')}")
                lines.append(f"- **Remediation note**: {f.get('remediation')}")
                lines.append("")
        return "\n".join(lines)
