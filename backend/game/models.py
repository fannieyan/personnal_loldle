# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class ChampionProperties(models.Model):

    class Gender(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'
        OTHER = 'Other'

    class Lane(models.TextChoices):
        BOTTOM = 'Bottom'
        JUNGLE = 'Jungle'
        MIDDLE = 'Middle'
        SUPPORT = 'Support'
        TOP = 'Top'

    class Species(models.TextChoices):
        ASPECT = 'Aspect'
        BRACKERN = 'Brackern'
        CAT = 'Cat'
        CELESTIAL = 'Celestial'
        CHEMICALLY_ALTERED = 'Chemically Altered'
        CYBORG = 'Cyborg'
        DARKIN = 'Darkin'
        DEMON = 'Demon'
        DRAGON = 'Dragon'
        GOD = 'God'
        GOD_WARRIOR = 'God-Warrior'
        GOLEM = 'Golem'
        HUMAN = 'Human'
        ICEBORN = 'Iceborn'
        MAGICALLY_ALTERED = 'Magically Altered'
        MAGICBORN = 'Magicborn'
        MINOTAUR = 'Minotaur'
        RAT = 'Rat'
        REVENANT = 'Revenant'
        SPIRIT = 'Spirit'
        SPIRITUALIST = 'Spiritualist'
        TROLL = "Troll"
        UNDEAD = "Undead"
        UNKNOWN = 'Unknown'
        VASTAYAN = 'Vastayan'
        VOID_BEING = 'Void-Being'
        YETI = 'Yeti'
        Yordle = 'Yordle'

    class Resource(models.TextChoices):
        BLOODTHIRST = 'Bloodthirst'
        COURAGE = 'Courage'
        ENERGY = 'Energy'
        FEROCITY = 'Ferocity'
        FLOW = 'Flow'
        FURY = 'Fury'
        GRIT = 'Grit'
        HEALTH_COST = 'Health costs'
        HEAT = 'Heat'
        MANA = 'Mana'
        MANALESS = 'Manaless'
        RAGE = 'Rage'
        SHIELD = 'Shield'

    class Range(models.TextChoices):
        MELEE = 'Melee'
        RANGED = 'Ranged'

    class Region(models.TextChoices):
        BANDLE_CITY = "Bandle City"
        BILGEWATER = 'Bilgewater'
        CAMAVOR = 'Camavor'
        DEMACIA = 'Demacia'
        FRELJORD = 'Freljord'
        ICATHIA = 'Icathia'
        IONIA = 'Ionia'
        IXTAL = 'Ixtal'
        NOXUS = 'Noxus'
        PILTOVER = 'Piltover'
        RUNTERRA = 'Runeterra'
        SHADOW_ISLES = 'Shadow Isles'
        SHURIMA = 'Shurima'
        TARGON = 'Targon'
        VOID = 'Void'
        ZAUN = 'Zaun'

    champion = models.CharField(primary_key=True, max_length=64)
    gender = models.CharField(blank=True, null=True,
                              max_length=64, choices=Gender.choices)
    lanes = ArrayField(models.CharField(
        blank=True, null=True, max_length=64, choices=Lane.choices))
    species = ArrayField(models.CharField(
        blank=True, null=True, max_length=64, choices=Species.choices))
    resource = models.CharField(
        blank=True, null=True, max_length=64, choices=Resource.choices)
    ranges = ArrayField(models.CharField(
        blank=True, null=True, max_length=64, choices=Range.choices))
    regions = ArrayField(models.CharField(
        blank=True, null=True, max_length=64, choices=Region.choices))
    release_date = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'champion_properties'
