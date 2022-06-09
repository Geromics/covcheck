
import csv, json

# It's tempting to get into object modeling here, but we're just
# dumping the data to json...

# The term GenoSet is a bit ambiguous, so I use the term GenoGroup to
# mean a list of GenoSets. The original term comes from SNPedia.

genogroup = dict()

with open('abo.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')

    for row in csv_reader:
        #print(row)

        # Unpack the line
        gsid = row['Genoset']
        phenotype = row['Blood Type']

        snp1 = row['SNP1']; a1 = row['A1']; b1 = row['B1'];
        snp2 = row['SNP2']; a2 = row['A2']; b2 = row['B2'];
        snp3 = row['SNP3']; a3 = row['A3']; b3 = row['B3'];

        # Build the dict
        if gsid not in genogroup:
            genogroup[gsid] = dict()
            genogroup[gsid]['id'] = gsid
            genogroup[gsid]['phenotype'] = phenotype
            genogroup[gsid]['genosets'] = []

        # Sanity check (faild for gs???, was gs129)
        assert genogroup[gsid]['phenotype'] == phenotype

        # The meat of the genogroup is a list of genosets
        genogroup[gsid]['genosets'].append(
            {
                snp1: a1 + b1,
                snp2: a2 + b2,
                snp3: a3 + b3
            }
        )

with open('abo.json', 'w') as json_file:
    json.dump(genogroup, json_file)
