from django.db import models
from .const import (
    Generation,
    Type,
    MoveDamageClass,
    MoveTarget,
)


class Pokemon(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=32)
    gen_intruduced = models.PositiveSmallIntegerField(choices=Generation.choices())

    type_1 = models.PositiveSmallIntegerField(choices=Type.choices())
    type_2 = models.PositiveSmallIntegerField(choices=Type.choices(), null=True)

    stat_hp = models.PositiveSmallIntegerField(default=1)
    stat_attack = models.PositiveSmallIntegerField(default=1)
    stat_defense = models.PositiveSmallIntegerField(default=1)
    stat_special_attack = models.PositiveSmallIntegerField(default=1)
    stat_special_defense = models.PositiveSmallIntegerField(default=1)
    stat_speed = models.PositiveSmallIntegerField(default=1)

    @property
    def types_display(self):
        t2 = f"/{self.type_2}" if self.type_2 else ""
        return f"{self.type_1}{t2}"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Pokemon: #{self.number} {self} {self.types_display}>"


class Move(models.Model):
    name = models.CharField(max_length=32, unique=True)
    move_type = models.PositiveSmallIntegerField(choices=Type.choices())
    target = models.PositiveSmallIntegerField(choices=MoveTarget.choices())
    damage_class = models.PositiveSmallIntegerField(choices=MoveDamageClass.choices())
    description = models.CharField(max_length=512)
    short_description = models.CharField(max_length=128)

    accuracy = models.PositiveSmallIntegerField(null=True)
    power = models.PositiveSmallIntegerField(null=True)
    pp = models.PositiveSmallIntegerField(null=True)
    priority = models.SmallIntegerField(null=True)

    def __str__(self):
        return f"{self.name} ({self.get_move_type_display()})"

    def __repr__(self):
        return f"<Move: {self}>"


class PokemonMove(models.Model):
    pokemon = models.ForeignKey("kbase.Pokemon", on_delete=models.CASCADE, related_name="moveset")
    move = models.ForeignKey("kbase.Move", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["pokemon", "move"]

    def __str__(self):
        return f"{self.pokemon_id}->{self.move_id}"

    def __repr__(self):
        return f"<PokemonMove: {self}>"
