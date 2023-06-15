from rest_framework import viewsets, parsers
from .models import Upload
from .serializers import UploadSerializer

class UploadViewset(viewsets.ModelViewSet):
 
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']