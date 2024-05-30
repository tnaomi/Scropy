"""Module

`field_vals`: contains the class textchoices for districts
"""


from django.db import models
from django.utils.translation import gettext_lazy as _


class Distr(models.Model):
    """ Class defining `District`"""
    class district(models.TextChoices):
        """ Class containing text choices for `District`"""
        CHITIPA = "CP", _("Chitipa")
        KARONGA = "KNG", _("Karonga")
        MZIMBA = "MZ", "Mzimba"
        RUMPHI = "RU", _("Rumphi") 
        NKHATABAY = "NB", _("Nkhatabay")
        NKHOTAKOTA = "NK", _("Nkhotakota")
        LIKOMA = "LK", _("Likoma")
        KASUNGU = "KA", _("Karonga")
        DOWA = "DA", _("Dowa")
        NTCHISI = "NT", _("Ntchisi")
        MCHINJI = "MC", _("Mchinji")
        LILONGWE = "LL", _("Lilongwe")
        SALIMA = "SLM", _("Salima")
        DEDZA = "DZ", _("Dedza")
        NTCHEU = "NU", _("Ntcheu")
        MANGOCHI = "MO", _("Mangochi")
        BALAKA = "BLK", _("Balaka")
        MACHINGA = "MA", _("Machinga")
        ZOMBA = "ZA", _("Zomba")
        NENO = "NE", _("Neno")
        MWANZA = "MW", _("Mwanza")
        BLANTYRE = "BT", _("Blantyre")
        CHIRADZULU = "CZ", _("Chiradzulu")
        PHALOMBE = "PH", _("Phalombe")
        THYOLO = "TO", _("Thyolo")
        MULANJE = "MJ", _("Mulanje")
        CHIKHWAWA = "CK", _("Chikhwawa")
        NSANJE = "NS", _("Nsanje")
