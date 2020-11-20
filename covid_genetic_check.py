from individual.individual import Individual
import covcheck_score as cs

# TOOD, use FASTAPI

# TODO, demo generating different text for different risk factors.

# TODO, add logging instead of prints.

# TODO, update to read real accessor functions.


def main():
    """Chains toghether all the other functions in the analysis."""
    print("Executing analysis")

    for individual_id in ["6117323d", "4c2a904b"]:
        i = Individual.from_file(f"tests/data/{individual_id}.json")
        age_score = cs.score_individual_by_age(i)
        snp_score = cs.score_individual_by_snp(i)
        report = get_report(age_score, snp_score)

        print(i)
        print(report)

    print("Done")


def get_report(snp_score, age_score):

    a = describe_age_score(age_score)
    b = describe_snp_score(snp_score)
    c = describe_interaction(
        snp_score,
        age_score)
    
    return f"{a}. {b}. {c}."

def describe_age_score(snp_score):
    return "Man you're old!"

def describe_snp_score(snp_score):
    return "Your genome is fine brh!"

def describe_interaction(snp_score, age_score):
    return "Although your genome does not put you at increased risk, your age is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing."


if __name__ == "__main__":
    main()
