from individual.individual import get_mock_individual
from covcheck_score import *

i1_id = '6117323d'
i2_id = '4c2a904b'
i3_id = 'deadbeef'

def test_score_individual_by_age():
    i = get_mock_individual(i1_id)
    s = score_individual_by_age(i)
    assert s == 144

    i = get_mock_individual(i2_id)
    s = score_individual_by_age(i)
    assert s == 0

    i = get_mock_individual(i3_id)
    s = score_individual_by_age(i)
    assert s == 16


def test_score_individual_by_snp():
    i = get_mock_individual(i1_id)
    s = score_individual_by_snp(i)
    assert s == 0.464

    i = get_mock_individual(i2_id)
    s = score_individual_by_snp(i)
    assert s == 0.5885

    i = get_mock_individual(i3_id)
    s = score_individual_by_snp(i)
    assert s == 0.713
    


if __name__ == '__main__':
    test_get_mock_individual()
    test_to_file()
    test_from_file()
    test_individual()
