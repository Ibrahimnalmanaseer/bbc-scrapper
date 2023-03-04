
from rest_framework.generics import ListCreateAPIView
from .serializers import NewsSerializer
from .models import News

class NewsAPIView(ListCreateAPIView):

    
    
   queryset = News.objects.all()
   serializer_class = NewsSerializer

    
        

