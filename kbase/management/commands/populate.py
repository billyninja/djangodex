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


def _pokemon_and_moves(ignore_existing=False, collect_moves=False):

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
        pokemon, created = Pokemon.objects.update_or_create(
            number=num,
            name=content["name"],
            gen_intruduced=1,
            defauls=dict(
                type_1=_id_from_url(content["types"][0]["type"]["url"]),
                type_2=type2,
                stat_hp=stats.get("hp"),
                stat_attack=stats.get("attack"),
                stat_defense=stats.get("defense"),
                stat_special_attack=stats.get("special-attack"),
                stat_special_defense=stats.get("special-defense"),
                stat_speed=stats.get("speed"),
            ),
        )

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

            move, created = Move.objects.update_or_create(
                name=mov_content["name"],
                defaults=dict(
                    move_type=_id_from_url(mov_content["type"]["url"]),
                    target=_id_from_url(mov_content["target"]["url"]),
                    damage_class=_id_from_url(mov_content["damage_class"]["url"]),
                    description=mov_content["effect_entries"][0]["effect"],
                    short_description=mov_content["effect_entries"][0]["short_effect"],
                    accuracy=mov_content["accuracy"],
                    power=mov_content["power"],
                    pp=mov_content["pp"],
                    priority=mov_content["priority"],
                ),
            )

            print("\t", move, created)
            PokemonMove.objects.get_or_create(pokemon=pokemon, move=move)

        sleep(0.1)
    print("fin.")


def _locations_and_encounters():
    resp = requests.get(f"{POKEAPI_BASE_URL}/region/1/")
    region_content = resp.json()
    for loc in region_content["locations"]:
        print(loc["name"])
        loc_resp = requests.get(loc["url"])
        loc_content = loc_resp.json()
        for area in loc_content["areas"]:
            area_resp = requests.get(area["url"])
            area_content = area_resp.json()
            print("\t", area_content["name"])
            for pkm_encounter in area_content["pokemon_encounters"]:
                pkm_name = pkm_encounter["pokemon"]["name"]
                version_details = [
                    v
                    for v in pkm_encounter["version_details"]
                    if v["version"]["name"] == "yellow"
                ]
                if not version_details:
                    continue

                version_details = version_details[0]
                encounter_details = [
                    e
                    for e in version_details["encounter_details"]
                    if e["method"]["name"]
                    in {"walk", "old-rod", "good-rod", "super-rod]"}
                ]
                if not encounter_details:
                    continue

                methods = [e["method"]["name"] for e in encounter_details]
                print("\t\t", pkm_name, version_details["version"]["name"], methods)
                Pokemon.objects.filter(name=pkm_encounter["pokemon"]["name"])

        print("---")


class Command(BaseCommand):
    def handle(self, *args, **options):
        _locations_and_encounters()
        # _pokemon_and_moves(ignore_existing=False, collect_moves=True)
