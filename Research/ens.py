
import requests

server = "https://rest.ensembl.org"


def get_ld_populations():
    ext = "/info/variation/populations/homo_sapiens?filter=LD"
    header = {"Content-Type": "application/json"}

    result = requests.get(f"{server}{ext}", headers=header)

    if not result.ok:
        return result.raise_for_status()

    return result.json()


def get_ld(id1, id2, population):
    if isinstance(population, dict):
        population = population['name']

    ext = f"/ld/human/pairwise/{id1}/{id2}?population_name={population}"
    header = {"Content-Type": "application/json"}

    result = requests.get(f"{server}{ext}", headers=header)

    if not result.ok:
        return result.raise_for_status()

    return result.json()
