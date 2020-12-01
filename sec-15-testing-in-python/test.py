import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()


# O/P:  python3 test.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
