"""
Static + local analysis scanner for Phylax (svm-7f3a-account).
"""

from pathlib import Path
from typing import List, Dict, Any
import yaml


class Scanner:
    def __init__(self, patterns_dir: Path | None = None):
        self.patterns_dir = patterns_dir or Path(__file__).parent.parent.parent / "patterns"
        self.patterns = self._load_patterns()

    def _load_patterns(self) -> List[Dict[str, Any]]:
        patterns = []
        if not self.patterns_dir.exists():
            return patterns
        for f in self.patterns_dir.glob("*.yaml"):
            with open(f) as fh:
                data = yaml.safe_load(fh)
                if isinstance(data, list):
                    patterns.extend(data)
                elif isinstance(data, dict):
                    patterns.append(data)
        return patterns

    def scan(self, target: Path) -> List[Dict[str, Any]]:
        findings = []
        if target.is_file():
            content = target.read_text(errors="ignore")
            findings.extend(self._match_content(content, str(target)))
        elif target.is_dir():
            for ext in ("*.rs", "*.toml"):
                for f in target.rglob(ext):
                    try:
                        content = f.read_text(errors="ignore")
                        findings.extend(self._match_content(content, str(f)))
                    except Exception:
                        continue
        return findings

    def _match_content(self, content: str, location: str) -> List[Dict[str, Any]]:
        findings = []
        lines = content.splitlines()
        for pat in self.patterns:
            indicators = pat.get("indicators", [])
            for ind in indicators:
                if ind.lower() in content.lower():
                    line_no = 1
                    for i, line in enumerate(lines, 1):
                        if ind.lower() in line.lower():
                            line_no = i
                            break
                    findings.append({
                        "pattern_id": pat.get("id", "UNKNOWN"),
                        "title": pat.get("title", ""),
                        "severity": pat.get("severity", "Medium"),
                        "confidence": pat.get("default_confidence", 0.6),
                        "location": location,
                        "line": line_no,
                        "evidence": ind,
                        "description": pat.get("description", ""),
                        "remediation": pat.get("remediation", ""),
                        "protocol": "svm-7f3a-account",
                    })
        seen = set()
        unique = []
        for f in findings:
            key = (f["pattern_id"], f["location"], f["line"])
            if key not in seen:
                seen.add(key)
                unique.append(f)
        return unique
