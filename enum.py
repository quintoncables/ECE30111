class enum:
    def __init__(self, *args):
        self._values = args
        for idx, name in enumerate(args):
            setattr(self, name, idx)

    def __contains__(self, value):
        return value in self._values

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "Enum" + str(tuple(self._values))
