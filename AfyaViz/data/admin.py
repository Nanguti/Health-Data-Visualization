from django.contrib import admin
from .models import DataSource, DataPoint, Variable, DataSet, VariableValue

# InlineModelAdmin for nesting VariableValue within DataPoint
class VariableValueInline(admin.TabularInline):
    model = VariableValue
    extra = 1  # Allow adding/removing at least one variable value

class DataPointAdmin(admin.ModelAdmin):
    inlines = [VariableValueInline]
    list_display = ('id', 'location')

admin.site.register(DataSource)
admin.site.register(DataSet)
admin.site.register(Variable)
admin.site.register(DataPoint, DataPointAdmin)