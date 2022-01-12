GENERATION_CHOICES = (
    (1, "generation-i"),
    (2, "generation-ii"),
    (3, "generation-iii"),
    (4, "generation-iv"),
    (5, "generation-v"),
    (6, "generation-vi"),
    (7, "generation-vii"),
    (8, "generation-viii"),
)


TYPE_CHOICES = (
    (1, "normal"),
    (2, "fighting"),
    (3, "flying"),
    (4, "poison"),
    (5, "ground"),
    (6, "rock"),
    (7, "bug"),
    (8, "ghost"),
    (9, "steel"),
    (10, "fire"),
    (11, "water"),
    (12, "grass"),
    (13, "electric"),
    (14, "psychic"),
    (15, "ice"),
    (16, "dragon"),
    (17, "dark"),
    (18, "fairy"),
    (10001, "unknown"),
    (10002, "shadow"),
)

MOVE_DAMAGE_CLASS_CHOICES = (
    (1, "status"),
    (2, "physical"),
    (3, "special"),
)

MOVE_TARGET_CHOICES = (
    (1, "specific-move",),
    (2, "selected-pokemon-me-first",),
    (3, "ally",),
    (4, "users-field",),
    (5, "user-or-ally",),
    (6, "opponents-field",),
    (7, "user",),
    (8, "random-opponent",),
    (9, "all-other-pokemon",),
    (10, "selected-pokemon",),
    (11, "all-opponents",),
    (12, "entire-field",),
    (13, "user-and-allies",),
    (14, "all-pokemon",),
    (15, "all-allies",),
)
