"""
Test suite for utils.py functions.
"""

import pytest
from utils import suma, resta, mayuscula_a_minuscula


class TestSuma:
    """Test cases for the suma function."""
    
    def test_suma_two_numbers(self):
        """Test suma with two numbers."""
        result = suma(5, 3)
        assert result == 8.0
    
    def test_suma_multiple_numbers(self):
        """Test suma with multiple numbers."""
        result = suma(1, 2, 3, 4, 5)
        assert result == 15.0
    
    def test_suma_single_number(self):
        """Test suma with a single number."""
        result = suma(7)
        assert result == 7.0
    
    def test_suma_no_numbers(self):
        """Test suma with no arguments."""
        result = suma()
        assert result == 0.0
    
    def test_suma_with_strings(self):
        """Test suma with string numbers."""
        result = suma("5", "3")
        assert result == 8.0
    
    def test_suma_with_floats(self):
        """Test suma with float numbers."""
        result = suma(2.5, 3.7)
        assert result == 6.2
    
    def test_suma_with_negative_numbers(self):
        """Test suma with negative numbers."""
        result = suma(-5, 3, -2)
        assert result == -4.0
    
    def test_suma_with_zero(self):
        """Test suma with zeros."""
        result = suma(0, 0, 5)
        assert result == 5.0
    
    def test_suma_large_numbers(self):
        """Test suma with large numbers."""
        result = suma(1000000, 2000000)
        assert result == 3000000.0
    
    def test_suma_invalid_string(self):
        """Test suma with invalid string that cannot be converted to float."""
        with pytest.raises(ValueError):
            suma("abc")
    
    def test_suma_mixed_valid_types(self):
        """Test suma with mixed valid types."""
        result = suma(1, "2", 3.0)
        assert result == 6.0


class TestResta:
    """Test cases for the resta function."""
    
    def test_resta_two_numbers(self):
        """Test resta with two numbers."""
        result = resta(10, 3)
        assert result == 7.0
    
    def test_resta_multiple_numbers(self):
        """Test resta with multiple numbers (10 - 2 - 3 - 1)."""
        result = resta(10, 2, 3, 1)
        assert result == 4.0
    
    def test_resta_single_number(self):
        """Test resta with a single number."""
        result = resta(7)
        assert result == 7.0
    
    def test_resta_with_strings(self):
        """Test resta with string numbers."""
        result = resta("10", "3")
        assert result == 7.0
    
    def test_resta_with_floats(self):
        """Test resta with float numbers."""
        result = resta(7.5, 2.3)
        assert result == pytest.approx(5.2, rel=1e-9)
    
    def test_resta_with_negative_numbers(self):
        """Test resta with negative numbers."""
        result = resta(-5, 3)
        assert result == -8.0
    
    def test_resta_negative_from_positive(self):
        """Test resta subtracting negative (double negative)."""
        result = resta(5, -3)
        assert result == 8.0
    
    def test_resta_with_zero(self):
        """Test resta with zeros."""
        result = resta(0, 5)
        assert result == -5.0
    
    def test_resta_zero_from_number(self):
        """Test subtracting zero from number."""
        result = resta(5, 0)
        assert result == 5.0
    
    def test_resta_large_numbers(self):
        """Test resta with large numbers."""
        result = resta(3000000, 1000000)
        assert result == 2000000.0
    
    def test_resta_invalid_string(self):
        """Test resta with invalid string that cannot be converted to float."""
        with pytest.raises(ValueError):
            resta("abc")
    
    def test_resta_sequential_subtraction(self):
        """Test resta with sequential subtraction (100 - 10 - 20 - 30)."""
        result = resta(100, 10, 20, 30)
        assert result == 40.0


