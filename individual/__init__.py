
import json

# Using simple Namedtuples here instead of classes for prototyping...
from collections import namedtuple

Individual = namedtuple('Individual', 'id age snps')


def write_mock_individuals():
    individuals = get_mock_individuals();


def print_json_individual(individual = None):
    if individual is None:
        individual = get_mock_individual()

    print(json.dumps(individual._asdict()))


def get_mock_individual(individual_id = 'deadbeef'):
    """Return data for a single mock 'individual' *for testing*."""

    individuals = get_mock_individuals();

    return individuals[individual_id]


def get_mock_individuals():
    """Return a 'database' of mock individuals *for testing*."""

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





