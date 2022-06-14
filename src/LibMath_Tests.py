###################################################################
# Project name: Gazorpazorp calculator
# File: LibMath_Tests.py
# Authors: Pavel Marek
# Description: Test for LibMath.py
# Date: 27. 3. 2020
###################################################################
# Run the tests in directory src:
# $ python3 LibMath_Tests.py
#

import unittest
import LibMath


# Tests of function add
class TestAdd(unittest.TestCase):

    def test_add_int_positive(self):
        self.assertEqual(LibMath.add(10, 5), 15)
        self.assertEqual(LibMath.add(5, 10), 15)
        self.assertEqual(LibMath.add(0, 5), 5)
        self.assertEqual(LibMath.add(5, 0), 5)
        self.assertEqual(LibMath.add(0, 0), 0)

    def test_add_int_negative(self):
        self.assertEqual(LibMath.add(-10, 5), -5)
        self.assertEqual(LibMath.add(10, -5), 5)
        self.assertEqual(LibMath.add(-10, -5), -15)
        self.assertEqual(LibMath.add(0, -5), -5)
        self.assertEqual(LibMath.add(-5, 0), -5)

    def test_add_float_positive(self):
        self.assertEqual(LibMath.add(0.25, 0.30), 0.55)
        self.assertEqual(LibMath.add(0, 0.30), 0.30)
        self.assertEqual(LibMath.add(15.88, 33.1259), 49.0059)

    def test_add_float_negative(self):
        self.assertEqual(LibMath.add(0.25, -0.30), -0.05)
        self.assertEqual(LibMath.add(-0.25, 0.30), 0.05)
        self.assertEqual(LibMath.add(-15.30, -0.30), -15.60)
        self.assertEqual(LibMath.add(15.88, -33.1259), -17.2459)


# Tests of function sub
class TestSub(unittest.TestCase):

    def test_sub_int_positive(self):
        self.assertEqual(LibMath.sub(10, 5), 5)
        self.assertEqual(LibMath.sub(0, 5), -5)
        self.assertEqual(LibMath.sub(150, 150), 0)
        self.assertEqual(LibMath.sub(10, 50), -40)
        self.assertEqual(LibMath.sub(0, 0), 0)

    def test_sub_int_negative(self):
        self.assertEqual(LibMath.sub(10, -5), 15)
        self.assertEqual(LibMath.sub(-10, -5), -5)
        self.assertEqual(LibMath.sub(-10, 5), -15)

    def test_sub_float_positive(self):
        self.assertEqual(LibMath.sub(10.5, 0.5), 10)
        self.assertEqual(LibMath.sub(0, 1.5), -1.5)
        self.assertEqual(LibMath.sub(150.33, 150.33), 0)
        self.assertEqual(LibMath.sub(10.01, 50), -39.99)

    def test_sub_float_negative(self):
        self.assertEqual(LibMath.sub(10.5, -0.5), 11)
        self.assertEqual(LibMath.sub(0, -1.5), 1.5)
        self.assertEqual(LibMath.sub(-150.33, -150.33), 0)
        self.assertEqual(LibMath.sub(150.33, -150.33), 300.66)
        self.assertEqual(LibMath.sub(-150.33, 150.33), -300.66)


# Tests of function mul
class TestMul(unittest.TestCase):

    def test_mul_int_positive(self):
        self.assertEqual(LibMath.mul(10, 5), 50)
        self.assertEqual(LibMath.mul(10, 0), 0)
        self.assertEqual(LibMath.mul(0, 5), 0)
        self.assertEqual(LibMath.mul(333, 333), 110889)
        self.assertEqual(LibMath.mul(0, 0), 0)

    def test_mul_int_negative(self):
        self.assertEqual(LibMath.mul(10, -5), -50)
        self.assertEqual(LibMath.mul(-10, 5), -50)
        self.assertEqual(LibMath.mul(0, -5), 0)
        self.assertEqual(LibMath.mul(-10, 0), 0)
        self.assertEqual(LibMath.mul(-333, 333), -110889)
        self.assertEqual(LibMath.mul(-333, -333), 110889)

    def test_mul_float_positive(self):
        self.assertEqual(LibMath.mul(10.2, 5), 51)
        self.assertEqual(LibMath.mul(100.215, 15.1254), 1515.791961)
        self.assertEqual(LibMath.mul(100.215, 0), 0)
        self.assertEqual(LibMath.mul(0, 155.15), 0)

    def test_mul_float_negative(self):
        self.assertEqual(LibMath.mul(10.2, -5), -51)
        self.assertEqual(LibMath.mul(100.215, -15.1254), -1515.791961)
        self.assertEqual(LibMath.mul(-100.215, 0), 0)
        self.assertEqual(LibMath.mul(0, -155.15), 0)


