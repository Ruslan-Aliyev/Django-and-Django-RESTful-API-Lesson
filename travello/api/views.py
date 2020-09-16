from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from travello.models import Destination
from travello.api.serializers import DestinationSerializer

@api_view(['GET'])
def api_index(request):
	dests = Destination.objects.all()
	serializer = DestinationSerializer(dests, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def api_dest(request, id):

	try:
		dest = Destination.objects.get(id=id)
	except Destination.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = DestinationSerializer(dest)
	return Response(serializer.data)
	
@api_view(['PUT'])
def api_update(request, id):

	try:
		dest = Destination.objects.get(id=id)
	except Destination.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = DestinationSerializer(dest, data=request.data)

	data = {}

	if serializer.is_valid():
		serializer.save()
		data["success"] = "update successful"
		return Response(data=data)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, id):

	try:
		dest = Destination.objects.get(id=id)
	except Destination.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	operation = dest.delete()
	data = {}

	if operation:
		data["success"] = "delete successful"
	else:
		data["failure"] = "delete failed"

	return Response(data=data)
