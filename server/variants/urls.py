from django.urls import path
from .views import GeneDetail, GeneList
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="variants/index.html")),
    path('genes/<int:pk>', GeneDetail.as_view()),
    path('genesearch/', GeneList.as_view())
]
