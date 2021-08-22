import unittest
import random
def PEP(cls):
    import importlib
    num = int(cls.__name__.split('PEP')[1])
    try:
        module = importlib.import_module(f'pep{num}')
    except ImportError:
        module = None
    if module is None:
        return unittest.skip('Import failure')(cls)
    setattr(cls, f'pep{num}', module)
    return cls
@PEP
class TestPEP204(unittest.TestCase):
    def test_all_given(self):
        params = {(1, 2, 3),
                  (0, 10, 2),
                  (-20, 125, 67),
                  (75, 26, -2),
                  (6, -3, -1),
                  (0, 0, 1),
                  }
        for p in params:
            with self.subTest(p=p):
                self.assertEqual(self.pep204[p[0]:p[1]:p[2]],
                                 range(*p))
    def test_omitted(self):
        params = ((1, 2),
                  (7,),
                  (4, 21),
                  (6, 17),
                  (1, 6),
                  [7, 60],
                  (-1,),
                  [16],
                  )
        for p in params:
            with self.subTest(p=p):
                if isinstance(p, list):
                    if len(p) == 1:
                        self.assertEqual(self.pep204[p[0]], range(*p))
                    else:
                        self.assertEqual(self.pep204[:p[0]:p[1]],
                                         range(0, *p))
                elif len(p) == 1:
                    self.assertEqual(self.pep204[:p[0]:], range(*p))
                elif len(p) == 2:
                    self.assertEqual(self.pep204[p[0]:p[1]], range(*p))
                else:
                    self.fail(f'Invalid argument {p!r}')
    def test_errors(self):
        for p in {(1, 2), (3, 4), (20, -6), (1024, 69927)}:
            with self.subTest(p=p):
                with self.assertRaisesRegex(ValueError,
                                            'Stop is required'):
                    self.pep204[p[0]::p[1]]
        for p in {(1.0, 2.5, 6.2), (49.4, 999.4, 7777.291),
                  (-1, 0.15, 5.4), (7.39, 9993, -1.0)}:
            with self.subTest(p=p):
                with self.assertRaises(TypeError):
                    self.pep204[p[0]:p[1]:p[2]]
@PEP
class TestPEP211(unittest.TestCase):
    def setUp(self):
        self.w = self.pep211.wrapper
        self.itertools = __import__('itertools')
    def assertEq(self, *args, **kwargs):
        try:
            a, b = list(args[0]), list(args[1])
        except TypeError:
            a, b = args[:2]
        return self.assertEqual(a, b, *args[2:], **kwargs)
    def test_call(self):
        objects = (1,
                   20.5,
                   complex(6, 2),
                   '666',
                   b'777',
                   (8, 9, 10),
                   [8, 9, 10],
                   {8: 9, 10: 11, 12: 13},
                   {8, 9, 10},
                   memoryview(b'Hello, world!'),
                   True,
                   (x for x in range(25)),
                   enumerate([555, 999, 666, -111]))
        for obj in objects:
            with self.subTest(obj=obj):
                self.assertEqual(self.w(obj)(), obj)
    def test_success(self):
        self.assertEq(self.w((6, 6, 6)) @ (7, 7, 7),
                      self.itertools.product((6, 6, 6), (7, 7, 7)))
        self.assertEq(self.w((-1, -9, 6, 2, 7)) @ self.w((94, 9)),
                      self.itertools.product((-1, -9, 6, 2, 7),
                                             (94, 9)))
        self.assertEq((3.14, 3.15) @ self.w((2.71, 2.72)),
                      self.itertools.product((3.14, 3.15),
                                             (2.71, 2.72)))

def run():
    unittest.main(verbosity=2)
if __name__ == '__main__':
    run()