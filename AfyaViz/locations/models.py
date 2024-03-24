from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=254)
    state_county = models.CharField(max_length=254, null=True, blank=True)
    city_town = models.CharField(max_length=254, blank=True)

    def __str__(self): 
        location_string = self.country
        if self.state_county:
            location_string += f", {self.state_county}"
        if self.city_town:
            location_string += f", {self.city_town}"
        return location_string

    