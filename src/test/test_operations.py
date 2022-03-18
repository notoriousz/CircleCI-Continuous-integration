import pytest
from ..main.Operations import Operations


class TestOperations:

    #Sum Operation
    @pytest.mark.parametrize('number_one, number_two', [(0, 1)])
    def test_operation_sum(self, number_one, number_two):
        calc = Operations()
        assert calc.sum_operation(number_one, number_two) == 1


    # Sub Operation
    @pytest.mark.parametrize('number_one, number_two', [(3, 1)])
    def test_operation_sub(self, number_one, number_two):
        calc = Operations()
        assert calc.sub_operation(number_one, number_two) == 2


    # Mult Operation
    @pytest.mark.parametrize('number_one, number_two', [(3, 1)])
    def test_operation_mult(self, number_one, number_two):
        calc = Operations()
        assert calc.mult_operation(number_one, number_two) == 3


    # Div Operation
    @pytest.mark.parametrize('number_one, number_two', [(8, 2)])
    def test_operation_div(self, number_one, number_two):
        calc = Operations()
        assert calc.div_operation(number_one, number_two) == 4
    