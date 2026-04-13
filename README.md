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

## Support / Upgrade
- Tip Jar: https://gumroad.com/l/claw-foundry-tip-jar
- Pro Upgrade: https://gumroad.com/l/residue-classifier-pro

If it helps you separate signal from junk, good. If you want the whole workspace governance layer cleaned up properly, that is the upgrade path.
