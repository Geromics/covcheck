from dataclasses import dataclass

@dataclass(frozen=True)
class SNP:
    """Class for SNP data."""
    id: str
    snps: frozenset

x = SNP('rs123', frozenset(['A', 'T']))
y = SNP('rs123', frozenset(['A', 'T']))
z = SNP('rs123', frozenset(['T', 'A']))

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


