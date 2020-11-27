CovCheck takes in a simple 'genome file' in JSON format and produces a genome report 

Note that this is work in progress!

# CovCheck

TODO: Add cli


TODO: It would help if you had a one-sentence description of your project in the README file to set the context.

TODO: You could also include the installation instructions and show some examples of usage.

TODO: If you have dependencies, you should absolutely list them with their expected versions in a requirements.txt file or a higher-level tool such as flit, poetry, or Pipenv.

TODO: A common pattern to mark an unfinished code is to raise a NotImplementedError, which will be noticed at runtime:

@classmethod
def from_api(cls, url):
    raise NotImplementedError  # TODO

TODO: I'd also recommend using a few tools to automatically take care of code formatting (black), flag style-related problems (flake8), as well as warn about potential bugs (pylint).

TODO: For example, you appear to be calling get_report() with arguments in the wrong order.





https://www.covid19hg.org/publications/


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
