from django.urls import path
from .views import GeneDetail, GeneList

urlpatterns = [
    path('genes/<int:pk>', GeneDetail.as_view()),
    path('genesearch/', GeneList.as_view())
]
