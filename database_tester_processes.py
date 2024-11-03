import multiprocessing
import time
import random
from synchronized_database import SynchronizedDatabase


class DatabaseTesterProcesses:
    def __init__(self, synchronized_database):
        self.synchronized_database = synchronized_database

    def read_from_db(self, process_id):
        """Function for a process to read from the database."""
        print(f"Process {process_id} attempting to read.")
        value = self.synchronized_database.value_get('test_key')
        print(f"Process {process_id} read value: {value}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate time spent reading

    def write_to_db(self, process_id, value):
        """Function for a process to write to the database."""
        print(f"Process {process_id} attempting to write value: {value}")
        self.synchronized_database.value_set('test_key', value)
        print(f"Process {process_id} wrote value: {value}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate time spent writing

    def start_test(self):
        """Sets up and starts processes for testing the SynchronizedDatabase."""
        processes = []

        # Create 10 processes for reading
        for i in range(10):
            p = multiprocessing.Process(target=self.read_from_db, args=(i,))
            processes.append(p)

        # Create 5 processes for writing
        for i in range(5):
            p = multiprocessing.Process(target=self.write_to_db, args=(i + 10, f"value_{i}"))
            processes.append(p)

        # Start all processes
        for p in processes:
            p.start()

        # Wait for all processes to complete
        for p in processes:
            p.join()

        print("All processes have finished execution.")
