from collections import defaultdict

from cyvcf2 import VCF

import logging
logging.basicConfig(level=logging.INFO)

imputed_vcf_files = []

for chr in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,'X']:
    imputed_vcf_files.append("/home/dan/Downloads/90365083240/" +
    f"Sanger Imputation Server/hrc-eagle2.vcfs/{chr}.vcf.gz")

for f in imputed_vcf_files:
    logging.info(f"opening vcf '{f}'")

    # These should be global, but put here to save memory on my laptop.
    imputed_snps_by_pos = defaultdict(dict)
    imputed_snps_by_ids = dict()
    imputed_snps_to_kil = dict()

    what_to_call = defaultdict(int)

    for v in VCF(f):

        # Same position, different rsID?
        if v.POS in imputed_snps_by_pos[v.CHROM]:
            x = imputed_snps_by_ids[
                imputed_snps_by_pos[v.CHROM][v.POS]
            ]

            if v.ID != x.ID:
                if v.ID is None:
                    logging.debug(
                        f"We fixed an ID from the imputaion file: {v.POS}: {v.ID} {x.ID}")
                    v.ID = x.ID
                else:
                    logging.info(f"Same positions, different id: {v.POS}: {v.ID} {x.ID}")
                    imputed_snps_to_kil[v.ID] = True
                    imputed_snps_to_kil[x.ID] = True
            else:
                # There are reasons for this (see below)
                if v.ALT == x.ALT:
                    logging.warning(f"WHAT?: {v.ID} {x.ID}")
                    imputed_snps_to_kil[v.ID] = True
                    imputed_snps_to_kil[x.ID] = True

        if v.ID is None:
            logging.debug(
                f"Missing ID in the imputaion file: {v.POS}: {v.ID}")
            # From now on we look at IDs
            continue

        if v.ID in imputed_snps_by_ids:
            x = imputed_snps_by_ids[v.ID]
            imputed_snps_to_kil[v.ID] = True
            imputed_snps_to_kil[x.ID] = True

            # I'd expect anything at this point...
            assert v.CHROM == x.CHROM, v.ID

            # First weirdness
            if v.POS != x.POS:
                dist = v.POS - x.POS
                logging.info(
                    f"Same id, different positions: '{v.ID}': {v.POS}, {x.POS}, {dist}"
                )

            else:
                # Multiple ALT alleles are represented as bi-allelic
                # in the imputation output (each additional ALT allele
                # is put on a new line with the same REF).

                # This would be fine, but how to interpret the actual
                # genotype calls?

                # First, check it's only ever REF or (single) ALT (the
                # file would be invalid VCF otherwise...)
                assert v.genotypes[0][0] in [0, 1], v.ID
                assert v.genotypes[0][1] in [0, 1], v.ID
                assert x.genotypes[0][0] in [0, 1], v.ID
                assert x.genotypes[0][1] in [0, 1], v.ID

                # I've given up trying to interpret the actual
                # genotype, lets just log them:

                what_to_call[ str(v.genotypes[0][0]) +
                              str(v.genotypes[0][1]) +
                              str(x.genotypes[0][0]) +
                              str(x.genotypes[0][1]) ] += 1

        imputed_snps_by_pos[v.CHROM][v.POS] = v.ID
        imputed_snps_by_ids[v.ID] = v

    for genotype, count in what_to_call.items():
        ```Lets see if we can interpret the call...
           0000 = REF/REF
           
           1000 = ALT1/REF
           0100 = REF/ALT1
           
           0010 = ALT2/REF
           0001 = REF/ALT2

           1100 = ALT1/ALT1
           0011 = ALT2/ALT2

           0101 = ALT1/ALT2 ??
           1010 = ALT1/ALT2 ??

           0110 = ??
           1001 = ??

           0111 = ??

           1011 = ??
           1101 = ??
           1110 = ??

           1111 = ??
        ```

           
        print(genotype, count)

