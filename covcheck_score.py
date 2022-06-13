## TODO: Scores should be LOD risk ratios I think...
import json
def score_individual_by_age(individual):
    """Score an individuals 'COVID risk' by age.

    See the analysis within stats/age_score.r to understand where the
    scores come from. Scores are 'odds ratios' of COVID-19 CFR risk.

    TODO: Read this data from file.
    TODO: Update the analyis!

    """
    if individual.age is None:
        return None
    age_risk_scores = json.load("age_risk_scores.json")
    for age, risk_score in sorted(age_riskscores.items()):
        if individual.age < age:
            return risk_score
    return None

def score_individual_by_snp(individual):
    """Score an individuals 'COVID risk' using SNPs.

    The increased CFR (is based on the analysis in this preprint:
    https://www.researchsquare.com/article/rs-37798/v1

    Below we assume statistical independence of the two variables!

    See the README.md for details.
    """

    snp_score = 0
    baseline_cfr = 0.1

    # TODO: Remove magic knowledge using a SNP object?
    # TODO: This is really crappy code!

    if len(set(('rs12329760', 'rs75603675')) & set(individual.snps)) == 0:
        return None

    for snp_id, alleles in individual.snps.items():
        if snp_id == 'rs12329760':
            # Each C adds 0.2320
            snp_score = snp_score + ( alleles.count("C") * 0.146 ) # CFR!

        if snp_id == 'rs75603675':
            # Each A adds 0.3565
            snp_score = snp_score + ( alleles.count("A") * 0.148 ) # CFR!

    snp_score = snp_score / baseline_cfr

    return snp_score

