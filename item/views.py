from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


# 카테고리에 따른 상품 보기 GET
class ItemAPIView(APIView):
    def get(self,request): 
        
        return Response(status=status.HTTP_200_OK)

    def post(self,request):

        return Response(status=status.HTTP_200_OK)
