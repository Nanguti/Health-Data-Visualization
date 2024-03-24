from django.db import models
from locations.models import Location

class DataSource(models.Model):
    name = models.CharField( max_length = 254, unique=True)
    description = models.TextField(blank = True)
    contact_info = models.CharField(max_length = 254, blank = True)

    def __str__(self):
        return self.name

class DataSet(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete = models.CASCADE)
    name = models.CharField(max_length=254)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    uploaded_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Variable(models.Model):
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    name = models.CharField(max_length = 254)
    description = models.TextField(blank=True)
    variable_type = models.CharField(max_length=255, choices=(
        ("Numeric", "Numeric"),
        ("Categorical", "Categorical"),
        ("Date", "Date"),
    ))

    def __str__(self):
        return self.name

class DataPoint(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Data Point ID: {self.id} (Location: {self.location})"

class VariableValue(models.Model):
    dataset = models.ForeignKey(DataSet, on_delete = models.CASCADE )
    variable = models.ForeignKey(Variable, on_delete = models.CASCADE )
    data_point = models.ForeignKey(DataPoint, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits = 10, decimal_places = 2)
    unit = models.CharField(max_length = 254, null = True, blank = True)
