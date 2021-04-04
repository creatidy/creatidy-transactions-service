from unittest import TestCase
from import_controller.exante_controller import Exante


class TestExanteDatabase(TestCase):
    def test_import_from_db(self):
        test = Exante()
        res = test.import_from_external_source()
        self.assertTrue(len(res) > 0)
