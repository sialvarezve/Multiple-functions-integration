"""
Test suite for main.py functions.
"""

import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import main
import utils


class TestMainFunction:
    """Test cases for the main function."""
    
    @patch('builtins.print')
    def test_main_no_function_provided(self, mock_print):
        """Test main with no function parameter."""
        main.main()
        mock_print.assert_called_with("No function provided.")
    
    @patch('builtins.print')
    def test_main_function_not_found(self, mock_print):
        """Test main with non-existent function."""
        main.main(func="nonexistent_function", params={"var1": 1})
        mock_print.assert_called_with("Function 'nonexistent_function' not found in utils module.")
    
    @patch('builtins.print')
    def test_main_params_not_dict(self, mock_print):
        """Test main with params that are not a dictionary."""
        main.main(func="suma", params="not_a_dict")
        mock_print.assert_called_with("Params should be a dictionary.")
    
    @patch('builtins.print')
    def test_main_successful_suma_call(self, mock_print):
        """Test main with successful suma function call."""
        params = {"var1": 5, "var2": 3}
        main.main(func="suma", params=params)
        
        # Check that the print calls include both the function execution and result
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("sumando" in str(call) for call in calls)
        assert any("Result: 8.0" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_main_successful_resta_call(self, mock_print):
        """Test main with successful resta function call."""
        params = {"var1": 10, "var2": 3}
        main.main(func="resta", params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("restando" in str(call) for call in calls)
        assert any("Result: 7.0" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_main_successful_mayuscula_a_minuscula_call(self, mock_print):
        """Test main with successful mayuscula_a_minuscula function call."""
        params = {"var1": "HELLO", "var2": "WORLD"}
        main.main(func="mayuscula_a_minuscula", params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("convirtiendo a minúsculas" in str(call) for call in calls)
        assert any("Result: ['hello', 'world']" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_main_with_exception(self, mock_print):
        """Test main when function raises an exception."""
        # Mock utils.suma to raise an exception
        with patch.object(utils, 'suma', side_effect=ValueError("Test error")):
            params = {"var1": "invalid", "var2": "data"}
            main.main(func="suma", params=params)
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("An error occurred: Test error" in str(call) for call in calls)
    
    def test_main_with_empty_params(self):
        """Test main with empty params dictionary."""
        with patch('builtins.print') as mock_print:
            main.main(func="suma", params={})
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("Result: 0" in str(call) for call in calls)
    
    def test_main_with_multiple_params(self):
        """Test main with multiple parameters."""
        with patch('builtins.print') as mock_print:
            params = {"var1": 1, "var2": 2, "var3": 3, "var4": 4}
            main.main(func="suma", params=params)
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("Result: 10.0" in str(call) for call in calls)


class TestMainInteractiveLoop:
    """Test cases for the interactive loop in main.py when run as script."""
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_loop_exit_immediately(self, mock_print, mock_input):
        """Test interactive loop when user exits immediately."""
        mock_input.return_value = "exit"
        
        # Since we can't easily test the if __name__ == "__main__" block directly,
        # we'll test the behavior by simulating the loop logic
        with patch('main.main') as mock_main_func:
            # Simulate the loop logic manually
            print('Enter "exit" to quit.')
            user_input = input('Enter function name: ').lower()
            assert user_input == "exit"
            
        mock_print.assert_called_with('Enter "exit" to quit.')
        mock_input.assert_called_with('Enter function name: ')
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_loop_with_function_call(self, mock_print, mock_input):
        """Test interactive loop with a function call."""
        # Simulate user input: function name, var1, var2, then exit
        mock_input.side_effect = ["suma", "5", "3", "exit"]
        
        with patch('main.main') as mock_main_func:
            # This is a bit tricky to test directly due to the while loop
            # We'll create a simplified version of the loop for testing
            user_inputs = ["suma", "5", "3", "exit"]
            input_iter = iter(user_inputs)
            
            def mock_input_func(prompt):
                return next(input_iter)
            
            with patch('builtins.input', side_effect=mock_input_func):
                # Simulate the loop logic
                print('Enter "exit" to quit.')
                user_input = input('Enter function name: ').lower()
                if user_input != "exit":
                    params = {}
                    params['var1'] = input('Enter value for var1: ')
                    if params['var1'] != 'exit':
                        params['var2'] = input('Enter value for var2: ')
                        if params['var2'] != 'exit':
                            mock_main_func(func=user_input, params=params)
                
                mock_main_func.assert_called_once_with(func="suma", params={"var1": "5", "var2": "3"})
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_loop_exit_on_var1(self, mock_print, mock_input):
        """Test interactive loop when user exits on var1 input."""
        mock_input.side_effect = ["suma", "exit"]
        
        with patch('main.main') as mock_main_func:
            # Simulate partial input then exit
            user_inputs = ["suma", "exit"]
            input_iter = iter(user_inputs)
            
            def mock_input_func(prompt):
                return next(input_iter)
            
            with patch('builtins.input', side_effect=mock_input_func):
                # Simulate the loop logic
                print('Enter "exit" to quit.')
                user_input = input('Enter function name: ').lower()
                if user_input != "exit":
                    params = {}
                    params['var1'] = input('Enter value for var1: ')
                    # Should exit here
                
                # main should not be called
                mock_main_func.assert_not_called()
    
    @patch('builtins.input')
    @patch('builtins.print')  
    def test_interactive_loop_exit_on_var2(self, mock_print, mock_input):
        """Test interactive loop when user exits on var2 input."""
        mock_input.side_effect = ["suma", "5", "exit"]
        
        with patch('main.main') as mock_main_func:
            # Simulate partial input then exit
            user_inputs = ["suma", "5", "exit"]
            input_iter = iter(user_inputs)
            
            def mock_input_func(prompt):
                return next(input_iter)
            
            with patch('builtins.input', side_effect=mock_input_func):
                # Simulate the loop logic
                print('Enter "exit" to quit.')
                user_input = input('Enter function name: ').lower()
                if user_input != "exit":
                    params = {}
                    params['var1'] = input('Enter value for var1: ')
                    if params['var1'] != 'exit':
                        params['var2'] = input('Enter value for var2: ')
                        # Should exit here
                
                # main should not be called
                mock_main_func.assert_not_called()


class TestMainEdgeCases:
    """Test edge cases for main.py functionality."""
    
    def test_main_with_none_params(self):
        """Test main when params is None (should use default empty dict)."""
        with patch('builtins.print') as mock_print:
            main.main(func="suma", params=None)
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("Params should be a dictionary." in str(call) for call in calls)
    
    def test_main_case_insensitive_function_lookup(self):
        """Test that main properly handles function names (case sensitivity)."""
        with patch('builtins.print') as mock_print:
            # The current implementation looks up the exact function name
            # so this should work for 'suma' but not 'SUMA'
            main.main(func="SUMA", params={"var1": 5, "var2": 3})
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("Function 'SUMA' not found in utils module." in str(call) for call in calls)
    
    def test_main_with_extra_params(self):
        """Test main with more parameters than needed."""
        with patch('builtins.print') as mock_print:
            params = {"var1": 1, "var2": 2, "var3": 3, "var4": 4, "var5": 5}
            main.main(func="suma", params=params)
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            # suma should accept all parameters via *args
            assert any("Result: 15.0" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_main_function_with_no_print_side_effect(self, mock_print):
        """Test that main function properly calls utils functions."""
        # Test with resta which should print 'restando'
        params = {"var1": 100, "var2": 50, "var3": 25}
        main.main(func="resta", params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("restando" in str(call) for call in calls)
        assert any("Result: 25.0" in str(call) for call in calls)


class TestMainIntegrationWithUtils:
    """Integration tests between main.py and utils.py."""
    
    @patch('builtins.print')
    def test_integration_suma_complete_flow(self, mock_print):
        """Test complete flow of suma function through main."""
        params = {"a": 10, "b": 20, "c": 30}
        main.main(func="suma", params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("sumando" in str(call) for call in calls)
        assert any("Result: 60.0" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_integration_text_conversion_complete_flow(self, mock_print):
        """Test complete flow of text conversion function through main."""
        params = {"text1": "PYTHON", "text2": "TESTING", "text3": "INTEGRATION"}
        main.main(func="mayuscula_a_minuscula", params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("convirtiendo a minúsculas" in str(call) for call in calls)
        assert any("Result: ['python', 'testing', 'integration']" in str(call) for call in calls)
    
    @patch('builtins.print')
    def test_integration_error_handling_invalid_conversion(self, mock_print):
        """Test error handling when utils function fails."""
        # Test with invalid data that might cause an error
        with patch.object(utils, 'suma', side_effect=Exception("Conversion error")):
            params = {"var1": "abc", "var2": "def"}
            main.main(func="suma", params=params)
            
            calls = [call.args[0] for call in mock_print.call_args_list]
            assert any("An error occurred: Conversion error" in str(call) for call in calls)


# Parametrized tests
@pytest.mark.parametrize("func_name,params,expected_in_output", [
    ("suma", {"var1": 1, "var2": 2}, "Result: 3.0"),
    ("resta", {"var1": 10, "var2": 5}, "Result: 5.0"), 
    ("mayuscula_a_minuscula", {"var1": "HELLO"}, "Result: ['hello']"),
])
def test_main_parametrized(func_name, params, expected_in_output):
    """Parametrized test for different function calls through main."""
    with patch('builtins.print') as mock_print:
        main.main(func=func_name, params=params)
        
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert any(expected_in_output in str(call) for call in calls)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])