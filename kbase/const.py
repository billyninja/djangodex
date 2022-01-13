from enum import Enum


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
            (cls.GEN_1, "generation-i"),
            (cls.GEN_2, "generation-ii"),
            (cls.GEN_3, "generation-iii"),
            (cls.GEN_4, "generation-iv"),
            (cls.GEN_5, "generation-v"),
            (cls.GEN_6, "generation-vi"),
            (cls.GEN_7, "generation-vii"),
            (cls.GEN_8, "generation-viii"),
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
            (cls.NORMAL, "normal"),
            (cls.FIGHTING, "fighting"),
            (cls.FLYING, "flying"),
            (cls.POISON, "poison"),
            (cls.GROUND, "ground"),
            (cls.ROCK, "rock"),
            (cls.BUG, "bug"),
            (cls.GHOST, "ghost"),
            (cls.STEEL, "steel"),
            (cls.FIRE, "fire"),
            (cls.WATER, "water"),
            (cls.GRASS, "grass"),
            (cls.ELECTRIC, "electric"),
            (cls.PSYCHIC, "psychic"),
            (cls.ICE, "ice"),
            (cls.DRAGON, "dragon"),
            (cls.DARK, "dark"),
            (cls.FAIRY, "fairy"),
            (cls.UNKNOWN, "unknown"),
            (cls.SHADOW, "shadow"),
        )


class MoveDamageClass(Enum):
    STATUS = 1
    PHYSICAL = 2
    SPECIAL = 3

    @classmethod
    def choices(cls):
        return (
            (cls.STATUS, "status"),
            (cls.PHYSICAL, "physical"),
            (cls.SPECIAL, "special"),
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
            (cls.SPECIFIC_MOVE, "specific-move",),
            (cls.SELECTED_POKEMON_ME_FIRST, "selected-pokemon-me-first",),
            (cls.ALLY, "ally",),
            (cls.USERS_FIELD, "users-field",),
            (cls.USER_OR_ALLY, "user-or-ally",),
            (cls.OPPONENTS_FIELD, "opponents-field",),
            (cls.USER, "user",),
            (cls.RANDOM_OPPONENT, "random-opponent",),
            (cls.ALL_OTHER_POKEMON, "all-other-pokemon",),
            (cls.SELECTED_POKEMON, "selected-pokemon",),
            (cls.ALL_OPPONENTS, "all-opponents",),
            (cls.ENTIRE_FIELD, "entire-field",),
            (cls.USER_AND_ALLIES, "user-and-allies",),
            (cls.ALL_POKEMON, "all-pokemon",),
            (cls.ALL_ALLIES, "all-allies",),
        )
