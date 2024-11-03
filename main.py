from synchronized_database import SynchronizedDatabase
from database_tester_threads import DatabaseTesterThreads
from database_tester_processes import DatabaseTesterProcesses


def run_thread_tests():
    """Run thread tests."""
    synchronized_database = SynchronizedDatabase(mode='threads')
    tester = DatabaseTesterThreads(synchronized_database)
    tester.start_test()


def run_process_tests():
    """Run process tests."""
    synchronized_database = SynchronizedDatabase(mode='processes')
    tester = DatabaseTesterProcesses(synchronized_database)
    tester.start_test()


if __name__ == "__main__":
    run_thread_tests()  # Uncomment to run thread tests
    # run_process_tests()  # Uncomment to run process tests