import threading
import multiprocessing
from database import FileDatabase


class SynchronizedDatabase(FileDatabase):
    def __init__(self, mode='threads', file_path='database.pkl'):
        super().__init__(file_path)
        self.mode = mode

        # Semaphore to control concurrent read access (up to 10)
        self.read_semaphore = (threading.Semaphore(10) if mode == 'threads'
                               else multiprocessing.Semaphore(10))

        # Lock to control exclusive write access
        self.write_lock = (threading.Lock() if mode == 'threads'
                           else multiprocessing.Lock())

    def value_set(self, key, val):
        """Inserts a value with exclusive write access."""
        with self.write_lock:  # Exclusive access for write
            return super().value_set(key, val)

    def value_get(self, key):
        """Allows up to 10 concurrent read accesses, but blocks if a write is in progress."""
        with self.write_lock:  # Prevents reading if a write is in progress
            with self.read_semaphore:  # Limited concurrent read access
                return super().value_get(key)

    def value_delete(self, key):
        """Deletes a value with exclusive write access."""
        with self.write_lock:  # Exclusive access for delete
            return super().value_delete(key)
