from individual.individual import *

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


def test_get_mock_individual():
    individual = get_mock_individual('deadbeef')
    assert isinstance(individual, Individual)
    assert individual.id == 'deadbeef'
    assert individual.age == 42
    assert individual.snps['rs1234'] == 'GG'


def test_to_file():
    individual = get_mock_individual('deadbeef')
    individual.to_file(filename='tests/data/test1.json', indent=None)

    with open('tests/data/test1.json') as f:
        result = f.read()
    assert len(result) == 111
    assert result.count('\n') == 0

    individual.to_file(filename='tests/data/test2.json', indent=4)

    with open('tests/data/test2.json') as f:
        result = f.read()
    assert len(result) == 163
    assert result.count('\n') == 9


def test_from_file():
    individual = Individual.from_file('tests/data/deadbeef.json')
    assert individual.id == 'deadbeef'
    assert individual.age == 42
    assert individual.snps['rs1234'] == 'GG'

    individual2 = get_mock_individual('deadbeef')

    print(individual)
    print(individual2)
    assert individual.__dict__ == individual2.__dict__


if __name__ == '__main__':
    test_get_mock_individual()
    test_to_file()
    test_from_file()
    test_individual()
