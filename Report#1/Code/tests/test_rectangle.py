from area.rectangle import Rectangle, InvalidEdgeType, ZeroEdgeError
import pytest


@pytest.fixture
def rectangle():
    return Rectangle(height=5, width=3)

# @pytest.fixture
# def float_rectangle():
#     return Rectangle(height=2.5, width=4.5)


def test_constructor(rectangle):
    assert isinstance(rectangle, Rectangle)


def test_constructor_with_float_edges():
    try:
        rectangle = Rectangle(2.5, 4.5)
    except Exception as e:
        pytest.fail("should not throw exception")
    else:
        assert True


def test_constructor_with_string_edges_should_throw_exception():
    try:
        rectangle = Rectangle(12, "Hello")
    except InvalidEdgeType as e:
        assert True
    else:
        pytest.fail("expected error but got none")


def test_rectangle_with_0_width_should_not_be_possible():
    try:
        rectangle = Rectangle(height=4, width=0)
    except ZeroDivisionError as e:
        assert isinstance(e, Exception)
    except ZeroEdgeError as e:
        assert isinstance(e, Exception)
    else:
        pytest.fail("Expected error but found none")


def test_rectangle_with_0_height_should_not_be_possible():
    try:
        rectangle = Rectangle(height=0, width=4)
    except ZeroDivisionError as e:
        assert isinstance(e, Exception)
    except ZeroEdgeError as e:
        assert isinstance(e, Exception)
    else:
        pytest.fail("Expected error but found none")


def test_compute_area_with_equal_edges():
    rectangle = Rectangle(height=2, width=2)
    assert rectangle.compute_area() == 4


def test_compute_area_with_integer_edges(rectangle):
    assert rectangle.compute_area() == 15


def test_compute_area_with_float_edges():
    rectangle = Rectangle(2.5, 4.5)
    assert rectangle.compute_area() == 2.5*4.5

