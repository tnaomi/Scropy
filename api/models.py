""" Module

Contains `District`, `Zone`, `Countries`, `Crops`, `Region` classes.
"""


from django.db import models
from django.utils.translation import gettext_lazy as _
from api.field_vals import Distr

      
class Districts(models.Model):
    """ Defines districts

    Args:
        models (Model): valid models w attributes: `name`

    Returns:
        str: Output a string representation of the `District` object
    """
    name = models.CharField("District name",max_length=15, unique=True, blank=False, choices=Distr.district, default=Distr.district.LILONGWE)   # type: ignore

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """ String representation of District
        """
        return self.name
    
class Zone(models.Model):
    """Create Zone class

    Args:
        models (_model_): _model for instantiating the Zone class_
    """
    name = models.PositiveIntegerField("Zone name as an integer", primary_key=True, blank=False)
    annual_rainfall = models.FloatField("Annual rainfall in mm...")
    avg_temp = models.FloatField("Average temperature...", max_length=4)
    districts = models.ManyToManyField(Districts)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Returns a printable representation of `Zone` """
        return "Zone {:d}".format(self.name)

class Region(models.Model):
    """ Define a Region

    Args:
        models (Model): base model

    Returns:
        obj: Class objects and methods
    """
    class continent(models.TextChoices):
        """ Define the `continent` choices for the `Region` class
        """
        NORTH_AMERICA = "North America", _("North America")
        SOUTH_AMERICA = "South America", _("South America")
        NORTH_EUROPE = "North Europe", _("North Europe")
        CENTRAL_EUROPE = "Central Europe", _("Central Europe")
        EAST_EUROPE = "East Europe", _("East Europe")
        SOUTH_EUROPE = "South Europe", _("South Europe")
        MIDDLE_EAST = "Middle East", _("Middle East")
        AFRICA = "Africa", _("Africa")
        ASIA = "Asia", _("Asia")
        AUSTRALIA = "Australia", _("Australia")
        OCEANIA = "Oceania", _("Oceania")

    name = models.CharField(max_length=20, choices=continent, unique=True, default=continent.AFRICA)  # type: ignore

    class Meta:
        ordering = ['name']
        

    def __str__(self):
        """ Returns a printable representation of `Region` """
        return self.name

class Countries(models.Model):
    """ Defines Countries """
    name = models.CharField("Country name...", max_length=40, blank=False)
    region = models.OneToOneField(Region, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Returns a printable representation of the `countries` object"""
        return self.name
            
class Crops(models.Model):
    """ Create the class `Crops` containing crop info

    Args:
        models (_model): _django models_
    """
    name = models.CharField("Crop name... Singular", max_length=20, blank=False, unique=True)
    genus = models.CharField("Crop genus...", max_length=30, blank=False)
    description = models.TextField(blank=True)
    matures_in = models.FloatField("Matures in...", max_length=5)
    bi_annual = models.BooleanField("Biannual?..", default=True)
    suitable_zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    consumed_in = models.ManyToManyField(Countries)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Returns a printable representation of `Crops` class """
        return self.name