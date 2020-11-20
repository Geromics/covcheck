import json


class Individual:
    def __init__(self, id, age=None, snps=None):
        self.id = id
        self.age = age
        self.snps = snps

    def __str__(self):
        return json.dumps(self.__dict__)

    def to_file(self, filename=None, indent=4):
        if filename is None:
            filename = f"tests/data/{self.id}.json"

        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=indent)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            s = f.read()
        j = json.loads(s)
        return cls(**j)

    @classmethod
    def from_api(cls, url):
        """TODO!"""
        pass


def write_mock_individuals():
    """Helper function to create some data for testing."""
    ids = get_mock_individual_ids()
    for id in ids:
        i = get_mock_individual(id)
        i.to_file()


def get_mock_individual(id='deadbeef'):
    return Individual(id, **_mock_individuals[id])


def get_mock_individual_ids():
    return _mock_individuals.keys()


_mock_individuals = {
    '6117323d': {
        'age': 93,
        'snps': {
            'rs1234': 'AA',
            'rs5678': 'GG',
            'rs12329760': 'CC',
            'rs75603675': 'CC'
        }
    },

    '4c2a904b': {
        'age':  7,
        'snps': {
            'rs1234': 'AG',
            'rs5678': 'GT',
            'rs12329760': 'CT',
            'rs75603675': 'AC'
        }
    },

    'deadbeef': {
        'age': 42,
        'snps': {
            'rs1234': 'GG',
            'rs5678': 'TT',
            'rs12329760': 'TT',
            'rs75603675': 'AA'
        }
    }
}


if __name__ == '__main__':
    print("writing mock individuals")
    write_mock_individuals()
