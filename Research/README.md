
Grabbed data from the original paper here:
https://www.nature.com/articles/s41586-021-03767-x

Converted to a gugu doc here:
https://docs.google.com/spreadsheets/d/1UcG3Sz0x5sejRaGAFyz_EAcK3ojTgCu4w3x_UW0w8t0


Copied the table on the 'Supp Table 2 - Meta results' sheet here:
https://docs.google.com/spreadsheets/d/1pBZsgRqJ6q8LWzTs7UTiohzkJoHmiNRo2r0GZIjZ8kE



These are the SNPs of interest:
rs2271616
rs10490770
rs11919389
rs1886814
rs72711165
rs912805253
rs10774671
rs1819040
rs77534576
rs2109069
rs74956615
rs4801778
rs13050728


Need to find the haploblocks that they are on (across populations) and
find the 23andMe SNPs that are on those haploblocks...

OK, lets do it...



virtualenv mypy

. mypy/bin/activate

pip install PyVCF

