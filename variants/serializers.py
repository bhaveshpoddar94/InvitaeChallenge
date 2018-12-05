from rest_framework import serializers
from .models import Gene, Variant

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Variant
        fields = ('nucleotide_change', 'protein_change', 'alias', 
                'region', 'reported_classification', 'last_evaluated', 
                'last_updated', 'url', 'source', 'other_mappings')

class GeneListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Gene
        fields = ('id', 'name')

class GeneDetailSerializer(serializers.ModelSerializer):
    variant_set = VariantSerializer(many=True, read_only=True)

    class Meta:
        model  = Gene
        fields = ('id', 'name', 'modified', 'variant_set')
