from unittest import TestCase
from drivers_model.tx_db import TxDatabase


class TestExanteDatabase(TestCase):
    def test_import_from_db(self):
        test = TxDatabase(f'../config/config.ini')
        res = test.import_from_db()
        self.assertTrue(len(res) > 0)
