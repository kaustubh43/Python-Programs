import unittest
import script


class TestMain(unittest.TestCase):
    def setUp(self) -> None:  # The setup function is called before any function call
        print('Starting a function....')

    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'ABCD'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):  # same as above method but used assertIsInstance
        test_param = 'ABCD'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff4(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please pass a number')

    def test_do_stuff5(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please pass a number')

    def test_do_stuff6(self):
        test_param = 0
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please pass a number')

    def tearDown(self) -> None:  # This function is called after a function has finished executing
        print('Cleaning Up')


if __name__ == '__main__':
    unittest.main()
