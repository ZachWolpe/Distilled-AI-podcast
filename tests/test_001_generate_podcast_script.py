"""
---------------------------------------------------------------------------
test_001_generate_podcast_script.py

: zachcolinwolpe@gmail.com
: 12.12.24
---------------------------------------------------------------------------
"""

import unittest
from src.prompt_engine import parse_runtime_yaml


class TestPromptEngine(unittest.TestCase):
    def test_parse_runtime_yaml(self, path_to_yml='./src/runtime.yml'):
        config = parse_runtime_yaml(path_to_yml)
        self.assertIn('stage_1_generate_script_from_pdf', config)

        # check all keys in "stage_1_generate_script_from_pdf" are present
        expected_stage_1_generate_script_from_pdf_keys = [
            'episode_name', 'path_to_pdf', 'output_dir', 'output_name'
        ]
        for key in expected_stage_1_generate_script_from_pdf_keys:
            self.assertIn(key, config['stage_1_generate_script_from_pdf'])


if __name__ == '__main__':
    unittest.main()
