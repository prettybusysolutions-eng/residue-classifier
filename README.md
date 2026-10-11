# Residue Classifier

Forensic categorization and hygiene protocols for structured data cleanup.

Residue Classifier is part of the operator kit for separating canonical assets, transient residue, runtime artifacts, and review-needed material before cleanup or promotion decisions are made.

**Start here:** [run the two-minute quickstart](QUICKSTART.md).

Release status and gates: [RELEASING.md](RELEASING.md).

## Role in the system
Cleanup without classification creates risk.
This layer exists to preserve signal while reducing sprawl.

## Standard
Classify first.
Remove carefully.
Protect what matters.

## What it does
- scans a workspace tree
- classifies files into governance buckets
- writes a local residue report
- stays non-destructive
- is safe to rerun

## Why use it
If you are about to clean up a workspace and you are not completely sure what should be kept, ignored, promoted, or archived, classification first is safer than deletion first.

## Files
- `residue_classifier.py` — local classification script
- `SKILL.md` — skill wrapper / usage context
- `LICENSE`
- `CONTRIBUTING.md`

## Usage
```bash
python3 residue_classifier.py
```

That writes a local `residue-classifier-report.json` in the current working directory.

## Safety
- no destructive actions
- no secret embedding
- no automatic cleanup
- report generation only

## Upgrade to Pro
The free version gives you a safe classification pass.
The Pro version is for when you want to save 5+ hours of cleanup confusion, reduce repo risk, and get a clearer path to a clean workspace.

Pro is intended to include:
- richer classification rules
- confidence-scored recommendations
- backup-first cleanup planning
- thin-root cleanup order
- clearer promote / ignore / archive decisions

Stripe Payment Link:
- https://buy.stripe.com/7sY00idgkcoresgbkG0kE07

## Support
If the free version helped you separate signal from junk, good. If you want the deeper cleanup and governance layer, that is what the Pro version is for.

## Versioned CLI and output contract

Install with `python -m pip install .`, then run `residue-classifier --version`
or `residue-classifier --workspace /path --stdout`. Version 0.1.0 returns the
complete schemaVersion 1 JSON report on stdout. Without `--stdout`, it also
writes a report; `--output` selects its location. `--max-files` defaults to 500.
`truncated=true` explicitly marks incomplete coverage. Exit 0 means scan completion,
not that files are safe to delete; exit 1 reports `SCAN_FAILED` for scan/I/O errors.
Git internals, symlinks and the output report are excluded. A write error does not
produce a success result. Reruns do not classify the previous output as evidence.

Eight synthetic labeled filename cases pass, including a misleading backup
name and the `memory/errors.md.bak` boundary. This is rule conformance, not measured
precision or recall on real workspaces. The classifier never reads file contents;
it cannot identify secrets, malicious files, redundant data or actual canonical
ownership. Unknown files remain review-needed. Files may change during a scan;
this is not a forensic snapshot or deletion authorization.
