class Journal:
    """
    Journal is responsible ONLY for managing journal entries.
    It does NOT know how or where the data is stored.
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        """
        Adds a new journal entry.
        """
        self.count += 1
        self.entries.append(entry)
        return self.entries

    def remove_entry(self, pos):
        """
        Removes an entry by position.
        """
        del self.entries[pos]

    def __str__(self):
        """
        Returns all entries as a single formatted string.
        """
        return '\n'.join(self.entries)


class PersistenceManager:
    """
    PersistenceManager is responsible ONLY for saving/loading data.
    It does NOT manage journal logic.
    """

    @staticmethod
    def save_to_file(journal, filename):
        """
        Saves journal content to a file.
        """
        with open(filename, 'w') as file:
            file.write(str(journal))


# ==========================
# Usage
# ==========================

J = Journal()
J.add_entry('I love Python')
J.add_entry('I am good at Django')

print(f'Journal entries:\n{J}')

PersistenceManager.save_to_file(J, 'journal.txt')
