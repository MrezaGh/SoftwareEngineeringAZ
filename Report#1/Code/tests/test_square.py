from area.rectangle import InvalidEdgeType, ZeroEdgeError
from area.square import Square, UnequalEdgesError
import pytest


@pytest.fixture
def square():
    return Square(5, 5)


def test_constructor(square):
    assert isinstance(square, Square)


def test_constructor_with_one_input():
    try:
        square = Square(4)
        assert square.height == 4
        assert square.width == 4
    except:
        pytest.fail("should not throw exception when there is 1 input")


def test_constructor_with_two_different_inputs():
    try:
        square = Square(4, 6)
    except UnequalEdgesError as e:
        assert isinstance(e, Exception)
    else:
        pytest.fail("Error expected but none found")


def test_constructor_with_float_edges():
    try:
        rectangle = Square(2.5)
    except Exception as e:
        pytest.fail("should not throw exception")
    else:
        assert True


def test_constructor_with_string_edges_should_throw_exception():
    try:
        square = Square("Hello")
    except InvalidEdgeType as e:
        assert True
    else:
        pytest.fail("expected error but got none")


def test_square_with_0_edge_should_not_be_possible():
    try:
        square = Square(0)
    except ZeroEdgeError as e:
        assert isinstance(e, Exception)
    else:
        pytest.fail("Expected error but found none")


def test_compute_area_with_integer_edges(square):
    assert square.compute_area() == 25


def test_compute_area_with_float_edges():
    square = Square(2.5)
    assert square.compute_area() == 2.5*2.5


# test set and get
def test_get_height(square):
    assert square.get_height() == 5


def test_get_width(square):
    assert square.get_width() == 5


def test_set_height_with_valid_height(square):
    assert square.get_height() == 5
    square.set_height(12)
    assert square.get_height() == 12
    assert square.get_width() == 12
    square.set_height(1.1)
    assert square.get_height() == 1.1
    assert square.get_width() == 1.1


def test_set_height_with_invalid_input(square):
    assert square.get_height() == 5
    invalid_heights = ["Moo!", 0, -2, "cool"]
    for invalid_height in invalid_heights:
        try:
            square.set_height(invalid_height)
        except (InvalidEdgeType, ZeroEdgeError) as e:
            assert isinstance(e, Exception)
        else:
            pytest.fail("Error expected but none found")


    def test_set_width_with_valid_width(square):
        assert square.get_width() == 5
        square.set_width(10)
        assert square.get_width() == 10
        assert square.get_height() == 10
        square.set_width(2.2)
        assert square.get_width() == 2.2
        assert square.get_height() == 2.2


def test_set_width_with_invalid_input(square):
    assert square.get_width() == 5
    invalid_widths = ["Moo!", 0, -2, "cool"]
    for invalid_width in invalid_widths:
        try:
            square.set_width(invalid_width)
        except (InvalidEdgeType, ZeroEdgeError) as e:
            assert isinstance(e, Exception)
        else:
            pytest.fail("Error expected but none found")



