from function import number_to_month, validate_number
import pytest


@pytest.mark.code
def test_result_jan_1():
    input = 1
    expected_result = "january"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_feb_2():
    input = 2
    expected_result = "february"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_mar_3():
    input = 3
    expected_result = "march"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_apr_4():
    input = 4
    expected_result = "april"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_may_5():
    input = 5
    expected_result = "may"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_jun_6():
    input = 6
    expected_result = "june"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_jul_7():
    input = 7
    expected_result = "july"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_aug_8():
    input = 8
    expected_result = "august"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_sep_9():
    input = 9
    expected_result = "september"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_oct_10():
    input = 10
    expected_result = "october"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_nov_11():
    input = 11
    expected_result = "november"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code
def test_result_dec_12():
    input = 12
    expected_result = "december"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_0():
    input = 0
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_13():
    input = 13
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_minus_10():
    input = -10
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_22():
    input = 22
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_input_integer_input_1_1():
    input = 1.1
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_13_1():
    input = 13.1
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_input_char_input_a():
    input = "a"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_input_char_input_shap():
    input = "#"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_in_of_range_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_in_of_range_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_0_5():
    input = 0.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_out_of_range_input_minus_1_5():
    input = -1.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_result_input_integer_input_1_5():
    input = 1.5
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result
