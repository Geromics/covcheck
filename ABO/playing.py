from dataclasses import dataclass

@dataclass(frozen=True)
class SNP:
    """Class for SNP data."""
    id: str
    snps: frozenset


x = SNP('rs123', frozenset('AT'))
y = SNP('rs123', frozenset('AT'))
z = SNP('rs123', frozenset('TA'))

print(x)
print(y)
print(z)

assert x == y
assert x == z
assert x is not y

assert x.snps == y.snps
assert x.snps == z.snps

d = dict()

d[x] = 'weee'

assert d[y] == 'weee'
assert d[z] == 'weee'


