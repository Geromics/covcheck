
import json

# TODO: Add logging?


class Individual:
    def __init__(self, id, age=None, snps=None, **kwargs):
        self.id = id
        self.age = age
        self.snps = snps

        if kwargs:
            self.extra = kwargs

    def __str__(self):
        return json.dumps(self.__dict__)

    def to_file(self, filename=None, indent=4):
        """Write an individual to file."""
        if filename is None:
            filename = f"tests/data/{self.id}.json"

        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=indent)

    @classmethod
    def from_file(cls, filename):
        """Create an individual from a simple JSON file."""
        with open(filename, 'r') as f:
            s = f.read()
        j = json.loads(s)
        return cls(**j)

    @classmethod
    def from_api(cls, url):
        """TODO: Create an individual from an API call."""
        pass


def _get_mock_individuals_for_testing(filename=None):
    """Convenience function for unit testing."""
    if filename is None:
        filename = 'tests/data/mock_individuals.json'

    with open(filename, 'r') as file:
        individuals = json.loads(file.read())

        for id, i in individuals.items():
            individuals[id] = Individual(id=id, **i)

    return individuals


if __name__ == '__main__':
    """Just for fun..."""
    for i in _get_mock_individuals_for_testing():
        print(i)
