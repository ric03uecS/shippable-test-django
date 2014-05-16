from django.test import TestCase

class FirstAppTestCase(TestCase):
    def test_first_test_1(self):
        self.assertEqual(True, True)

    def test_first_test_2(self):
        self.assertEqual(2, 2)
