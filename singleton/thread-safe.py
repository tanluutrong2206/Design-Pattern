import threading


class NumberGenerator:
    _lock = threading.Lock()
    _instance = None
    _current_number = 0
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_next_number(self):
        with self._lock:
            number = self._current_number
            self._current_number += 1
        return number

def test_singleton_thread_safe():
    generator = NumberGenerator()

    print(f"Generated number is: {generator.get_next_number()}")

if __name__ == '__main__':
    # Create multiple threads to test thread safety
    threads = []
    for i in range(5):
        thread = threading.Thread(target=test_singleton_thread_safe)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()