# Tests of function div
class TestDiv(unittest.TestCase):

    def test_div_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(LibMath.div(10, 0))
        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(LibMath.div(0, 0))
        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(LibMath.div(10.55, 0))
        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(LibMath.div(-10.55, 0))

    def test_div_int_positive(self):
        self.assertEqual(LibMath.div(10, 5), 2)
        self.assertEqual(LibMath.div(5, 10), 0.5)

    def test_div_dividend_is_zero(self):
        self.assertEqual(LibMath.div(0, 5), 0)
        self.assertEqual(LibMath.div(0, -5), 0)
        self.assertEqual(LibMath.div(0, 5.13), 0)
        self.assertEqual(LibMath.div(0, -5.25), 0)

    def test_div_int_negative(self):
        self.assertEqual(LibMath.div(10, -5), -2)
        self.assertEqual(LibMath.div(-5, 10), -0.5)
        self.assertEqual(LibMath.div(-5, -10), 0.5)

    def test_div_float_positive(self):
        self.assertEqual(LibMath.div(10.54, 5), 2.108)
        self.assertAlmostEqual(LibMath.div(5, 64.25), 0.077821)

    def test_div_float_negative(self):
        self.assertEqual(LibMath.div(10.54, -5), -2.108)
        self.assertAlmostEqual(LibMath.div(5, -64.25), -0.077821)
        self.assertEqual(LibMath.div(-10.54, 5), -2.108)
        self.assertAlmostEqual(LibMath.div(-5, 64.25), -0.077821)
        self.assertEqual(LibMath.div(-10.54, -5), 2.108)
        self.assertAlmostEqual(LibMath.div(-5, -64.25), 0.077821011673)


# Tests of function fact
class TestFact(unittest.TestCase):

    def test_fact_with_zero(self):
        self.assertEqual(LibMath.fact(0), 1)

    def test_fact_not_int_or_lesser_than_zero(self):
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.fact(-5))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.fact(-20.5))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.fact(20.5))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.fact(54.5487))

    def test_fact_int_positive(self):
        self.assertEqual(LibMath.fact(3), 6)
        self.assertEqual(LibMath.fact(12), 479001600)


# Tests of function power
class TestPower(unittest.TestCase):

    def test_power_base_is_zero(self):
        self.assertEqual(LibMath.power(0, 15), 0)
        self.assertEqual(LibMath.power(0, 22), 0)

    def test_power_exponent_is_zero(self):
        self.assertEqual(LibMath.power(5, 0), 1)
        self.assertEqual(LibMath.power(2.5, 0), 1)
        self.assertEqual(LibMath.power(-5, 0), 1)
        self.assertEqual(LibMath.power(-2.5, 0), 1)

    def test_power_base_and_exponent_are_zero(self):
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.power(0, 0))

    def test_power_exponent_is_not_int_except_for_zero(self):
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.power(5, -2))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.power(5, -2.5))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.power(5, 2.5))

    def test_power_base_int_positive(self):
        self.assertEqual(LibMath.power(2, 4), 16)
        self.assertEqual(LibMath.power(25, 5), 9765625)

    def test_power_base_int_negative(self):
        self.assertEqual(LibMath.power(-2, 4), 16)
        self.assertEqual(LibMath.power(-25, 5), -9765625)

    def test_power_base_float_positive(self):
        self.assertEqual(LibMath.power(2.5, 4), 39.0625)
        self.assertAlmostEqual(LibMath.power(11.589, 6), 2422566.889458712667)
        self.assertAlmostEqual(LibMath.power(21.112, 5), 4194178.272112057)

    def test_power_base_float_negative(self):
        self.assertEqual(LibMath.power(-2.5, 4), 39.0625)
        self.assertEqual(LibMath.power(-2.5, 5), -97.65625)
        self.assertAlmostEqual(LibMath.power(-11.589, 3), -1556.459729, 6) 
        self.assertAlmostEqual(LibMath.power(-11.2, 3), -1404.928)
        self.assertAlmostEqual(LibMath.power(-21.112, 5), -4194178.272112056696)


# Tests of function root
class TestRoot(unittest.TestCase):

    def test_root_degree_is_zero(self):
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(2, 0))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(-4, 0))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(25.5, 0))

    def test_root_even_degree_of_a_negative_radicant(self):
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(-5, 2))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(-5.5, 4))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(-5.55, 6))
        with self.assertRaises(ValueError):
            self.assertRaises(LibMath.root(-5, 10))

    def test_root_int_positive(self):
        self.assertEqual(LibMath.root(1, 5), 1)
        self.assertAlmostEqual(LibMath.root(155, 5), 2.741992987, 6) 
        self.assertEqual(LibMath.root(15, 1), 15)
        self.assertEqual(LibMath.root(0, 2), 0)

    def test_root_float_positive(self):
        self.assertAlmostEqual(LibMath.root(185.55, 2.33), 9.409973368, 6) 
        self.assertEqual(LibMath.root(0.2, 0.2), 0.00032)

    def test_root_int_negative(self):
        self.assertEqual(LibMath.root(-1, -5), -1)
        self.assertEqual(LibMath.root(16, -2), 0.25)
        self.assertEqual(LibMath.root(1, -5), 1)
        self.assertEqual(LibMath.root(2147483648, -31), 0.5)

    def test_root_float_negative(self):
        self.assertEqual(LibMath.root(0.2, -0.2), 3125)
        self.assertEqual(LibMath.root(-0.2, -0.2), -3125)


# Tests of function abs
class TestAbs(unittest.TestCase):

    def test_abs_int_positive(self):
        self.assertEqual(LibMath.abs(1), 1)
        self.assertEqual(LibMath.abs(155), 155)

    def test_abs_int_negative(self):
        self.assertEqual(LibMath.abs(-1), 1)
        self.assertEqual(LibMath.abs(-155), 155)

    def test_abs_float_positive(self):
        self.assertEqual(LibMath.abs(15.458), 15.458)

    def test_abs_float_negative(self):
        self.assertEqual(LibMath.abs(-15.458), 15.458)

    def test_abs_zero(self):
        self.assertEqual(LibMath.abs(0), 0)


# to simplify testing
if __name__ == '__main__':
    unittest.main()
