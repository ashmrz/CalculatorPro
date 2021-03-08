from errors import Errors
import math


class Calculator:
    """
    The main class for our computation logics.
    """

    def __init__(self, name):
        """
        The constructor method for the calculator class.

        :param name: str
            The name of this instance of the calculator.
        """
        self.name = name

    def compute_add(self, op1, op2):
        """
        This function return sum of its inputs

        :param op1: float
            The first operand
        :param op2: float
            The second operand

        :return : float
            return the sum of two operands
        """
        return op1 + op2

    def compute_sub(self, op1, op2):
        """
        The computer method for subtract operation.

        :param op1: float
            The first operand
        :param op2: float
            The second operand
        :return : float
            return the subtraction of two operands
        """
        return op1 - op2

    def compute_div(self, op1, op2):
        """
        The computer method for divition operation.

        :param op1: float
            The first operand
        :param op2: float
            The second operand
        :return : float
            return the division of two operands
        """
        if op2 == 0:
            return Errors.DIV_BY_ZERO
        return op1 / op2

    def compute_mul(self, op1, op2):
        """
        The computer method for multiplication operation.

        :param op1: float
            The first operand
        :param op2: float
            The second operand
        :return : float
            return the multiplication of two operands
        """
        return op1 * op2

    def compute_sqrt(self, op1):
        """
        The computer method for multiplication operation.

        :param op1: float
            The first operand
        :return : float
            return the square root of the input
        """
        return math.sqrt(op1)
