from individual.individual import get_mock_individual
from covcheck_score import *

i1 = get_mock_individual('6117323d')
i2 = get_mock_individual('4c2a904b')
i3 = get_mock_individual('deadbeef')
i4 = get_mock_individual('1c272047')
i5 = get_mock_individual('71768b5e')

def test_score_individual_by_age():
    s = score_individual_by_age(i1)
    assert s == 159.000

    s = score_individual_by_age(i2)
    assert s ==   0

    s = score_individual_by_age(i3)
    assert s ==   2.950

    s = score_individual_by_age(i4)
    assert s is None


def test_score_individual_by_snp():
    s = score_individual_by_snp(i1)
    assert round(s, 2) == 2.92

    s = score_individual_by_snp(i2)
    assert round(s, 2) == 2.94

    s = score_individual_by_snp(i3)
    assert round(s, 2) == 2.96

    s = score_individual_by_snp(i4)
    assert round(s, 2) == 2.94

    s = score_individual_by_snp(i5)
    assert s is None


    # These tests are for documenting purposes only...
    i = get_mock_individual('6a061313')
    s = score_individual_by_snp(i)
    assert round(s, 2) == 5.88

    # These tests are for documenting purposes only...
    i = get_mock_individual('78d811e9')
    s = score_individual_by_snp(i)
    assert round(s, 2) == 0.00


if __name__ == '__main__':
    test_score_individual_by_age()
    test_score_individual_by_snp()
