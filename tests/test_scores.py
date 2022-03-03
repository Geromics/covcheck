
from individual import individual as ind
from scores import \
    score_individual_by_age, \
    score_individual_by_snp_1

individual = ind._get_mock_individuals_for_testing()

i1 = individual['6117323d']  # snp_1 protected old
i2 = individual['4c2a904b']  # snp_1 protected young
i3 = individual['deadbeef']  # snp_1 protected middleaged
i4 = individual['1c272047']  # snp_1 protected, no age
i5 = individual['71768b5e']  # no matching snp_1, no age
i6 = individual['6a061313']  # max snp score, no age
i7 = individual['78d811e9']  # min snp score, no age


def test_runthrough():
    for i in individual.values():
        print(i)
        a = score_individual_by_age(i)
        assert isinstance(a, int) or isinstance(a, float) or a is None

        s = score_individual_by_snp_1(i)
        assert s['group'] == 'hap_1'
        assert s['trait'] == 'severe infection'

        assert 'snps' in s
        assert 'score' in s

        print(s)
        print()


def test_score_individual_by_age():

    s = score_individual_by_age(i1)
    assert s == 159.000

    s = score_individual_by_age(i2)
    assert s == 000.000

    s = score_individual_by_age(i3)
    assert s == 002.950

    s = score_individual_by_age(i4)
    assert s is None


def test_score_individual_by_snp_1():

    s = score_individual_by_snp_1(i1)
    s = s['score']

    assert 'rs13078854' not in s
    assert 'rs71325088' not in s
    assert 'rs10490770' in s

    s = s['rs10490770']['or']
    assert round(s, 2) == 2.00

    s = score_individual_by_snp_1(i5)
    assert len(s['score']) == 0

    s = score_individual_by_snp_1(i6)
    assert 'rs13078854' in s['score']
    assert 'rs71325088' in s['score']
    assert 'rs10490770' in s['score']

    assert round(s['score']['rs13078854']['or'], 2) == 0.60
    assert round(s['score']['rs71325088']['or'], 2) == 1.90
    assert round(s['score']['rs10490770']['or'], 2) == 2.00

    s = score_individual_by_snp_1(i7)
    assert 'rs13078854' in s['score']
    assert 'rs71325088' in s['score']
    assert 'rs10490770' in s['score']

    assert round(s['score']['rs13078854']['or'], 2) == 1.00
    assert round(s['score']['rs71325088']['or'], 2) == 1.00
    assert round(s['score']['rs10490770']['or'], 2) == 1.00


if __name__ == '__main__':
    test_runthrough()
    test_score_individual_by_age()
    test_score_individual_by_snp_1()
