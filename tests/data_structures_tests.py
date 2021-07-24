import unittest
import math
from ray_tracer import data_structures


class TestDataStructures(unittest.TestCase):
    
    def test_point_tuple(self):
        point = data_structures.Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(point.x, 4.3)
        self.assertEqual(point.y, -4.2)
        self.assertEqual(point.z, 3.1)
        self.assertEqual(point.w, 1.0)
        self.assertTrue(point.is_point())
        self.assertFalse(point.is_vector())

    def test_vector_tuple(self):
        vector = data_structures.Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(vector.x, 4.3)
        self.assertEqual(vector.y, -4.2)
        self.assertEqual(vector.z, 3.1)
        self.assertEqual(vector.w, 0.0)
        self.assertFalse(vector.is_point())
        self.assertTrue(vector.is_vector())

    def test_factory_classes(self):
        point = data_structures.Point(4, -4, 3)
        self.assertEqual(point, data_structures.Tuple(4, -4, 3, 1))
        vector = data_structures.Vector(4, -4, 3)
        self.assertEqual(vector, data_structures.Tuple(4, -4, 3, 0))

    def test_tuple_addition(self):
        a1 = data_structures.Tuple(3, -2, 5, 1)
        a2 = data_structures.Tuple(-2, 3, 1, 0)
        self.assertEqual(a1+a2, data_structures.Tuple(1, 1, 6, 1))

    def test_tuple_subtraction(self):
        p1 = data_structures.Point(3, 2, 1)
        p2 = data_structures.Point(5, 6, 7)
        self.assertEqual(p1-p2, data_structures.Vector(-2, -4, -6))

        v1 = data_structures.Vector(5, 6, 7)
        self.assertEqual(p1-v1, data_structures.Point(-2, -4, -6))
        v2 = data_structures.Vector(3, 2, 1)
        self.assertEqual(v2-v1, data_structures.Vector(-2, -4, -6))

    def test_negate_tuple(self):
        zero = data_structures.Vector(0, 0, 0)
        v = data_structures.Vector(1, -2, 3)
        self.assertEqual(zero-v, data_structures.Vector(-1, 2, -3))
        self.assertEqual(-v, data_structures.Vector(-1, 2, -3))

    def test_tuple_multiplication(self):
        a = data_structures.Tuple(1, -2, 3, -4)
        self.assertEqual(a*3.5, data_structures.Tuple(3.5, -7, 10.5, -14))
        self.assertEqual(a*3, data_structures.Tuple(3, -6, 9, -12))
        self.assertEqual(a*0.5, data_structures.Tuple(0.5, -1, 1.5, -2))

    def test_tuple_devision(self):
        a = data_structures.Tuple(1, -2, 3, -4)
        self.assertEqual(a/2, data_structures.Tuple(0.5, -1, 1.5, -2))

    def test_tuple_magnitude(self):
        v = data_structures.Vector(1, 0, 0)
        self.assertEqual(v.magnitude(), 1)
        v = data_structures.Vector(0, 1, 0)
        self.assertEqual(v.magnitude(), 1)
        v = data_structures.Vector(0, 0, 1)
        self.assertEqual(v.magnitude(), 1)
        v = data_structures.Vector(1, 2, 3)
        self.assertEqual(v.magnitude(), math.sqrt(14))
        v = data_structures.Vector(-1, -2, -3)
        self.assertEqual(v.magnitude(), math.sqrt(14))

    def test_tuple_normalization(self):
        v = data_structures.Vector(4, 0, 0)
        self.assertEqual(v.normalize(), data_structures.Vector(1, 0, 0))
        v = data_structures.Vector(1, 2, 3)
        norm = v.normalize()
        self.assertAlmostEqual(norm.x, 0.26726, places=5)
        self.assertAlmostEqual(norm.y, 0.53452, places=5)
        self.assertAlmostEqual(norm.z, 0.80178, places=5)
        self.assertAlmostEqual(v.normalize().magnitude(), 1)

    def test_tuple_dot_product(self):
        a = data_structures.Vector(1, 2, 3)
        b = data_structures.Vector(2, 3, 4)
        self.assertEqual(a.dot(b), 20)

    def test_3d_cross_product(self):
        a = data_structures.Vector(1, 2, 3)
        b = data_structures.Vector(2, 3, 4)
        self.assertEqual(a.cross(b), data_structures.Vector(-1, 2, -1))
        self.assertEqual(b.cross(a), data_structures.Vector(1, -2, 1))

        x = data_structures.Vector(1, 0, 0)
        y = data_structures.Vector(0, 1, 0)
        z = data_structures.Vector(0, 0, 1)
        self.assertEqual(x.cross(y), z)
        self.assertEqual(y.cross(z), x)
        self.assertEqual(z.cross(x), y)
        self.assertEqual(z.cross(y), -x)

    def test_color_attrs(self):
        c = data_structures.Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)

    def test_color_operations(self):
        c1 = data_structures.Color(0.9, 0.6, 0.75)
        c2 = data_structures.Color(0.7, 0.1, 0.25)
        c = c1-c2
        self.assertAlmostEqual(c1+c2, data_structures.Color(1.6, 0.7, 1.0, 2))
        self.assertAlmostEqual(c.x, 0.2, places=5)
        self.assertAlmostEqual(c.y, 0.5, places=5)
        self.assertAlmostEqual(c.z, 0.5, places=5)
        self.assertAlmostEqual(c1*2, data_structures.Color(1.8, 1.2, 1.5, 2))

    def test_muliplying_colors(self):
        c1 = data_structures.Color(1, 0.2, 0.4)
        c2 = data_structures.Color(0.9, 1, 0.1)
        c3 = c1*c2
        self.assertAlmostEqual(c3.x, 0.9, places=5)
        self.assertAlmostEqual(c3.y, 0.2, places=5)
        self.assertAlmostEqual(c3.z, 0.04, places=5)
