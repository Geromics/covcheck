
import sys, argparse, json, math

from individual.individual import Individual
from covcheck_score import \
    score_individual_by_age, \
    score_individual_by_snp

VERSION = '0.1.18'


# TODO: Demo generating different text for different risk factors.
# TODO: Add logging instead of prints.

def main():
    ap = argparse.ArgumentParser(description='Score an individual.')

    ap.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    ap.add_argument('--verbose', '-v', action='count', default=0)

    ap.add_argument('infile', type=argparse.FileType('r'),
                    help='JSON format file containing individual data')

    ap.add_argument('outfile', type=argparse.FileType('w'), nargs='?',
                    default=sys.stdout,
                    help='JSON format results file (default: <stdout>)')

    args = ap.parse_args()

    print(f"Executing analysis for file '{args.infile.name}'")

    i = Individual.from_file(filename=args.infile.name)

    age_score = score_individual_by_age(i)
    snp_score = score_individual_by_snp(i)
    report_text = get_report_text(age_score, snp_score)

    i_report = {}
    i_report['id'] = i.id
    i_report['age'] = i.age
    i_report['age_score'] = age_score
    i_report['snp_score'] = snp_score
    i_report['text'] = report_text

    json.dump(i_report, args.outfile, indent=2)


def get_report_text(age_score, snp_score):

    a = b = c = d = ""

    if age_score is not None:
        a = describe_age_score(age_score)

    if snp_score is not None:
        c = describe_snp_score(snp_score)

    if age_score is not None and snp_score is not None:
        b = describe_interaction_1(age_score, snp_score)
        d = describe_interaction_2(age_score, snp_score)

    return f"{a}{b}{c}{d}"


def describe_age_score(score):

    if score is None:
        return ""

    # Build up the description string part 1/3
    desc = "By virtue of your age, "

    # Conditional part 2/3
    if score < 2:
        desc += "you are at a slightly lower or negligible "
    elif score < 3:
        desc += "you are at a slightly increased "
    else:
        desc += "you are at an increased "

    # Why is rounding so complicated in Python?
    score = round(score, 1)

    # Final part 3/3
    desc += "risk of severe COVID-19 infection relative to other people " + \
            f"({score} times as likely to have a severe infection). "

    return desc


def describe_snp_score(score):
    if score is None:
        return ""

    # Build up the description string part 1/3
    desc = "By inspecting your genome, "

    # Conditional part 2/3
    if score < 1:
        desc += "you are at a slightly lower or negligible "
    elif score < 3:
        desc += "you are at a slightly increased "
    else:
        desc += "you are at an increased "

    # Why is rounding so complicated in Python?
    score = round(score, 1)

    # Final part 3/3
    desc += "risk of severe COVID-19 infection relative to other people " + \
            f"({score} times as likely to have a severe infection). "

    return desc


def describe_interaction_1(age_score, snp_score):

    diff = abs(math.log((age_score+0.001)/(snp_score+0.001)))

    if diff > 5:
        return "However, "

    return "Similarly, "


def describe_interaction_2(age_score, snp_score):
    desc = ""

    if math.log((age_score+0.001)/(snp_score+0.001)) > +5:
        desc = "Although your genome does not put you at increased risk, your age is " \
               "a significant factor that does put you at above average risk of " \
               "severe COVID 19 infection. You should consider taking extra " \
               "precautions such as hand washing, mask wearing and social " \
               "distancing. "

    if math.log((age_score+0.001)/(snp_score+0.001)) < -5:
        desc = "Although your age does not put you at increased risk, your genome is " \
               "a significant factor that does put you at above average risk of " \
               "severe COVID 19 infection. You should consider taking extra " \
               "precautions such as hand washing, mask wearing and social " \
               "distancing. "

    return desc




if __name__ == "__main__":
    main()


def test_something():
    """Chains toghether all the other functions in the analysis.

    TODO: Move this function into a test file.

    """

    for individual_id in ["6117323d", "4c2a904b"]:
        i = Individual.from_file(f"tests/data/{individual_id}.json")
        age_score = score_individual_by_age(i)
        snp_score = score_individual_by_snp(i)
        report = get_report_text(age_score, snp_score)

        print(report)

    print("Done")
