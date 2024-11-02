class ValidateISBN:
    ISBN_SHORT = 10
    ISBN_LONG = 13
    ISBN_SHORT_VALIDATOR = 11
    ISBN_LONG_VALIDATOR = 10

    def check_isbn(self, isbn: str) -> bool:
        if len(isbn) == self.ISBN_SHORT or len(isbn) == self.ISBN_LONG:
            if len(isbn) == self.ISBN_LONG:
                return self.check_isbn_thirteen_digits(isbn)
            else:
                return self.check_isbn_ten_digits(isbn)
        else:
            raise ValueError("ISBN number should have length of 10 or 13")

    def check_isbn_ten_digits(self, isbn: str) -> bool:
        total = 0
        for i in range(self.ISBN_SHORT):
            if not isbn[i].isdigit():
                if i == 9 and isbn[i] == 'X':
                    total += 10
                else:
                    raise ValueError("ISBN numbers can only have digits.")
            else:
                total += int(isbn[i]) * (self.ISBN_SHORT - i)
        
        return total % self.ISBN_SHORT_VALIDATOR == 0

    def check_isbn_thirteen_digits(self, isbn: str) -> bool:
        total = 0
        for i in range(self.ISBN_LONG):
            if isbn[i].isdigit():
                if i % 2 == 0:
                    total += int(isbn[i]) * 1
                else:
                    total += int(isbn[i]) * 3
            else:
                raise ValueError("ISBN numbers can only have digits.")
        
        return total % self.ISBN_LONG_VALIDATOR == 0