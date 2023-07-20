from django.views.generic.base import TemplateView

class IndexTemplateView(TemplateView):
    print("hola")
    template_name = "index.html"