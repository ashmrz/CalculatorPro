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
