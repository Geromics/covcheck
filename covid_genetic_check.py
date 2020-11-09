import json

# Using simple Namedtuples here instead of classes for prototyping...
from collections import namedtuple
from individual import get_mock_individual


# TODO, demo generating different text for different risk factors.

# TODO, add logging instead of prints.

# TODO, update to read real accessor functions.


def main():
    """The main function is basically a test of all the functions in the
    analysis 'framework' chained together in order.

    """
    print("Executing analysis")

    for individual_id in ["6117323d", "4c2a904b"]:
        individual_data = get_analysis_data(individual_id)
        risk_score = score_individual(individual_data)
        analysis_text = result_for_individual(*risk_score)
        
        print(json.dumps(individual_data._asdict()))
        print(risk_score)
        print(analysis_text)

    print("Done")


def get_analysis_data(individual_id):
    """Get the data used by the analysis for the given individual_id.

    Note, we mock the data here!

    Later we will 'call out' to some API or other.

    """
    individual_data = get_mock_individual(individual_id)

    return(individual_data)


def score_individual(individual_data):
    """Produce the 'covcheck score' from the given data.

    Currently snp scores are based on this preprint:
    https://www.researchsquare.com/article/rs-37798/v1

    ##reference=GRCh38.p12
    chr21 41480570 rs12329760 C T . . .
    chr21 41507982 rs75603675 C A . . .

    rs12329760, TMPRSS2(-), V197M, G>A, V[GTG] > M[ATG]
    C is the risk allele, T is 'protective'

    rs75603675, TMPRSS2(-), G008V, G>T, G[GGT] > V[GTT]
    A is the risk allele, C is 'protective'

    Spearman’s correlation with CFR:
    ρ = -0.464, P = 0.0157 for V197M C>T (G>A)
    ρ = +0.713, P = 0.0018 for G008V C>A (G>T)

    The higher the score, the greater your genetic risk of severe
    COVID-19 infection.

    """    
    snp_score = 0
    age_score = 0

    if individual_data.age > 80:
        age_score = age_score + 128
    if individual_data.age > 40:
        age_score = age_score +  16

    # TODO: Remove magic knowledge using SNP tuple
    for snp_id, alleles in individual_data.snps.items():
        if snp_id == 'rs12329760':
            # Each C adds 0.2320
            snp_score = snp_score + ( alleles.count("C") * 0.2320 )

        if snp_id == 'rs75603675':
            # Each A adds 0.3565
            snp_score = snp_score + ( alleles.count("A") * 0.3565 )

    # TODO: Remove magic knowledge here somehowx
    return age_score, snp_score


def result_for_individual(snp_score, age_score):

    a = describe_snp_score(snp_score)
    b = describe_age_score(age_score)
    c = describe_interaction(snp_score, age_score)
    
    return f"{a}. {b}. {c}."

def describe_snp_score(snp_score):
    return "Your genome is fine brh!"

def describe_age_score(snp_score):
    return "Man you're old!"

def describe_interaction(snp_score, age_score):
    return "Although your genome does not put you at increased risk, your age is a significant factor that does put you at above average risk of severe COVID 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing."


if __name__ == "__main__":
    main()
