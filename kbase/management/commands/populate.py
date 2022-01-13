import requests
from time import sleep
from django.core.management.base import BaseCommand
from kbase.models import Pokemon, Move, PokemonMove

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"


def _id_from_url(url):
    return int(url.split("/")[-2])


def _as_dict(stat_list):
    out = {}
    for stat in stat_list:
        out[stat["stat"]["name"]] = stat["base_stat"]
    return out

def populate_1st_gen(ignore_existing=False, collect_moves=False):

    moves_cache = {}

    _rng = set(range(1, 152))
    if ignore_existing:
        _rng -= set(Pokemon.objects.all().values_list("number", flat=True))

    for num in _rng:
        resp = requests.get(f"{POKEAPI_BASE_URL}pokemon/{num}")
        content = resp.json()
        sleep(0.1)

        type2 = None
        if len(content["types"]) > 1:
            type2 = _id_from_url(content["types"][1]["type"]["url"])

        stats = _as_dict(content["stats"])
        pokemon, created = Pokemon.objects.get_or_create(
            number=num,
            name=content["name"],
            gen_intruduced=1,
            type_1=_id_from_url(content["types"][0]["type"]["url"]),
            type_2=type2,
        )

        pokemon.stat_hp = stats.get("hp")
        pokemon.stat_attack = stats.get("attack")
        pokemon.stat_defense = stats.get("defense")
        pokemon.stat_special_attack = stats.get("special-attack")
        pokemon.stat_special_defense = stats.get("special-defense")
        pokemon.stat_speed = stats.get("speed")
        pokemon.save()

        print(num, pokemon, created)

        if not collect_moves:
            continue

        for mov in content["moves"]:
            mov_content = moves_cache.get(mov["move"]["name"])
            if not mov_content:
                mov_resp = requests.get(mov["move"]["url"])
                mov_content = mov_resp.json()
                moves_cache[mov["move"]["name"]] = mov_content
                sleep(0.1)

            if mov_content["generation"]["name"] != "generation-i":
                continue

            move, created = Move.objects.get_or_create(
                name=mov_content["name"],
                move_type=_id_from_url(mov_content["type"]["url"]),
                target=_id_from_url(mov_content["target"]["url"]),
                damage_class=_id_from_url(mov_content["damage_class"]["url"]),
                description=mov_content["effect_entries"][0]["effect"],
                short_description=mov_content["effect_entries"][0]["short_effect"],
            )

            move.accuracy = mov_content["accuracy"]
            move.power = mov_content["power"]
            move.pp = mov_content["pp"]
            move.priority = mov_content["priority"]

            move.save()

            print("\t", move, created)
            PokemonMove.objects.get_or_create(pokemon=pokemon, move=move)

        sleep(0.1)
    print("fin.")

class Command(BaseCommand):

    def handle(self, *args, **options):
        populate_1st_gen(ignore_existing=False, collect_moves=True)
