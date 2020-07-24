from area.rectangle import Rectangle, InvalidEdgeType, ZeroEdgeError
import pytest


@pytest.fixture
def rectangle():
    return Rectangle(height=5, width=3)


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


# test set and get
def test_get_height(rectangle):
    assert rectangle.get_height() == 5


def test_get_width(rectangle):
    assert rectangle.get_width() == 3


def test_set_height_with_valid_height(rectangle):
    assert rectangle.get_height() == 5
    rectangle.set_height(12)
    assert rectangle.get_height() == 12
    rectangle.set_height(1.1)
    assert rectangle.get_height() == 1.1


def test_set_height_with_invalid_input(rectangle):
    assert rectangle.get_height() == 5
    invalid_heights = ["Moo!", 0, -2, "cool"]
    for invalid_height in invalid_heights:
        try:
            rectangle.set_height(invalid_height)
        except (InvalidEdgeType, ZeroEdgeError) as e:
            assert isinstance(e, Exception)
        else:
            pytest.fail("Error expected but none found")


def test_get_width_with_valid_width(rectangle):
    assert rectangle.get_width() == 3
    rectangle.set_width(10)
    assert rectangle.get_width() == 10
    rectangle.set_width(2.2)
    assert rectangle.get_width() == 2.2


def test_set_width_with_invalid_input(rectangle):
    assert rectangle.get_width() == 3
    invalid_widths = ["Moo!", 0, -2, "cool"]
    for invalid_width in invalid_widths:
        try:
            rectangle.set_width(invalid_width)
        except (InvalidEdgeType, ZeroEdgeError) as e:
            assert isinstance(e, Exception)
        else:
            pytest.fail("Error expected but none found")



