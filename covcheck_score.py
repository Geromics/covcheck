## TODO: Scores should be LOD risk ratios I think...

def score_individual_by_age(individual):
    """Score an individuals 'COVID risk' by age.


    """
    age_score = 0

    if individual.age > 80:
        age_score = age_score + 128

    if individual.age > 40:
        age_score = age_score +  16

    return age_score


def score_individual_by_snp(individual):
    """Score an individuals 'COVID risk' using SNPs.

    See the README.md for details.
    """
    snp_score = 0

    # TODO: Remove magic knowledge using a SNP object?
    for snp_id, alleles in individual.snps.items():
        if snp_id == 'rs12329760':
            # Each C adds 0.2320
            snp_score = snp_score + ( alleles.count("C") * 0.2320 )

        if snp_id == 'rs75603675':
            # Each A adds 0.3565
            snp_score = snp_score + ( alleles.count("A") * 0.3565 )

    return snp_score


