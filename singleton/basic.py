class NumberGenerator:
    _instance = None
    _current_number = 0
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_next_number(self):
        self._current_number += 1
        return self._current_number


# Example usage
if __name__ == '__main__':
    generator1 = NumberGenerator()
    generator2 = NumberGenerator()

    print(generator1.get_next_number())  # Output: 1
    print(generator2.get_next_number())  # Output: 2

    print(generator1 is generator2)  # Output: True
    print(generator1._current_number)  # Output: 2
    print(generator2._current_number)  # Output: 2