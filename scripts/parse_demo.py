"""Quick CLI: python scripts/parse_demo.py <file>"""
import sys
from backend.parser import parse_document

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: parse_demo.py <file>")
        sys.exit(1)
    chunks = parse_document(sys.argv[1])
    print(f"Parsed {len(chunks)} chunks")
    for c in chunks[:5]:
        print(f"\n[{c['id']}] {c['text'][:200]}")
