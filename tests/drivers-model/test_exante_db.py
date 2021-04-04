from unittest import TestCase
from drivers_model.exante_db import ExanteDatabase


class TestExanteDatabase(TestCase):
    def test_import_from_db(self):
        test = ExanteDatabase(f'config/config.ini')
        res = test.import_from_db()
        self.assertTrue(len(res) > 0)
