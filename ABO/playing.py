
from dataclasses import dataclass


# Working on a Genotype class

@dataclass(frozen=True)
class Genotype:
    """A Genotype represents an individuals alleles at a given locus."""
    id: str
    alleles: frozenset

    @classmethod
    def from_string(cls, id, alleles):
        return cls(id, frozenset(alleles))


x = Genotype.from_string('rs123', 'AT')
y = Genotype.from_string('rs123', 'AT')
z = Genotype.from_string('rs123', 'TA')

print(x)
print(y)
print(z)

assert x == y
assert x == z

assert x.alleles == y.alleles
assert x.alleles == z.alleles


# Working towards a Genoset class

# Test using Genotypes as dictionary keys

d = {x: 'weee'}

assert d[y] == 'weee'
assert d[z] == 'weee'


# Test using 'frozenset's of Genotypes as dictionay keys!

a = Genotype.from_string('rs8176719', 'DI')
b = Genotype.from_string('rs8176746', 'AC')
c = Genotype.from_string('rs8176747', 'CG')

print(a.alleles)

p = frozenset([a, b, c])
q = frozenset([c, a, b])

d = {p: 'weee'}

assert d[q] == 'weee'

r = frozenset([a, b])

assert r not in d


# OK

class GenoGroup:
    """A GenoGroup is _several sets_ of Genotypes (genosets)."""

    genogroup = dict()
    phenotype = 'null'

    def __init__(self, genosets, phenotype):
        for genoset in genosets:
            assert genoset not in self.genogroup
            self.genogroup[frozenset(genoset)] = phenotype

    def __str__(self):
        return str(self.genogroup)

genogroup = GenoGroup([frozenset([a, b, c])], 'Type B likely')

print(genogroup)


        

# import json


# with open('abo.json') as fp:
#     j = json.load(fp)

# print(j)


    
