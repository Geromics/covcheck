from individual.individual import get_mock_individual
from covcheck_score import score_individual_by_snp, score_individual_by_age
from covid_genetic_check import get_report_text

i1 = get_mock_individual('6117323d')
i2 = get_mock_individual('4c2a904b')
i3 = get_mock_individual('deadbeef')
i4 = get_mock_individual('1c272047')
i5 = get_mock_individual('44444444')
i6 = get_mock_individual('eeeeeeee')
i7 = get_mock_individual('71768b5e')

def test_get_report_text():
    age_score = score_individual_by_age(i1)
    snp_score = score_individual_by_snp(i1)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == 'By virtue of your age, you are at an increased risk of severe COVID-19 infection relative to other people (159 times as likely to have a severe infection). Similarly, By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (2.9 times as likely to have a severe infection). '

    age_score = score_individual_by_age(i2)
    snp_score = score_individual_by_snp(i2)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == 'By virtue of your age, you are at a slightly lower or negligible risk of severe COVID-19 infection relative to other people (0 times as likely to have a severe infection). However, By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (2.9 times as likely to have a severe infection). Although your age does not put you at increased risk, your genome is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing. '

    age_score = score_individual_by_age(i3)
    snp_score = score_individual_by_snp(i3)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == 'By virtue of your age, you are at a slightly increased risk of severe COVID-19 infection relative to other people (3.0 times as likely to have a severe infection). Similarly, By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (3.0 times as likely to have a severe infection). '

    age_score = score_individual_by_age(i4)
    snp_score = score_individual_by_snp(i4)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == 'By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (2.9 times as likely to have a severe infection). '

    age_score = score_individual_by_age(i5)
    snp_score = score_individual_by_snp(i5)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == 'By virtue of your age, you are at a slightly lower or negligible risk of severe COVID-19 infection relative to other people (0 times as likely to have a severe infection). However, By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (1.5 times as likely to have a severe infection). Although your age does not put you at increased risk, your genome is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing. '

    age_score = score_individual_by_age(i6)
    snp_score = score_individual_by_snp(i6)

    report_text = get_report_text(age_score, snp_score)

    print(f"-{report_text}-")
    assert report_text == 'By virtue of your age, you are at a slightly lower or negligible risk of severe COVID-19 infection relative to other people (0 times as likely to have a severe infection). However, By inspecting your genome, you are at a slightly increased risk of severe COVID-19 infection relative to other people (1.5 times as likely to have a severe infection). Although your age does not put you at increased risk, your genome is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing. '

    age_score = score_individual_by_age(i7)
    snp_score = score_individual_by_snp(i7)

    report_text = get_report_text(age_score, snp_score)

    assert report_text == ''

