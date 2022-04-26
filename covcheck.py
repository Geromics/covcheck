
version = '0.2.1'

import argparse
import sys
import json
import math

from individual.individual import Individual

from scores import \
    score_individual_by_age, \
    score_individual_by_snp_1


# TODO: Links to --version below
import logging
logging.getLogger().setLevel(logging.DEBUG)


def main():
    ap = argparse.ArgumentParser(description='Score an individual.')

    ap.add_argument('--version', action='version', version=f'%(prog)s {version}')
    ap.add_argument('--verbose', '-v', action='count', default=0)

    ap.add_argument('infile', type=argparse.FileType('r'),
                    help='JSON format file containing individual SNP data')

    ap.add_argument('outfile', type=argparse.FileType('w'), nargs='?',
                    default=sys.stdout,
                    help='JSON format results file (default: <stdout>)')

    args = ap.parse_args()

    logging.info(f"Executing analysis for file '{args.infile.name}'")

    try:
        i = Individual.from_file(filename=args.infile.name)
    except Error:
        logging.error(
            f"Failed to load individual from file '{args.infile.name}'")
    else:
        logging.debug(f"Scoring individual '{i}'")

    # Build the score from various sources
    a = score_individual_by_age(i)
    s = score_individual_by_snp_1(i)

    logging.debug(f"Age score: {a}")
    logging.debug(f"SNP score: {s}")

    i_report = {}
    i_report['id'] = i.id
    i_report['age'] = i.age
    i_report['age_score'] = a
    i_report['snp_score'] = s

    json.dump(i_report, args.outfile, indent=2)


if __name__ == "__main__":
    main()
