
#import pytest

from individual.individual import Individual


def test_constructor():

    individual = Individual('whatevs')
    assert isinstance(individual, Individual)
    assert individual.id == 'whatevs'

    assert hasattr(individual, 'age')
    assert hasattr(individual, 'snps'), "has snps"

    individual = Individual('whatevs', 56)
    assert individual.age == 56

    individual = Individual('whatevs', 56, {'rs1234': 'AG'})
    assert individual.age == 56
    assert individual.snps == {'rs1234': 'AG'}


def test_to_file():
    individual = Individual.from_file('tests/data/deadbeef.json')

    individual.to_file(filename='tests/data/test1.json', indent=None)

    with open('tests/data/test1.json') as f:
        result = f.read()
    assert len(result) == 119
    assert result.count('\n') == 0

    individual.to_file(filename='tests/data/test2.json', indent=4)

    with open('tests/data/test2.json') as f:
        result = f.read()
    assert len(result) == 187
    assert result.count('\n') == 11


def test_from_file():

    individual = Individual.from_file('tests/data/deadbeef.json')
    assert individual.id == 'deadbeef'
    assert individual.age == 42
    assert individual.snps['rs10490770'] == 'TT'


if __name__ == '__main__':
    test_constructor()
    test_to_file()
    test_from_file()
