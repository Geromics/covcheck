Note that this is work in progress!

# Covcheck Backend

Each of the 2SNP projects have a specific back end to perform their specific analysis. This repo contains the code for the CovCheck back end.



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
