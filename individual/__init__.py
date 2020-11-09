
import json

# Using simple Namedtuples here instead of classes for prototyping...
from collections import namedtuple

Individual = namedtuple('Individual', 'id age snps')

# TODO: Make an individual Class, and have a bit of class data for the
# mock individuals.


def get_individual_from_file(filename =
                             'test/data/individuals/deadbeef.json'):
    
    with open(filename, 'r') as f:
        individual_string = f.read()
        individual_json = json.loads(individual_string)
    return individual_from_json(individual_json)


def write_mock_individuals():
    """Helper function to create some data for testing."""
    individuals = get_mock_individuals();

    for iid, i in individuals.items():
        f = open(f"test/data/individuals/{iid}.json", "w")

        with f:
            f.write(get_json_individual(i))


def individual_to_json(individual = None):
    """Get the individual object as a json string."""
    return json.dumps(individual._asdict())


def individual_from_json(individual_json = None):
    """Get the individual object as a json string."""

    return Individual(
        id = individual_json['id'],
        age = individual_json['age'],
        snps = individual_json['snps']
    )


def get_mock_individual(individual_id = None):
    """Return a single mock 'individual' for testing."""

    individuals = get_mock_individuals();

    return individuals[individual_id]


def get_mock_individuals():
    """Return a 'database' of mock individuals for testing."""

    individuals = {}

    individuals['6117323d'] = Individual(
        id = '6117323d',
        age = 93,
        snps = {'rs1234': 'AA',
                'rs5678': 'GG',
                'rs12329760': 'CC',
                'rs75603675': 'CC'
        }
    )

    individuals['4c2a904b'] = Individual(
        id = '4c2a904b',
        age =  7,
        snps = {'rs1234': 'AG',
                'rs5678': 'GT',
                'rs12329760': 'CT',
                'rs75603675': 'AC'
        }
    )

    individuals['deadbeef'] = Individual(
        id = 'deadbeef',
        age = 42,
        snps = {'rs1234': 'GG',
                'rs5678': 'TT',
                'rs12329760': 'TT',
                'rs75603675': 'AA'
        }
    )

    return individuals


if __name__ == '__main__':
    #write_mock_individuals()

    i = get_individual_from_file()
    print(i)
