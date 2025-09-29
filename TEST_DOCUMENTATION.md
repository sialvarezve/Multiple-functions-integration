# Test Documentation

This document provides an overview of the comprehensive test suite for the Multiple Functions Integration project.

## Test Files

### `test_utils.py`
Tests for all functions in the `utils.py` module:

#### TestSuma Class
- **test_suma_two_numbers**: Tests basic addition with two numbers
- **test_suma_multiple_numbers**: Tests addition with multiple arguments
- **test_suma_single_number**: Tests edge case with single argument
- **test_suma_no_numbers**: Tests behavior with no arguments (returns 0)
- **test_suma_with_strings**: Tests numeric strings conversion
- **test_suma_with_floats**: Tests floating point arithmetic
- **test_suma_with_negative_numbers**: Tests negative number handling
- **test_suma_with_zero**: Tests zero value handling
- **test_suma_large_numbers**: Tests with large numeric values
- **test_suma_invalid_string**: Tests error handling for invalid strings
- **test_suma_mixed_valid_types**: Tests mixed int/string/float inputs

#### TestResta Class  
- **test_resta_two_numbers**: Tests basic subtraction with two numbers
- **test_resta_multiple_numbers**: Tests sequential subtraction (a-b-c-d)
- **test_resta_single_number**: Tests edge case with single argument
- **test_resta_with_strings**: Tests numeric strings conversion
- **test_resta_with_floats**: Tests floating point subtraction with precision
- **test_resta_with_negative_numbers**: Tests negative number subtraction
- **test_resta_negative_from_positive**: Tests double negative scenarios
- **test_resta_with_zero**: Tests zero value handling
- **test_resta_zero_from_number**: Tests subtracting zero
- **test_resta_large_numbers**: Tests with large numeric values
- **test_resta_invalid_string**: Tests error handling for invalid strings
- **test_resta_sequential_subtraction**: Tests complex sequential operations

#### TestMayusculaAMinuscula Class
- **test_single_uppercase_string**: Tests basic uppercase to lowercase conversion
- **test_single_mixed_case_string**: Tests mixed case conversion
- **test_multiple_strings**: Tests multiple string arguments
- **test_already_lowercase_string**: Tests already lowercase strings
- **test_empty_string**: Tests empty string handling
- **test_string_with_numbers**: Tests strings containing numbers
- **test_string_with_special_characters**: Tests special character preservation
- **test_mixed_types_converted_to_string**: Tests non-string type conversion
- **test_no_arguments**: Tests behavior with no arguments
- **test_unicode_characters**: Tests Unicode character handling (ñ, é, etc.)
- **test_whitespace_only**: Tests whitespace-only strings
- **test_multiple_mixed_case_strings**: Tests multiple mixed case inputs

#### TestUtilsFunctionIntegration Class
- **test_suma_and_resta_combination**: Tests combining suma and resta operations
- **test_all_functions_with_edge_cases**: Tests all functions with edge cases

#### TestUtilsWithFixtures Class
- **test_suma_with_fixture**: Tests suma using pytest fixtures
- **test_resta_with_fixture**: Tests resta using pytest fixtures
- **test_mayuscula_a_minuscula_with_fixture**: Tests text conversion using fixtures
- **test_mixed_case_conversion**: Tests mixed case conversion with fixtures

### `test_main.py`
Tests for the main orchestration function in `main.py`:

#### TestMainFunction Class
- **test_main_no_function_provided**: Tests behavior when no function is specified
- **test_main_function_not_found**: Tests behavior when function doesn't exist
- **test_main_params_not_dict**: Tests error handling for invalid params type
- **test_main_successful_suma_call**: Tests successful suma function execution
- **test_main_successful_resta_call**: Tests successful resta function execution  
- **test_main_successful_mayuscula_a_minuscula_call**: Tests successful text conversion
- **test_main_with_exception**: Tests error handling when utils function raises exception
- **test_main_with_empty_params**: Tests behavior with empty parameters dictionary
- **test_main_with_multiple_params**: Tests behavior with multiple parameters

#### TestMainInteractiveLoop Class
- **test_interactive_loop_exit_immediately**: Tests immediate exit from interactive mode
- **test_interactive_loop_with_function_call**: Tests complete interactive flow
- **test_interactive_loop_exit_on_var1**: Tests exit during first parameter input
- **test_interactive_loop_exit_on_var2**: Tests exit during second parameter input

#### TestMainEdgeCases Class
- **test_main_with_none_params**: Tests behavior when params is None
- **test_main_case_insensitive_function_lookup**: Tests case sensitivity of function names
- **test_main_with_extra_params**: Tests behavior with more parameters than expected
- **test_main_function_with_no_print_side_effect**: Tests function execution without side effects

#### TestMainIntegrationWithUtils Class
- **test_integration_suma_complete_flow**: Tests complete integration with suma
- **test_integration_text_conversion_complete_flow**: Tests complete text conversion flow
- **test_integration_error_handling_invalid_conversion**: Tests error handling integration

#### Parametrized Tests
- **test_main_parametrized**: Tests multiple scenarios using pytest parametrization

## Test Coverage Summary

### Functions Tested
- ✅ `utils.suma()` - 11 test cases
- ✅ `utils.resta()` - 12 test cases  
- ✅ `utils.mayuscula_a_minuscula()` - 12 test cases
- ✅ `main.main()` - 20 test cases
- ✅ Interactive loop logic - 4 test cases

### Test Categories
- **Unit Tests**: 58 tests
- **Integration Tests**: 6 tests
- **Edge Case Tests**: Multiple edge cases per function
- **Error Handling Tests**: Exception and validation testing
- **Parametrized Tests**: 3 parametrized scenarios

### Total Test Count: **64 tests**

## Test Features Used

### Python Testing Tools
- **pytest**: Main testing framework
- **unittest.mock**: Mocking for isolation and control
- **pytest.fixture**: Reusable test data
- **pytest.parametrize**: Data-driven testing
- **pytest.approx**: Floating point comparison

### Testing Patterns
- **Arrange-Act-Assert**: Clear test structure
- **Mocking**: Isolation of external dependencies
- **Fixtures**: Reusable test data and setup
- **Edge Case Testing**: Boundary value analysis
- **Error Testing**: Exception handling validation
- **Integration Testing**: Component interaction testing

### Code Coverage
The test suite provides comprehensive coverage including:
- All function paths and branches
- Error conditions and exception handling  
- Edge cases and boundary values
- Integration between components
- User input simulation and validation

## Running the Tests

```bash
# Run all tests
python3 -m pytest test_utils.py test_main.py -v

# Run with coverage
python3 -m pytest test_utils.py test_main.py --cov=. --cov-report=html

# Run specific test class
python3 -m pytest test_utils.py::TestSuma -v

# Run specific test method
python3 -m pytest test_main.py::TestMainFunction::test_main_successful_suma_call -v
```

## Test Results
All 64 tests pass successfully, ensuring:
- Function correctness across all scenarios
- Proper error handling and validation
- Integration between main.py and utils.py
- Edge case handling and robustness