#!/usr/bin/env python3
###################################################################
# Project name: Gazorpazorp calculator
# File: LibMath.py
# Authors: Vilem Gottwald, Pavel Marek
# Description: Library implementing basic mathematical operations
###################################################################


##
# @file LibMath.py
# @author Vilem Gottwald, Pavel Marek
# @package gapalib
# Gapalib is mathematical library for GazorPazorp calculator.
#
# This math library contains basic mathematical function.
#

## number of digits to which the library rounds
digits = 10

##
# @brief Function to add two numbers.
#
# @param a First addend
# @param b Second addend
#
# @return Sum of a and b
def add(a, b):
    return round(a + b, digits)

##
# @brief Function to subtract one number from another.
#
# @param a Minuend (number we subtract from)
# @param b Subtrahend (number we subtract)
#
# @return Difference of a and b
def sub(a, b):
    return round(a - b, digits)

##
# @brief Function to multiply two numbers.
#
# @param a First factor
# @param b Second factor
#
# @return Product of a and b
def mul(a, b):
    return round(a * b, digits)

##
# @brief Function to divide two numbers.
#
# @param a Dividend
# @param b Divisor
#
# @exception ZeroDivisionError if Divisor is zero
#
# @return Quotient of a and b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division error - dividing by zero")
    return round(a / b, digits)

##
# @brief Function to compute the remainder of a division.
# Both operands have to be integers.
#
# @param a Dividend
# @param b Divisor
#
# @exception ZeroDivisionError if Divisor is zero
# @exception ValueError if operands aren't integers
#
# @return Remainder of a and b division
def mod(a, b):
    if not(isinstance(a, int) and isinstance (b, int)):
        raise ValueError("Modulo error - both operands have to be integer")
    if b == 0:
        raise ZeroDivisionError("Division error - dividing by zero")
    return round(a % b, digits)

##
# @brief Function to compute factorial.
#
# @param a Number, factorial will be computed from
#
# @exception ValueError if Number isn't positive integer
#
# @return Factorial of given number
def fact(a):
    if not isinstance(a, int) or a < 0:
        raise ValueError("Factorial error - number isn't integer or is smaller than 0")
    if a == 0:
        return 1

    result = a
    while a != 1:
        a -= 1
        result *= a
    return result

##
# @brief Function to compute power
#
# @param a Base
# @param exp Exponent
#
# @exception ValueError if Exponent isn't a natural number
# @exception ValueError if Exponent and Base are zeros
#
# @return Result of the exponentiation
def power(a, exp):
    if not isinstance(exp, int) or exp < 0:
        raise ValueError("Power error - exponent is not a natural number")
    if a == 0 and exp == 0:
        raise ValueError("Power error - zero raised to zero ins't defined")
    return round(a**exp, digits)

##
# @brief Function to compute root
#
# @param a Radicand
# @param deg Degree
#
# @exception ValueError if degree is zero
# @exception ValueError if radicant negative and degree even
#
# @return Result of the root
def root(a, deg):
    if deg % 2 == 0 and a < 0:
        raise ValueError("Root error - even degree of a negative radicant")
    if deg == 0:
        raise ValueError("Root error - degree can't be zero")

    negate = False
    if a < 0 and deg % 2 == 1:
        a = -a
        negate = True

    result = round(a**(1/deg), digits)
    return -result if negate else result

##
# @brief Function to compute absolute value of a given number
#
# @param x Number, absolute value will be computed from
#
# @return Absolute Value of given number
def abs(x):
    if x >= 0:
        return x
    if x < 0:
        return -x

# End of file LibMath.py
