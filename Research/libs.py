
from cyvcf2 import VCF

import logging
logging.basicConfig(level=logging.INFO)


def get_imputed_snps_from_file(vcf_file):
    snp_by_id = dict()
    id_by_loc = dict()
    to_ignore = dict()

    for v in VCF(vcf_file):

        # Ignore missing IDs
        if v.ID is None:
            continue

        # Remove multiple 'SNPs' with the same location
        location = f"{v.CHROM}:{v.POS}"
        if location in id_by_loc:
            to_ignore[location] = True

        snp_by_id[v.ID] = v
        id_by_loc[location] = v.ID

    for _x in to_ignore:
        if _x in id_by_loc:
            snp_by_id.pop(id_by_loc[_x])

    return snp_by_id
