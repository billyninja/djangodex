# Generated by Django 3.2.11 on 2022-01-13 00:41

from django.db import migrations, models
import django.db.models.deletion
import kbase.const


class Migration(migrations.Migration):

    dependencies = [
        ('kbase', '0003_alter_move_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='stat_attack',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stat_defense',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stat_hp',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stat_special_attack',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stat_special_defense',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stat_speed',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='damage_class',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.MoveDamageClass['STATUS'], 'status'), (kbase.const.MoveDamageClass['PHYSICAL'], 'physical'), (kbase.const.MoveDamageClass['SPECIAL'], 'special')]),
        ),
        migrations.AlterField(
            model_name='move',
            name='move_type',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.Type['NORMAL'], 'normal'), (kbase.const.Type['FIGHTING'], 'fighting'), (kbase.const.Type['FLYING'], 'flying'), (kbase.const.Type['POISON'], 'poison'), (kbase.const.Type['GROUND'], 'ground'), (kbase.const.Type['ROCK'], 'rock'), (kbase.const.Type['BUG'], 'bug'), (kbase.const.Type['GHOST'], 'ghost'), (kbase.const.Type['STEEL'], 'steel'), (kbase.const.Type['FIRE'], 'fire'), (kbase.const.Type['WATER'], 'water'), (kbase.const.Type['GRASS'], 'grass'), (kbase.const.Type['ELECTRIC'], 'electric'), (kbase.const.Type['PSYCHIC'], 'psychic'), (kbase.const.Type['ICE'], 'ice'), (kbase.const.Type['DRAGON'], 'dragon'), (kbase.const.Type['DARK'], 'dark'), (kbase.const.Type['FAIRY'], 'fairy'), (kbase.const.Type['UNKNOWN'], 'unknown'), (kbase.const.Type['SHADOW'], 'shadow')]),
        ),
        migrations.AlterField(
            model_name='move',
            name='target',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.MoveTarget['SPECIFIC_MOVE'], 'specific-move'), (kbase.const.MoveTarget['SELECTED_POKEMON_ME_FIRST'], 'selected-pokemon-me-first'), (kbase.const.MoveTarget['ALLY'], 'ally'), (kbase.const.MoveTarget['USERS_FIELD'], 'users-field'), (kbase.const.MoveTarget['USER_OR_ALLY'], 'user-or-ally'), (kbase.const.MoveTarget['OPPONENTS_FIELD'], 'opponents-field'), (kbase.const.MoveTarget['USER'], 'user'), (kbase.const.MoveTarget['RANDOM_OPPONENT'], 'random-opponent'), (kbase.const.MoveTarget['ALL_OTHER_POKEMON'], 'all-other-pokemon'), (kbase.const.MoveTarget['SELECTED_POKEMON'], 'selected-pokemon'), (kbase.const.MoveTarget['ALL_OPPONENTS'], 'all-opponents'), (kbase.const.MoveTarget['ENTIRE_FIELD'], 'entire-field'), (kbase.const.MoveTarget['USER_AND_ALLIES'], 'user-and-allies'), (kbase.const.MoveTarget['ALL_POKEMON'], 'all-pokemon'), (kbase.const.MoveTarget['ALL_ALLIES'], 'all-allies')]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gen_intruduced',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.Generation['GEN_1'], 'generation-i'), (kbase.const.Generation['GEN_2'], 'generation-ii'), (kbase.const.Generation['GEN_3'], 'generation-iii'), (kbase.const.Generation['GEN_4'], 'generation-iv'), (kbase.const.Generation['GEN_5'], 'generation-v'), (kbase.const.Generation['GEN_6'], 'generation-vi'), (kbase.const.Generation['GEN_7'], 'generation-vii'), (kbase.const.Generation['GEN_8'], 'generation-viii')]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_1',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.Type['NORMAL'], 'normal'), (kbase.const.Type['FIGHTING'], 'fighting'), (kbase.const.Type['FLYING'], 'flying'), (kbase.const.Type['POISON'], 'poison'), (kbase.const.Type['GROUND'], 'ground'), (kbase.const.Type['ROCK'], 'rock'), (kbase.const.Type['BUG'], 'bug'), (kbase.const.Type['GHOST'], 'ghost'), (kbase.const.Type['STEEL'], 'steel'), (kbase.const.Type['FIRE'], 'fire'), (kbase.const.Type['WATER'], 'water'), (kbase.const.Type['GRASS'], 'grass'), (kbase.const.Type['ELECTRIC'], 'electric'), (kbase.const.Type['PSYCHIC'], 'psychic'), (kbase.const.Type['ICE'], 'ice'), (kbase.const.Type['DRAGON'], 'dragon'), (kbase.const.Type['DARK'], 'dark'), (kbase.const.Type['FAIRY'], 'fairy'), (kbase.const.Type['UNKNOWN'], 'unknown'), (kbase.const.Type['SHADOW'], 'shadow')]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_2',
            field=models.PositiveSmallIntegerField(choices=[(kbase.const.Type['NORMAL'], 'normal'), (kbase.const.Type['FIGHTING'], 'fighting'), (kbase.const.Type['FLYING'], 'flying'), (kbase.const.Type['POISON'], 'poison'), (kbase.const.Type['GROUND'], 'ground'), (kbase.const.Type['ROCK'], 'rock'), (kbase.const.Type['BUG'], 'bug'), (kbase.const.Type['GHOST'], 'ghost'), (kbase.const.Type['STEEL'], 'steel'), (kbase.const.Type['FIRE'], 'fire'), (kbase.const.Type['WATER'], 'water'), (kbase.const.Type['GRASS'], 'grass'), (kbase.const.Type['ELECTRIC'], 'electric'), (kbase.const.Type['PSYCHIC'], 'psychic'), (kbase.const.Type['ICE'], 'ice'), (kbase.const.Type['DRAGON'], 'dragon'), (kbase.const.Type['DARK'], 'dark'), (kbase.const.Type['FAIRY'], 'fairy'), (kbase.const.Type['UNKNOWN'], 'unknown'), (kbase.const.Type['SHADOW'], 'shadow')], null=True),
        ),
        migrations.AlterField(
            model_name='pokemonmove',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moveset', to='kbase.pokemon'),
        ),
    ]
