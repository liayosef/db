import pickle
import os


class Database:
    def __init__(self, file_path='database.pkl'):
        self.file_path = file_path
        self._data = self._load_data()

    def _load_data(self):
        """Loads the database from a file if it exists, otherwise returns an empty dictionary."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as f:
                return pickle.load(f)
        return {}

    def _save_data(self):
        """Saves the database to a file."""
        with open(self.file_path, 'wb') as f:
            pickle.dump(self._data, f)

    def value_set(self, key, val):
        """Inserts a value with the given key, returns True on success, False otherwise."""
        self._data[key] = val
        self._save_data()
        return True

    def value_get(self, key):
        """Returns the value mapped to the key, or None if it doesn't exist."""
        return self._data.get(key, None)

    def value_delete(self, key):
        """Deletes a value mapped to the key and returns it, or None if the key doesn't exist."""
        if key in self._data:
            val = self._data.pop(key)
            self._save_data()
            return val
        return None
