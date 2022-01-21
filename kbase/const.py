from enum import Enum


class Region(Enum):
    KANTO = 1

    @classmethod
    def choices(cls):
        return ((cls.KANTO.value, "kanto"),)


class Generation(Enum):
    GEN_1 = 1
    GEN_2 = 2
    GEN_3 = 3
    GEN_4 = 4
    GEN_5 = 5
    GEN_6 = 6
    GEN_7 = 7
    GEN_8 = 8

    @classmethod
    def choices(cls):
        return (
            (cls.GEN_1.value, "generation-i"),
            (cls.GEN_2.value, "generation-ii"),
            (cls.GEN_3.value, "generation-iii"),
            (cls.GEN_4.value, "generation-iv"),
            (cls.GEN_5.value, "generation-v"),
            (cls.GEN_6.value, "generation-vi"),
            (cls.GEN_7.value, "generation-vii"),
            (cls.GEN_8.value, "generation-viii"),
        )


class Type(Enum):
    NORMAL = 1
    FIGHTING = 2
    FLYING = 3
    POISON = 4
    GROUND = 5
    ROCK = 6
    BUG = 7
    GHOST = 8
    STEEL = 9
    FIRE = 10
    WATER = 11
    GRASS = 12
    ELECTRIC = 13
    PSYCHIC = 14
    ICE = 15
    DRAGON = 16
    DARK = 17
    FAIRY = 18
    UNKNOWN = 10001
    SHADOW = 10002

    @classmethod
    def choices(cls):
        return (
            (cls.NORMAL.value, "normal"),
            (cls.FIGHTING.value, "fighting"),
            (cls.FLYING.value, "flying"),
            (cls.POISON.value, "poison"),
            (cls.GROUND.value, "ground"),
            (cls.ROCK.value, "rock"),
            (cls.BUG.value, "bug"),
            (cls.GHOST.value, "ghost"),
            (cls.STEEL.value, "steel"),
            (cls.FIRE.value, "fire"),
            (cls.WATER.value, "water"),
            (cls.GRASS.value, "grass"),
            (cls.ELECTRIC.value, "electric"),
            (cls.PSYCHIC.value, "psychic"),
            (cls.ICE.value, "ice"),
            (cls.DRAGON.value, "dragon"),
            (cls.DARK.value, "dark"),
            (cls.FAIRY.value, "fairy"),
            (cls.UNKNOWN.value, "unknown"),
            (cls.SHADOW.value, "shadow"),
        )


class MoveDamageClass(Enum):
    STATUS = 1
    PHYSICAL = 2
    SPECIAL = 3

    @classmethod
    def choices(cls):
        return (
            (cls.STATUS.value, "status"),
            (cls.PHYSICAL.value, "physical"),
            (cls.SPECIAL.value, "special"),
        )


class MoveTarget(Enum):
    SPECIFIC_MOVE = 1
    SELECTED_POKEMON_ME_FIRST = 2
    ALLY = 3
    USERS_FIELD = 4
    USER_OR_ALLY = 5
    OPPONENTS_FIELD = 6
    USER = 7
    RANDOM_OPPONENT = 8
    ALL_OTHER_POKEMON = 9
    SELECTED_POKEMON = 10
    ALL_OPPONENTS = 11
    ENTIRE_FIELD = 12
    USER_AND_ALLIES = 13
    ALL_POKEMON = 14
    ALL_ALLIES = 15

    @classmethod
    def choices(cls):
        return (
            (
                cls.SPECIFIC_MOVE.value,
                "specific-move",
            ),
            (
                cls.SELECTED_POKEMON_ME_FIRST.value,
                "selected-pokemon-me-first",
            ),
            (
                cls.ALLY.value,
                "ally",
            ),
            (
                cls.USERS_FIELD.value,
                "users-field",
            ),
            (
                cls.USER_OR_ALLY.value,
                "user-or-ally",
            ),
            (
                cls.OPPONENTS_FIELD.value,
                "opponents-field",
            ),
            (
                cls.USER.value,
                "user",
            ),
            (
                cls.RANDOM_OPPONENT.value,
                "random-opponent",
            ),
            (
                cls.ALL_OTHER_POKEMON.value,
                "all-other-pokemon",
            ),
            (
                cls.SELECTED_POKEMON.value,
                "selected-pokemon",
            ),
            (
                cls.ALL_OPPONENTS.value,
                "all-opponents",
            ),
            (
                cls.ENTIRE_FIELD.value,
                "entire-field",
            ),
            (
                cls.USER_AND_ALLIES.value,
                "user-and-allies",
            ),
            (
                cls.ALL_POKEMON.value,
                "all-pokemon",
            ),
            (
                cls.ALL_ALLIES.value,
                "all-allies",
            ),
        )


class EncounterMethods(Enum):
    WALK = 1
    SURF = 2
    FISHING = 3

    @classmethod
    def choices(cls):
        return (
            (
                cls.WALK.value,
                "walk",
            ),
            (
                cls.SURF.value,
                "surf",
            ),
            (
                cls.FISHING.value,
                "fishing",
            ),
        )
