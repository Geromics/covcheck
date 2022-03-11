from collections import defaultdict

import numpy as np

import libs
import ens

import logging
logging.basicConfig(level=logging.INFO)

t3andme_v3_file = '/home/dan/Downloads/90365083240/' + \
    'genome_Dan_Bolser_v3_Full_20210922075748.txt'

snps_of_interest = [
    'rs2271616', 'rs10490770', 'rs11919389', 'rs1886814', 'rs72711165',
    'rs912805253', 'rs10774671', 'rs1819040', 'rs77534576', 'rs2109069',
    'rs74956615', 'rs4801778', 'rs13050728'
]

# The imputed file is a shortcut we can use re. haplotypes
imputed_vcf_chr_files = []
for chr in [3, 6, 8, 12, 17, 19, 21]:
    imputed_vcf_chr_files.append(
        "/home/dan/Downloads/90365083240/" +
        f"Sanger Imputation Server/hrc-eagle2.vcfs/{chr}.vcf.gz")

# We're measuring LD, so...
ld_populations = ens.get_ld_populations()
logging.info(f"Got {len(ld_populations)} populations from Ensembl")


# Begin
logging.info(f"reading file '{t3andme_v3_file}'")
t3andme_snps_by_pos = defaultdict(dict)
t3andme_snps_by_ids = dict()
with open(t3andme_v3_file, 'r') as f:
    for l in f:
        if l[0] == '#':
            continue
        (id, chr, pos, alele) = l.split('\t')

        # Ignoring several can's of worms...
        t3andme_snps_by_pos[chr][int(pos)] = id

        assert id not in t3andme_snps_by_ids
        t3andme_snps_by_ids[id] = [chr, pos]


logging.info(f"converting to numpy for later")
t3andme_snps_np_pos = dict()
for chr, pos in t3andme_snps_by_pos.items():
    t3andme_snps_np_pos[chr] = np.asarray(sorted(pos.keys()))


logging.info(f"opening imputed vcf chromosomes")
imputed_snps_by_ids = dict()
for f in imputed_vcf_chr_files:
    logging.info(f"opening vcf '{f}'")
    imputed_snps_by_ids = libs.get_imputed_snps_from_file(f)

    # DEBUGGING
    break


# Get the 10 closest snps to the snps_of_interest
near_snps = dict()
for id in snps_of_interest:
    logging.info(f"Finding SNPs near to {id} in the 23andMe v3 array.")

    if id not in imputed_snps_by_ids:
        logging.error(f"MISSING SNP '{id}'")
        continue

    chr = imputed_snps_by_ids[id].CHROM
    pos = imputed_snps_by_ids[id].POS

    logging.info(f"SNP {id} has chromosome {chr}, position {pos}.")

    # Good old numpy arrays
    delta = abs(t3andme_snps_np_pos[chr] - pos)

    min_index = np.argmin(delta)

    near_snps[id] = dict()
    for near_idx in range(min_index-5, min_index+5):
        near_pos = t3andme_snps_np_pos[chr][near_idx]
        near_snp = t3andme_snps_by_pos[chr][near_pos]
        distance = delta[near_idx]

        logging.debug([id, distance, near_pos, near_snp])

        near_snps[id][near_snp] = {'dist': distance}

        logging.info(f"Near SNP: '{near_snp}' ({distance})")

        near_snps[id][near_snp]['pops'] = list()
        for pop in ld_populations:
            ld = ens.get_ld(id, near_snp, pop)

            near_snps[id][near_snp]['count'] = 0
            for l in ld:
                near_snps[id][near_snp]['pops'].append({'pop': pop, 'ld': l})

                if float(l['r2']) > 0.6:
                    near_snps[id][near_snp]['count'] += 1

        print(near_snps[id][near_snp]['count'])
               
               
