import requests
from time import sleep
from django.core.management.base import BaseCommand
from kbase.models import Pokemon

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"


def populate_1st_gen(ignore_existing=False):

    _rng = set(range(1, 152))
    if ignore_existing:
        _rng -= set(Pokemon.objects.all().values_list("number", flat=True))

    for num in _rng:
        resp = requests.get(f"{POKEAPI_BASE_URL}pokemon/{num}")
        content = resp.json()

        type2 = None
        if len(content["types"]) > 1:
            type2 = int(content["types"][1]["type"]["url"].split("/")[-2])

        pokemon, created = Pokemon.objects.get_or_create(
            number=num,
            name=content["name"],
            gen_intruduced=1,
            type_1=int(content["types"][0]["type"]["url"].split("/")[-2]),
            type_2=type2,
        )
        print(num, pokemon, created)
        sleep(0.1)
    print("fin.")

class Command(BaseCommand):

    def handle(self, *args, **options):
        populate_1st_gen(ignore_existing=True)
