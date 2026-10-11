import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from residue_classifier import main,scan,classify

class ContractTests(unittest.TestCase):
    def test_limit_exclusions_and_idempotent_report(self):
        with tempfile.TemporaryDirectory() as root:
            root=Path(root)
            for name in ['a','b','c']: (root/name).write_text('unchanged')
            (root/'.git').mkdir();(root/'.git'/'private').write_text('excluded')
            (root/'link').symlink_to(root/'a')
            output=root/'report.json';output.write_text('{}')
            first=scan(root,output,2);second=scan(root,output,2)
            self.assertTrue(first['truncated']);self.assertEqual(first['rows'],second['rows'])
            self.assertEqual(first['rows'],[{'path':'a','class':'review_needed'},{'path':'b','class':'review_needed'}])
            self.assertEqual((root/'a').read_text(),'unchanged')
    def test_failure_is_structured_and_nonzero(self):
        with contextlib.redirect_stdout(io.StringIO()) as stream:
            status=main(['--workspace','/does-not-exist','--stdout'])
        self.assertEqual(status,1);self.assertEqual(json.loads(stream.getvalue())['error']['code'],'SCAN_FAILED')
    def test_labeled_synthetic_rules_and_boundary(self):
        fixture={'STATE.md':'canonical','NEXT-ACTION.md':'canonical','memory/errors.md':'local_only',
                 'memory/errors.md.bak':'review_needed','logs/session':'runtime_or_state',
                 'data/events':'runtime_or_state','notes':'review_needed','important_customer_backup':'review_needed'}
        self.assertEqual({path:classify(path) for path in fixture},fixture)
