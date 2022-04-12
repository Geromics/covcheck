
## What is CovCheck?


The CovCheck analysis computes a personal genome report indicating
'risk of severe symptoms' (CFR) from COVID-19 infection.

The risk analysis is based on published, peer-reviewed studies:
https://www.covid19hg.org/publications/

Personal genome data and age (if provided) is read from a simple
'genome file' in JSON format.

**Note that this analyis is work in progress!!!**



### Installation and Usage

To install, pull from git:

    git@github.com:Geromics/covcheck.git


change to the appropriate directory:

    cd covcheck


and run the code:

    python3 covid_genetic_check.py -h

    usage: check.py [-h] [--version] [--verbose] infile [outfile]

    Score an individual.

    positional arguments:
      infile         JSON format file containing individual data
      outfile        JSON format results file (default: <stdout>)

    optional arguments:
      -h, --help     show this help message and exit
      --version      show program's version number and exit
      --verbose, -v


The only formal requirements (`requirements.txt`) are for testing:

    pip install -r requirements.txt


which is done by:

    python3 -m pytest -v .


Note, project dependncies are **not** managed by a high level tool
such as flit, poetry or Pipenv.



### Analysis details

The analysis of risk with age is based on data from here:
* https://ourworldindata.org/mortality-risk-covid#case-fatality-rate-of-covid-19-by-age

and has been done with help from:
* https://realrisk.wintoncentre.uk/

The genome report is currently based on the analysis in this preprint:
https://www.researchsquare.com/article/rs-37798/v1


Notes from the preprint...

    ##reference=GRCh38.p12
    chr21 41480570 rs12329760 C T . . .
    chr21 41507982 rs75603675 C A . . .

    rs12329760, TMPRSS2(-), V197M, C->T (G->A, V[GTG] -> M[ATG])
    C is the risk allele, T is 'protective'

    rs75603675, TMPRSS2(-), G008V, C->A (G->T, G[GGT] -> V[GTT])
    A is the risk allele, C is 'protective'

    Spearman’s correlation with COVID-19 CFR:
    ρ = -0.464, P = 0.0157 for V197M C->T (G->A)
    ρ = +0.713, P = 0.0018 for G008V C->A (G->T)

    The higher the score, the greater your genetic risk of severe
    COVID-19 infection.



### Additional references

#### COVID:
* QCovid® risk calculator
    * https://qcovid.org/
* The Association of Local Authority Medical Advisors (ALAMA), COVID-AGE
    * https://alama.org.uk/covid-19-medical-risk-assessment/
* Charlson Comorbidity Index
    * https://www.mdcalc.com/charlson-comorbidity-index-cci
* GenOMICC COVID-19 Study
    * https://genomicc.org/
    * https://www.genomicsengland.co.uk/covid-19/


#### Polygenic Risk Scores:
* From Basic Science to Clinical Application of Polygenic Risk Scores: A Primer.
    * https://europepmc.org/article/MED/32997097
* Towards clinical utility of polygenic risk scores.
    * http://europepmc.org/article/MED/31363735


#### Papers studying the genetics of COVID
* Genetic susceptibility of COVID-19: a systematic review of current evidence
    * https://eurjmedres.biomedcentral.com/articles/10.1186/s40001-021-00516-8
* Mapping the human genetic architecture of COVID-19
    * https://www.nature.com/articles/s41586-021-03767-x
* Identification of LZTFL1 as a candidate effector gene at a COVID-19 risk locus
    * https://www.nature.com/articles/s41588-021-00955-3
* The major genetic risk factor for severe COVID-19 is inherited from Neanderthals
    * https://www.nature.com/articles/s41586-020-2818-3
* Genetic mechanisms of critical illness in COVID-19
    * https://www.nature.com/articles/s41586-020-03065-y
* The quest to find genes that drive severe COVID
    * https://www.nature.com/articles/d41586-021-01827-w
* A catalog of associations between rare coding variants and COVID-19 outcomes
    * https://www.medrxiv.org/content/10.1101/2020.10.28.20221804v2




### Random notes

A common pattern to mark an unfinished code is to raise a
`NotImplementedError` that is noticed at runtime:

    @classmethod
    def from_api(cls, url):
        raise NotImplementedError  # TODO

TODO: Use a few tools to automatically take care of code formatting
(black), flag style-related problems (flake8), as well as warn about
potential bugs (pylint).

