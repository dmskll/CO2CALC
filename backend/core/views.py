from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class CurrentUserView(APIView):
    def get(self, request):
        user = request.user
        print("!!!!!!!!")
        print(user.username)
        if user.is_authenticated:
            return Response({
                'username': user.username,
                'email': user.email,
                'authenticated': True
            })
        #en caso de que no esté loggeado
        return Response({
            'authenticated': False
        })
        
