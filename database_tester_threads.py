import threading
import time
import random
from synchronized_database import SynchronizedDatabase


class DatabaseTesterThreads:
    def __init__(self, synchronized_database):
        self.synchronized_database = synchronized_database
        self.threads = []

    def read_from_db(self, thread_id):
        """Function for a thread to read from the database."""
        print(f"Thread {thread_id} attempting to read.")
        value = self.synchronized_database.value_get('test_key')
        print(f"Thread {thread_id} read value: {value}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate time spent reading

    def write_to_db(self, thread_id, value):
        """Function for a thread to write to the database."""
        print(f"Thread {thread_id} attempting to write value: {value}")
        self.synchronized_database.value_set('test_key', value)
        print(f"Thread {thread_id} wrote value: {value}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate time spent writing

    def start_test(self):
        """Sets up and starts threads for testing the SynchronizedDatabase."""
        # Create 10 threads for reading
        for i in range(10):
            t = threading.Thread(target=self.read_from_db, args=(i,))
            self.threads.append(t)

        # Create 5 threads for writing
        for i in range(5):
            t = threading.Thread(target=self.write_to_db, args=(i + 10, f"value_{i}"))
            self.threads.append(t)

        # Start all threads
        for t in self.threads:
            t.start()

        # Wait for all threads to complete
        for t in self.threads:
            t.join()

        print("All threads have finished execution.")