class TestMayusculaAMinuscula:
    """Test cases for the mayuscula_a_minuscula function."""
    
    def test_single_uppercase_string(self):
        """Test with a single uppercase string."""
        result = mayuscula_a_minuscula("HELLO")
        assert result == ["hello"]
    
    def test_single_mixed_case_string(self):
        """Test with a single mixed case string."""
        result = mayuscula_a_minuscula("HeLLo WoRLd")
        assert result == ["hello world"]
    
    def test_multiple_strings(self):
        """Test with multiple strings."""
        result = mayuscula_a_minuscula("HELLO", "WORLD", "TEST")
        assert result == ["hello", "world", "test"]
    
    def test_already_lowercase_string(self):
        """Test with already lowercase string."""
        result = mayuscula_a_minuscula("hello")
        assert result == ["hello"]
    
    def test_empty_string(self):
        """Test with empty string."""
        result = mayuscula_a_minuscula("")
        assert result == [""]
    
    def test_string_with_numbers(self):
        """Test with string containing numbers."""
        result = mayuscula_a_minuscula("HELLO123")
        assert result == ["hello123"]
    
    def test_string_with_special_characters(self):
        """Test with string containing special characters."""
        result = mayuscula_a_minuscula("HELLO@WORLD!")
        assert result == ["hello@world!"]
    
    def test_mixed_types_converted_to_string(self):
        """Test with non-string types that get converted."""
        result = mayuscula_a_minuscula(123, True, None)
        assert result == ["123", "true", "none"]
    
    def test_no_arguments(self):
        """Test with no arguments."""
        result = mayuscula_a_minuscula()
        assert result == []
    
    def test_unicode_characters(self):
        """Test with unicode characters."""
        result = mayuscula_a_minuscula("ÑOÑO", "CAFÉ")
        assert result == ["ñoño", "café"]
    
    def test_whitespace_only(self):
        """Test with whitespace-only string."""
        result = mayuscula_a_minuscula("   ")
        assert result == ["   "]
    
    def test_multiple_mixed_case_strings(self):
        """Test with multiple mixed case strings."""
        result = mayuscula_a_minuscula("PyThOn", "JaVaScRiPt", "HTML")
        assert result == ["python", "javascript", "html"]


class TestUtilsFunctionIntegration:
    """Integration tests for utils functions."""
    
    def test_suma_and_resta_combination(self):
        """Test combining suma and resta operations."""
        suma_result = suma(10, 5, 3)
        resta_result = resta(suma_result, 8)
        assert resta_result == 10.0
    
    def test_all_functions_with_edge_cases(self):
        """Test all functions with various edge cases."""
        # Test suma with edge case
        suma_result = suma(0.1, 0.2)
        assert suma_result == pytest.approx(0.3, rel=1e-9)
        
        # Test resta with edge case
        resta_result = resta(1.0, 0.9)
        assert resta_result == pytest.approx(0.1, rel=1e-9)
        
        # Test mayuscula_a_minuscula with edge case
        text_result = mayuscula_a_minuscula("MiXeD cAsE 123!")
        assert text_result == ["mixed case 123!"]


# Fixtures for testing
@pytest.fixture
def sample_numbers():
    """Provide sample numbers for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_strings():
    """Provide sample strings for testing."""
    return ["HELLO", "WORLD", "PYTHON", "TEST"]


@pytest.fixture
def mixed_case_strings():
    """Provide mixed case strings for testing."""
    return ["HeLLo", "WoRLd", "PyThOn", "TeSt"]


class TestUtilsWithFixtures:
    """Test utils functions using pytest fixtures."""
    
    def test_suma_with_fixture(self, sample_numbers):
        """Test suma using fixture data."""
        result = suma(*sample_numbers)
        assert result == 15.0
    
    def test_resta_with_fixture(self, sample_numbers):
        """Test resta using fixture data (1-2-3-4-5)."""
        result = resta(*sample_numbers)
        assert result == -13.0
    
    def test_mayuscula_a_minuscula_with_fixture(self, sample_strings):
        """Test mayuscula_a_minuscula using fixture data."""
        result = mayuscula_a_minuscula(*sample_strings)
        expected = [s.lower() for s in sample_strings]
        assert result == expected
    
    def test_mixed_case_conversion(self, mixed_case_strings):
        """Test conversion with mixed case fixture."""
        result = mayuscula_a_minuscula(*mixed_case_strings)
        expected = ["hello", "world", "python", "test"]
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])