import pytest
from validate_isbn import ValidateISBN  # Asegúrate de que el archivo con la clase ValidateISBN esté importado correctamente.

class TestValidateISBN:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.validate_isbn = ValidateISBN()

    def test_check_valid_isbn(self):
        result = self.validate_isbn.check_isbn("0140449116")
        assert result is True

    def test_check_invalid_isbn(self):
        result = self.validate_isbn.check_isbn("0140441927")
        assert result is False

    def test_check_isbn_length_ten_or_thirteen(self):
        with pytest.raises(ValueError, match="ISBN number should have length of 10 or 13"):
            self.validate_isbn.check_isbn("012345678")

    def test_check_isbn_numeric(self):
        with pytest.raises(ValueError, match="ISBN numbers can only have digits."):
            self.validate_isbn.check_isbn("helloworld")

    def test_check_contains_x(self):
        result = self.validate_isbn.check_isbn("080442957X")
        assert result is True

    def test_check_valid_thirteen_digit_isbn(self):
        result = self.validate_isbn.check_isbn("9780306406157")
        assert result is True