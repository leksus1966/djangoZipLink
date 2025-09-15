from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL
from .serializers import ShortURLSerializer
from .utils import generate_short_code


class ShortURLCreateView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    def perform_create(self, serializer):
        code = generate_short_code()
        serializer.save(short_code=code)


@api_view(["GET"])
def redirect_view(request, code):
    short_url = get_object_or_404(ShortURL, short_code=code)
    return redirect(short_url.original_url)
