import threading
from datetime import datetime


class FileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, file_name: str):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._file_name = file_name
                with open(cls._instance._file_name, 'a') as file:
                    file.write("File Audit Log Initialized\n")
                    file.write(f"Log started: {datetime.now()}\n\n")
        return cls._instance

    def log_message(self, message: str):
        timestamp_format = "%Y-%m-%d %H:%M:%S"
        with self._lock:
            with open(self._file_name, 'a') as file:
                file.write(f"{datetime.now().strftime(timestamp_format)}: {message}\n")

def test_file_audit_manager():
    audit_manager = FileAuditManager("audit_log.txt")
    audit_manager.log_message("This is a test message.")
    audit_manager.log_message("Another test message.")

if __name__ == '__main__':
    # Create multiple threads to test thread safety
    threads = []
    for i in range(5):
        thread = threading.Thread(target=test_file_audit_manager)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()