import unittest
import random  # NOQA
def PEP(cls):
    import importlib
    num = int(cls.__name__.split('PEP')[1])
    try:
        module = importlib.import_module(f'pep{num}')
    except ImportError:
        try:
            module = importlib.import_module(f'.pep{num}', 'rejected_peps')
        except ImportError:
            module = None
    if module is None:
        return unittest.skip('Import failure')(cls)
    setattr(cls, f'pep{num}', module)
    setattr(cls, 'num', num)
    return cls
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
iterables = objects[5:9]

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
@PEP
class TestPEP212(unittest.TestCase):
    def test_indices(self):
        for i in iterables:
            with self.subTest(i=i):
                self.assertEqual(self.pep212.indices(i), range(len(i)))
    def test_irange(self):
        for i in iterables:
            with self.subTest(i=i):
                self.assertEqual(list(self.pep212.irange(i)),
                                list(enumerate(i)))
                self.assertEqual(list(self.pep212.irange(i)),
                                list(zip(range(len(i)), i)))
@PEP
class TestPEP259(unittest.TestCase):
    def setUp(self):
        self.sio = __import__('io').StringIO
    def test_regular(self):
        s = self.sio()
        self.pep259.print(file=s)
        self.assertEqual(s.getvalue(), '\n')
        del s
        s = self.sio()
        self.pep259.print(1, 2, 3, 4, file=s)
        self.assertEqual(s.getvalue(), '1 2 3 4\n')
        del s
        s = self.sio()
        self.pep259.print(787, '4949848373737', -1.5,
                          sep='\n', end='\t123\n', file=s)
        self.assertEqual(s.getvalue(), '787\n4949848373737\n-1.5\t123\n')
        del s
    def test_omit(self):
        s = self.sio()
        self.pep259.print(1, 2, 3, 4, '\n', file=s)
        self.assertEqual(s.getvalue(), '1 2 3 4 \n')
        del s
        s = self.sio()
        self.pep259.print(27575, '\n\n', sep='\t', file=s)
        self.assertEqual(s.getvalue(), '27575\t\n\n')
        del s
@PEP
class TestPEP265(unittest.TestCase):
    def test_sorted(self):
        self.assertIs(self.pep265.sorted, sorted)
    def test_constants(self):
        self.assertEqual(self.pep265.ORIGINAL, -1)
        self.assertEqual(self.pep265.KEYS, 0)
        self.assertEqual(self.pep265.VALUES, +1)
    def test_itemlist(self):
        import math
        sp = self.pep265
        testdict = {1: 9, 5: 6, 3: 3}
        # Test ORIGINAL
        self.assertListEqual(sp.itemlist(testdict, sp.ORIGINAL),
                             list(testdict.items()))
        # Test KEYS & key
        self.assertListEqual(sp.itemlist(testdict, sp.KEYS,
                                         key=math.log2),
                             [(1, 9), (3, 3), (5, 6)])
        # Test VALUES & reverse
        self.assertListEqual(sp.itemlist(testdict, sp.VALUES, reverse=True),
                             [(1, 9), (5, 6), (3, 3)])
        # Test ORIGINAL & reverse
        self.assertListEqual(sp.itemlist(testdict, sp.ORIGINAL, reverse=True),
                             [(3, 3), (5, 6), (1, 9)])
        with self.assertRaises(TypeError):
            sp.itemlist({None: 1, 3: 2, 4: None}, sp.KEYS)
    def test_alias(self):
        self.assertIs(self.pep265.items, self.pep265.itemlist)
@PEP
class TestPEP276(unittest.TestCase):
    def test_subclass(self):
        self.assertIsInstance(self.pep276.int(20), int)
    def test_iter(self):
        self.assertTupleEqual(tuple(self.pep276.int(99)),
                              tuple(range(99)))
        self.assertTupleEqual(tuple(self.pep276.int('0')),
                              tuple(range(0)))
        self.assertTupleEqual(tuple(self.pep276.int(-3.14)),
                              tuple(range(0)))
@PEP
class TestPEP281(unittest.TestCase):
    def test_regular(self):
        from decimal import Decimal
        r = self.pep281.range
        self.assertTupleEqual(tuple(r(1, 6)),
                              (1, 2, 3, 4, 5))
        self.assertTupleEqual(tuple(r(7, 3, -1)),
                              (7, 6, 5, 4))
        self.assertTupleEqual(tuple(r(1, 9, 2)),
                              (1, 3, 5, 7))
        A = type('A', (), {'__index__': (lambda s: 2)})
        self.assertTupleEqual(tuple(r(A(), 5)),
                              (2, 3, 4))
        for a in [(1.0, 2.0, 0.5),
                  (Decimal('1')),
                  (complex(2, 7), 7)]:
            with self.subTest(arg=a):
                with self.assertRaises(TypeError):
                    r(1.0, 2.0, 0.5)
    def test_new(self):
        import itertools
        r = self.pep281.range
        for a, b, c in itertools.permutations(iterables, 3):
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(r(a, b, c), range(len(a),
                                                   len(b),
                                                   len(c)))

def run(**kwargs):
    if 'v' in kwargs and 'verbosity' not in kwargs:
        kwargs['verbosity'] = kwargs.pop('v')
    kwargs.setdefault('verbosity', 2)
    unittest.main(**kwargs)
if __name__ == '__main__':
    run(v=2)
