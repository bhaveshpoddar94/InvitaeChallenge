from .models import Gene
from .serializers import GeneListSerializer, GeneDetailSerializer, VariantSerializer
from rest_framework import generics
from django.shortcuts import render


class GeneList(generics.ListAPIView):
    serializer_class = GeneListSerializer

    def get_queryset(self):
        """
        Returs gene names, by filtering against the 
        search `term` query parameter in the URL.
        """
        queryset = Gene.objects.all()
        term = self.request.query_params.get('term', None)
        if term is not None:
            queryset = queryset.filter(name__startswith=term)
        return queryset


class GeneDetail(generics.RetrieveAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneDetailSerializer


    
    

