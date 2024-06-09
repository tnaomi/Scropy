"""Module

`field_vals`: contains the class textchoices for districts
"""


from django.db import models
from django.utils.translation import gettext_lazy as _


class Distr(models.Model):
    """ Class defining `District`"""
    class district(models.TextChoices):
        """ Class containing text choices for `District`"""
        CHITIPA = "Chitipa", _("Chitipa")
        KARONGA = "Karonga", _("Karonga")
        MZIMBA = "Mzimba", "Mzimba"
        RUMPHI = "Rumphi", _("Rumphi") 
        NKHATABAY = "Nkhatabay", _("Nkhatabay")
        NKHOTAKOTA = "Nkhotakota", _("Nkhotakota")
        LIKOMA = "Likoma", _("Likoma")
        KASUNGU = "Kasungu", _("Kasungu")
        DOWA = "Dowa", _("Dowa")
        NTCHISI = "Ntchisi", _("Ntchisi")
        MCHINJI = "Mchinji", _("Mchinji")
        LILONGWE = "Lilongwe", _("Lilongwe")
        SALIMA = "Salima", _("Salima")
        DEDZA = "Dedza", _("Dedza")
        NTCHEU = "Ntcheu", _("Ntcheu")
        MANGOCHI = "Mangochi", _("Mangochi")
        BALAKA = "Balaka", _("Balaka")
        MACHINGA = "Machinga", _("Machinga")
        ZOMBA = "Zomba", _("Zomba")
        NENO = "Neno", _("Neno")
        MWANZA = "Mwanza", _("Mwanza")
        BLANTYRE = "Blantyre", _("Blantyre")
        CHIRADZULU = "Chiradzulu", _("Chiradzulu")
        PHALOMBE = "Phalombe", _("Phalombe")
        THYOLO = "Thyolo", _("Thyolo")
        MULANJE = "Mulanje", _("Mulanje")
        CHIKHWAWA = "Chikhwawa", _("Chikhwawa")
        NSANJE = "Nsanje", _("Nsanje")
