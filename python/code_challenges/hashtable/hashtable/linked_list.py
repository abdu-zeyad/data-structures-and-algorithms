MAX_HASH_TABLE_SIZE = 4096


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        hash('key')

    def __getitem__(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        return None if kv is None else kv[1]

    def __setitem__(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ')
                 for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)


# Create a hash table
table = HashTable()
# Insert some key-value pairs
table['a'] = 1
table['b'] = 34
# Retrieve the inserted values
table['a'] == 1 and table['b'] == 34
# Update a value
table['a'] = 99
# Check the updated value
table['a'] == 99
# Get a list of key-value pairs
list(table) == [('a', 99), ('b', 34)]
