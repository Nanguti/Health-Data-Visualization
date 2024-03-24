from rest_framework import serializers

from .models import DataSource, DataSet, DataPoint, Variable, VariableValue

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = "__all__"

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = '__all__'

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = '__all__'

class VariableValueSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='data_point.location')  
    dataset_name = serializers.CharField(source='variable.dataset.name')
    variable_name = serializers.CharField(source='variable.name')
    class Meta:
        model = VariableValue
        fields = ('id', 'value', 'unit', 'dataset_name', 'variable_name', 'location') 