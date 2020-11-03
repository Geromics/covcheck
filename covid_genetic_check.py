
# Using Namedtuples instead of classes for now for prototyping
from collections import namedtuple

# Construct a namedtuple class for (crudely) working with SNP data
SNPs = namedtuple('SNP', ['id', 'alleles'])


# TODO, add 'scores' for the real SNPs.

# TODO, demo generating different text for different risk factors.

# TODO, add logging instead of prints.

# TODO, think about data structures a bit more.

# TODO, update to read accessor functions.


def result_for_individual(individual_id):
    snp_score, age_score = score_individual(individual_id)

    print(snp_score, age_score)
    
    a = describe_snp_score(snp_score)
    b = describe_age_score(age_score)
    c = describe_interaction(snp_score, age_score)
    
    return f"{a}. {b}. {c}."

def describe_snp_score(snp_score):
    return "Your genome is fine brh!"

def describe_age_score(snp_score):
    return "Man you're old!"

def describe_interaction(snp_score, age_score):
    return "Although your genome does not put you at increased risk, your age is a significant factor that does put you at above average risk of severe Covid 19 infection. You should consider taking extra precautions such as hand washing, mask wearing and social distancing."



def score_individual(individual_id):
    """Produce a 'covcheck score' for a given individual_id."""
    print(f"Getting private data for individual_id: {individual_id}")

    snp_data = get_snp_data(individual_id)
    print(snp_data)

    age_data = get_age_data(individual_id)
    print(age_data)

    snp_score = score_snps(snp_data)
    age_score = score_ages(age_data)

    # I was thinking to produce a combined score, but the information
    # we want to give to the user is age specific.
    return(snp_score, age_score)



def score_snps(snp_data):
    """Use SNP data to produce a 'covcheck score' based on SNPs.

    Note, we mock the analysis here!
    """
    
    snp_score = 0
    
    for snp in snp_data:
        print(snp)

        if snp.id == 'rs1234':
            # Each A adds +05
            if snp.alleles == 'AA':
                snp_score = snp_score + 10
            if snp.alleles == 'AG':
                snp_score = snp_score +  5
            if snp.alleles == 'GA':
                snp_score = snp_score +  5

        if snp.id == 'rs5678':
            # Each T adds +10
            if snp.alleles == 'TT':
                snp_score = snp_score + 20
            if snp.alleles == 'GT':
                snp_score = snp_score + 10
            if snp.alleles == 'TG':
                snp_score = snp_score + 10

    return snp_score



def score_ages(age):
    """Use age data to produce a 'covcheck score' based on age.

    Note, we mock the analysis here!
    """
    
    age_score = 0

    if age is None:
        return None

    if age > 80:
        age_score = age_score + 128
    if age > 60:
        age_score = age_score +  64
    if age > 50:
        age_score = age_score +  32
    if age > 40:
        age_score = age_score +  16
    if age > 30:
        age_score = age_score +   8
    if age > 20:
        age_score = age_score +   4
    if age > 10:
        age_score = age_score +   2

    return age_score



def get_snp_data(individual_id):
    """Return the analysis specific SNPs for the given individual_id.

    Note, we mock the data here!
    """
    
    snp1 = SNPs('rs1234', 'AG')
    snp2 = SNPs('rs5678', 'GT')
    snp3 = SNPs('rs12329760', 'CT')
    snp4 = SNPs('rs75603675', 'AT')

    if individual_id == '6117323d':
        snp1 = SNPs('rs1234', 'AA')
        snp2 = SNPs('rs5678', 'GG')
        snp3 = SNPs('rs12329760', 'CC')
        snp4 = SNPs('rs75603675', 'AA')

    if individual_id == '4c2a904b':
        snp1 = SNPs('rs1234', 'GG')
        snp2 = SNPs('rs5678', 'TT')
        snp3 = SNPs('rs12329760', 'TT')
        snp4 = SNPs('rs75603675', 'TT')

    return([snp1, snp2])

def get_age_data(individual_id):
    """Return the age of the given individual_id, if available.

    Note, we mock the data here!
    """
    
    age = None

    if individual_id == '6117323d':
        age = 93
    
    if individual_id == '4c2a904b':
        age = 7

    return(age)



if __name__ == "__main__":
    print("Executing analysis")

    print(result_for_individual("6117323d"))
    print(result_for_individual("4c2a904b"))
    print(result_for_individual("deadbeef"))

    print("Done")
