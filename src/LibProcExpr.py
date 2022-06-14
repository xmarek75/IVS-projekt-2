#!/usr/bin/env python3
###################################################################
# Project name: Gazorpazorp calculator
# File: LibProcExpr.py
# Authors: Vilem Gottwald
# Description: Library for processing mathematical expression, given by GUI
#              this library uses mathematical functions from LibMath
###################################################################

import LibMath as math

##
# @file LibProcExpr.py
#
# @author Vilem Gottwald
#
# @brief Library for processing mathematical expression, given by GUI
# This library uses functions from LibMath library to solve mathematical expression given as a string.
#

##
# @brief Function that converts number in any format into the corresponding format
#
# @param num Number that is converted
#
# @return Number as float or integer, depending on it's value
def conv_to_num(num):
    if isinstance(num, str):
        num = float(num)

    if isinstance(num, int):
        return num
    elif isinstance(num, float):
        return int(num) if num.is_integer() else num
    else:
        raise TypeError("Error - wrong parameter type")

##
# @brief Function that separates string containing mathematical expression into individual items
#
# @param expression String that will be separated
#
# @return List containing expression items
def parse_expr(expression):
    operators_l = ["!", "^", "√", "*", "/", "%", "+", "-"]
    separated = list()
    number = True
    num_str = ""

    for char in expression:
        for op in operators_l:
            if char == op:
                number = False
                break

        if number:
            num_str += char
        else:
            if num_str != "":
                separated.append(num_str)
                num_str = ""
            separated.append(op)
            number =  True
    if num_str != "":
            separated.append(num_str)

    return separated

##
# @brief Function that solves parsed mathematical expression and returns result
#
# @param expression Mathematical expression to be solved (as a list of items)
#
# @return Result of the expression
def solve_expr(expression):
    operators = [["!"], ["^", "√"], ["*", "/", "%"], ["+", "-"]]
    parsed_expr = parse_expr(expression)

    if parsed_expr[0] == "+":
        del parsed_expr[0]
    elif parsed_expr[0] == "-":
        parsed_expr[1] = - conv_to_num(parsed_expr[1])
        del parsed_expr[0]

    for op_group in operators:
        i = 0
        while i < len(parsed_expr):
            if parsed_expr[i] in op_group:

                if parsed_expr[i] == "!" and i != 0:
                    operand = conv_to_num(parsed_expr[i - 1])
                    parsed_expr[i - 1] = (math.fact(operand))
                    del parsed_expr[i]
                    i -= 1

                elif parsed_expr[i] == "^" and i != 0:
                    base = conv_to_num(parsed_expr[i - 1])
                    exponent = conv_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (math.power(base, exponent))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "√" :

                    try:
                        degree = conv_to_num(parsed_expr[i - 1])
                        num = True
                    except ValueError:
                        num = False

                    if num and i != 0:
                        base = conv_to_num(parsed_expr[i + 1])
                        parsed_expr[i - 1] = (math.root(base, degree))
                        del parsed_expr[i + 1]
                        del parsed_expr[i]
                        i -= 2
                    else:
                        degree = 2
                        base = conv_to_num(parsed_expr[i + 1])
                        parsed_expr[i] = (math.root(base, degree))
                        del parsed_expr[i + 1]
                        i -= 1

                elif parsed_expr[i] == "*" and i != 0:
                    operand1 = conv_to_num(parsed_expr[i - 1])
                    operand2 = conv_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (math.mul(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "/" and i != 0 :
                    operand1 = conv_to_num(parsed_expr[i - 1])
                    operand2 = conv_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (math.div(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "%" and i != 0:
                    operand1 = conv_to_num(parsed_expr[i - 1])
                    operand2 = conv_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (math.mod(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "+" and i != 0:
                    if i == 0:
                        parsed_expr[i] = conv_to_num(parsed_expr[i + 1])
                        del parsed_expr[i + 1]
                        i -= 1
                    elif parsed_expr[i + 1] == "-":
                        parsed_expr[i] = "-"
                        del parsed_expr[i + 1]
                        i -= 1
                    elif parsed_expr[i + 1] == "+":
                        parsed_expr[i] = "+"
                        del parsed_expr[i + 1]
                        i -= 1
                    else:
                        operand1 = conv_to_num(parsed_expr[i - 1])
                        operand2 = conv_to_num(parsed_expr[i + 1])
                        parsed_expr[i - 1] = (math.add(operand1, operand2))
                        del parsed_expr[i + 1]
                        del parsed_expr[i]
                        i -= 2

                elif parsed_expr[i] == "-" and i != 0:
                    if i == 0:
                        parsed_expr[i] = - conv_to_num(parsed_expr[i + 1])
                        del parsed_expr[i + 1]
                        i -= 1
                    elif parsed_expr[i + 1] == "-":
                        parsed_expr[i] = "+"
                        del parsed_expr[i + 1]
                        i -= 1
                    elif parsed_expr[i + 1] == "+":
                        parsed_expr[i] = "-"
                        del parsed_expr[i + 1]
                        i -= 1
                    else:
                        operand1 = conv_to_num(parsed_expr[i - 1])
                        operand2 = conv_to_num(parsed_expr[i + 1])
                        parsed_expr[i - 1] = (math.sub(operand1, operand2))
                        del parsed_expr[i + 1]
                        del parsed_expr[i]
                        i -= 2
            i += 1
    if len(parsed_expr) != 1:
        raise ValueError("Error - expression in wrong format")
    return conv_to_num(parsed_expr[0])

# End of file LibProcExpr.py
