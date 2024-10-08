from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from dj_rest_auth.registration.views import RegisterView

from .models import User
from .serializers import UserDetailSerializer, CustomRegisterSerializer
from property.serializers import ReservationsListSerializer


class CustomRegisterView(RegisterView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CustomRegisterSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    
    serializer = ReservationsListSerializer(reservations, many=True)
    
    return JsonResponse(serializer.data, safe=False)