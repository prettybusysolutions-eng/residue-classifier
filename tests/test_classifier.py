import os
import tempfile
import unittest
from pathlib import Path

import residue_classifier


class ClassifierTest(unittest.TestCase):
    def test_known_classes_and_unknown_default(self):
        self.assertEqual(residue_classifier.classify("STATE.md"), "canonical")
        self.assertEqual(
            residue_classifier.classify("logs/session.jsonl"),
            "runtime_or_state",
        )
        self.assertEqual(
            residue_classifier.classify("notes.txt"),
            "review_needed",
        )

    def test_run_is_non_destructive(self):
        with tempfile.TemporaryDirectory() as directory:
            original_cwd = Path.cwd()
            original_workspace = residue_classifier.WORKSPACE
            original_report = residue_classifier.REPORT
            try:
                os.chdir(directory)
                sample = Path("notes.txt")
                sample.write_text("keep me", encoding="utf-8")
                residue_classifier.WORKSPACE = Path.cwd()
                residue_classifier.REPORT = Path.cwd() / "residue-classifier-report.json"
                residue_classifier.run()
                self.assertEqual(sample.read_text(encoding="utf-8"), "keep me")
                self.assertTrue(residue_classifier.REPORT.exists())
            finally:
                residue_classifier.WORKSPACE = original_workspace
                residue_classifier.REPORT = original_report
                os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
