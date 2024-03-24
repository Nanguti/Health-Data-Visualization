from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Location
from .serializers import LocationSerializer


class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many= True)
        return Response(serializer.data)
    
class LocationDetail(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(id=pk)
        except Location.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    