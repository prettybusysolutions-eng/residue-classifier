# Residue Classifier

Residue Classifier is a small local utility for sorting workspace sprawl into buckets like canonical, runtime, local-only, or review-needed before cleanup.

I wrote it because once a workspace gets busy enough, it becomes way too easy to lose track of what is real, what is temporary, and what should never have been in the root in the first place.

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
- [Stripe Payment Link Placeholder]

## Support
If the free version helped you separate signal from junk, good. If you want the deeper cleanup and governance layer, that is what the Pro version is for.
