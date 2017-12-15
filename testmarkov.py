import unittest

import markov


class TestMarkov(unittest.TestCase):
    def test_get_table(self):
        # run a unit
        # get a result
        res = markov.get_table('xy')
        
        # make assertion about result
        self.assertEqual(res, {'x': {'y': 1}})

    def test_class(self):
        m = markov.Markov('ab')
        self.assertTrue(m is not None)

    def test_predict(self):
        m = markov.Markov('hello world')
        markov.random.seed(42)
        res = m.predict('o')
        self.assertEqual(res, ' ')

if __name__ == '__main__':
    unittest.main()
