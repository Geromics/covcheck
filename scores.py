
# TODO: Remove 'magic knowledge' by using a SNP Object?


def score_individual_by_age(individual):
    """Score an individuals 'COVID risk' by age.

    See the analysis within stats/age_score.r to understand where the
    scores come from. Scores are 'odds ratios' of COVID-19 CFR risk.

    TODO: Read this data from file?

    """
    if individual.age is None:
        return None

    if individual.age < 9:
        return 0

    elif individual.age < 19:
        return 00.500
    elif individual.age < 29:
        return 01.050
    elif individual.age < 39:
        return 01.875
    elif individual.age < 49:
        return 02.950
    elif individual.age < 59:
        return 08.000
    elif individual.age < 69:
        return 27.000
    elif individual.age < 79:
        return 79.750

    # Age is 80+
    return 159


def score_individual_by_snp_1(individual):
    """Calculate the odds ratios of Covid-19 'severe infection' using SNPs
       from three COVID associations reported in cytogenetic region
       3p21.31 (LZTFL1, SLC6A20). All three studies report SNPs in
       close LD with each other.

    rs13078854, reported in PMID:33888907 Trans-ancestry analysis
      reveals genetic and nongenetic associations with COVID-19
      susceptibility and severity. [Respiratory simptoms]. The G
      allele (G/A) is protective (OR 0.6).

    rs71325088, reported in PMID:33307546 Genetic mechanisms of
      critical illness in Covid-19. [Critical illness]. The C allele
      (T/C) is causative (OR 1.9).

    rs11385942, reported in PMID:32558485 Genomewide Association Study
      of Severe Covid-19 with Respiratory Failure. [Severe
      infection]. The GA allele is causative (OR 2.11). AND
      PMID:33453462 Chromosome 3 cluster rs11385942 variant links
      complement activation with severe COVID-19.

    MARKER SNP:

    rs10490770, is in LD with all of the above (in European and
      African populations) and found in the 23andMe v3 chip. Note that
      when rs10490770 is T (T/C), rs13078854 is G and rs71325088 is
      T. rs11385942 isn't mapped for some reason...

    """

    snp_score = {}
    snp_score['group'] = 'hap_1'
    snp_score['trait'] = 'severe infection'

    snp_score['snps'] = {}
    snp_score['snps']['rs13078854'] = {'effect_allele': "G", 'other_allele': "A", 'or': 0.6}
    snp_score['snps']['rs71325088'] = {'effect_allele': "C", 'other_allele': "T", 'or': 1.9}
    snp_score['snps']['rs10490770'] = {'effect_allele': "T", 'other_allele': "C", 'or': 2.0}

    snp_score['score'] = {}
    for snp in snp_score['snps']:

        if snp in individual.snps:
            alleles = individual.snps[snp]
            snp_score['score'][snp] = {
                'imputed': False,
                'alleles': alleles,
            }
            if alleles.count(snp_score['snps'][snp]['effect_allele']) > 0:
                snp_score['score'][snp].update({
                    'or': snp_score['snps'][snp]['or']
                })
            else:
                snp_score['score'][snp].update({
                    'or': 1.0,
                })


    # TODO: Sanity check alleles

    return snp_score
