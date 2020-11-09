
import individual


def test_individual(i1 = None):
    if i1 is None:
        i1 = individual.get_mock_individual('deadbeef')

    assert type(i1) is individual.Individual, "type check"
    assert hasattr(i1, 'id'), "has id"
    assert hasattr(i1, 'age'), "has age"
    assert hasattr(i1, 'snps'), "has snps"
    
    assert i1.id == 'deadbeef', "default individual id placeholder"
    assert i1.age == 42, "the default individual is 42 years old"
    assert i1.snps['rs75603675'] == 'AA', "the default individual has AA"


def test_json_individual():
    i1 = individual.get_mock_individual('deadbeef')
    i1_json = individual.individual_to_json(i1)
    i2 = individual.individual_from_json(i1_json)

    assert i1 == i2, "we can round trip an individual to and from json"

    test_individual(i2)


def test_write_mock_individuals():
    # TODO: meh
    pass


def test_individual_from_file():
    i1 = individual.individual_from_file()
    test_individual(i1)


def test_score_individual():
    i1 = individual.individual_from_file()

    # TODO...


if __name__ == '__main__':
    test_individual()
    test_json_individual()
