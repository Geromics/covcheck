import sys, argparse, json

from individual.individual import Individual
from covcheck_score import score_individual_by_age, score_individual_by_snp

version = '0.1.18'


# TODO: Demo generating different text for different risk factors.
# TODO: Add logging instead of prints.

def main():
    ap = argparse.ArgumentParser(description='Score an individual.')

    ap.add_argument('--version', action='version', version=f'%(prog)s {version}')
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

    a = describe_age_score(age_score)
    b = describe_snp_score(snp_score)
    c = describe_interaction(
        age_score,
        snp_score
    )
    
    return f"{a}. {b}. {c}."

def describe_age_score(snp_score):
    return "Man you're old!"

def describe_snp_score(snp_score):
    return "Your genome is fine brh!"

def describe_interaction(snp_score, age_score):
    return "Although your genome does not put you at increased risk, your age is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing."


if __name__ == "__main__":
    main()


def test_something():
    """Chains toghether all the other functions in the analysis."""

    for individual_id in ["6117323d", "4c2a904b"]:
        i = Individual.from_file(f"tests/data/{individual_id}.json")
        age_score = cs.score_individual_by_age(i)
        snp_score = cs.score_individual_by_snp(i)
        report = get_report(age_score, snp_score)

        print(report)

    print("Done")

