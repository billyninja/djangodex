from django.db import models
from .const import (
    GENERATION_CHOICES,
    TYPE_CHOICES,
    MOVE_DAMAGE_CLASS_CHOICES,
    MOVE_TARGET_CHOICES,
)


class Pokemon(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=32)
    gen_intruduced = models.PositiveSmallIntegerField(choices=GENERATION_CHOICES)

    type_1 = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    type_2 = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, null=True)

    @property
    def types_display(self):
        t2 = f"/{self.type_2}" if self.type_2 else ""
        return f"{self.type_1}{t2}"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Pokemon: #{self.number} {self} {self.types_display}>"


class Move(models.Model):
    name = models.CharField(max_length=32)
    move_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    target = models.PositiveSmallIntegerField(choices=MOVE_TARGET_CHOICES)
    damage_class = models.PositiveSmallIntegerField(choices=MOVE_DAMAGE_CLASS_CHOICES)
    description = models.CharField(max_length=512)
    short_description = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} ({self.type})"

    def __repr__(self):
        return f"<Move: {self}>"


class PokemonMove(models.Model):
    pokemon = models.ForeignKey("kbase.Pokemon", on_delete=models.CASCADE)
    move = models.ForeignKey("kbase.Move", on_delete=models.CASCADE)
    models.PositiveSmallIntegerField(choices=GENERATION_CHOICES)

    class Meta:
        unique_together = ["pokemon", "move"]

    def __str__(self):
        return f"{self.pokemon_id}->{self.move_id}"

    def __repr__(self):
        return f"<PokemonMove: {self}>"
