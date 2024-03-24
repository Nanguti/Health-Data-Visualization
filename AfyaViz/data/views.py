from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import DataPoint, DataSet, DataSource, Variable, VariableValue
from .serializers import DataSourceSerializer, DataSetSerializer, VariableSerializer, DataPointSerializer, VariableValueSerializer


class DataSourceList(APIView):
    def get(self, request):
        data_sorces = DataSource.objects.all()
        serializer = DataSourceSerializer(data_sorces, many=True )
        return Response(serializer.data)
    
class DataSourceDetail(APIView):
    def get_object(self, pk):
        try: 
            return DataSource.objects.get(id=pk)
        except DataSource.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        data_source= self.get_object(pk)
        serializer = DataSourceSerializer(data_source)
        return Response(serializer.data)

class DataSetList(APIView):
    def get(self, request):
        dataset =  DataSet.objects.all()
        serializer =  DataSetSerializer(dataset, many=True)
        return Response(serializer.data)

class DataSetDetail(APIView):
    def get_object(self, pk):
        try:
            return DataSet.objects.get(id = pk)
        except DataSet.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        data_set = self.get_object(pk)
        serializer = DataSetSerializer(data_set)
        return Response(serializer.data)

class VariableListByDataset(APIView):
  """
  GET: List all variables associated with a specific dataset by ID.
  """
  def get_object(self, pk): 
    try:
      return DataSet.objects.get(id=pk)
    except DataSet.DoesNotExist:
      raise NotFound

  def get(self, request, pk): 
    dataset = self.get_object(pk)
    variables = dataset.variable_set.all()
    serializer = VariableSerializer(variables, many=True)
    return Response(serializer.data)

class DataPointListByDatasetVariable(APIView):
    """
    GET: List all data points for a specific dataset and variable combination.
    """
    def get_objects(self, dataset_pk, variable_pk):
        try:
            dataset = DataSet.objects.get(pk=dataset_pk)
            variable = dataset.variable_set.get(pk=variable_pk)
            return dataset, variable
        except (DataSet.DoesNotExist, Variable.DoesNotExist):
            raise NotFound

    def get(self, request, dataset_pk, variable_pk):
        dataset, variable = self.get_objects(dataset_pk, variable_pk)
        data_points = DataPoint.objects.filter(dataset=dataset, variable=variable)
        serializer = DataPointSerializer(data_points, many=True)
        return Response(serializer.data)
    

class DataListView(APIView):
    def get(self, request, dataset_id=None, datapoint_id=None):
        if datapoint_id:
            data_values = VariableValue.objects.select_related('data_point__location', 'variable', 'variable__dataset') \
                .filter(data_point__id=datapoint_id)
        elif dataset_id:
            data_values = VariableValue.objects.select_related('data_point__location', 'variable', 'variable__dataset') \
                .filter(variable__dataset__id=dataset_id)
        else:
            data_values = VariableValue.objects.select_related('data_point__location', 'variable', 'variable__dataset')

        serializer = VariableValueSerializer(data_values, many=True)
        return Response(serializer.data)