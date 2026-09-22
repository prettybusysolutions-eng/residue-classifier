# Quickstart

Residue Classifier is intentionally non-destructive. Run it against a disposable
sample before pointing it at a real workspace.

```bash
git clone https://github.com/prettybusysolutions-eng/residue-classifier.git
cd residue-classifier
repo_dir="$(pwd)"
sample_dir="$(mktemp -d)"
mkdir -p "$sample_dir/logs"
touch "$sample_dir/STATE.md" "$sample_dir/logs/session.jsonl" "$sample_dir/notes.txt"
cd "$sample_dir"
python3 "$repo_dir/residue_classifier.py"
python3 -m json.tool residue-classifier-report.json
```

Expected classifications:

- `STATE.md` → `canonical`
- `logs/session.jsonl` → `runtime_or_state`
- `notes.txt` → `review_needed`

The command writes one JSON report and deletes nothing.
