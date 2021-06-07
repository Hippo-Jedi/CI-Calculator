import calculator


class TestCalc:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_sub(self):
        assert 5 == calculator.sub(10, 5)

    def test_div(self):
        assert 2 == calculator.div(10, 5)

    def test_mult(self):
        assert 20 == calculator.mult(10, 2)
