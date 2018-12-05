from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Gene, Variant


class GeneSuggestTest(APITestCase):
    """ Test module for GET gene name suggestions API """

    def setUp(self):
        self.gene1 = Gene.objects.create(name='AICD')
        self.gene2 = Gene.objects.create(name='ABEF')

    def test_gene_suggest_one_letter(self):
        response = self.client.get('/api/genesearch/', {"term": 'A'})
        self.assertEqual(response.data,
            [{"id": self.gene1.id, "name": self.gene1.name}, 
             {"id": self.gene2.id, "name": self.gene2.name}])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gene_suggest_two_letters(self):
        response = self.client.get('/api/genesearch/', {"term": 'AB'})
        self.assertEqual(response.data,
            [{"id": self.gene2.id, "name": self.gene2.name}])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gene_suggest_nomatch(self):
        response = self.client.get('/api/genesearch/', {"term": 'Q'})
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GeneVariantsTest(APITestCase):
    def setUp(self):
        self.gene = Gene.objects.create(name='ABCD')
        self.variant1 = Variant.objects.create(
            gene=self.gene,
            nucleotide_change='Nucleotide Change',
            protein_change='Protein Change',
            other_mappings='Other Mappings',
            alias='Alias',
            transcripts='Transcripts',
            region='Region',
            reported_classification='Reported Classification',
            source='Source',
            last_evaluated='Last Evaluated',
            last_updated='Last Updated',
            url='URL')
        self.variant2 = Variant.objects.create(
            gene=self.gene,
            nucleotide_change='Nucleotide Change2',
            protein_change='Protein Change2',
            other_mappings='Other Mappings2',
            alias='Alias2',
            transcripts='Transcripts2',
            region='Region2',
            reported_classification='Reported Classification2',
            source='Source2',
            last_evaluated='Last Evaluated2',
            last_updated='Last Updated2',
            url='URL2')

        def test_endpoint_access(APITestCase):
            response = self.client.get('/api/genes/{}'.format(self.gene.id))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_genedetail_keys(APITestCase):
            response = self.client.get('/api/genes/{}'.format(self.gene.id))
            self.assertCountEqual(response.data.keys(), 
                ["id", "name", "created", "modified", "variant_set"])

        def test_gene_data_except_variant_set(APITestCase):
            response = self.client.get('/api/genes/{}'.format(self.gene.id))
            self.assertEqual(response.data.get("id"), self.gene.id)
            self.assertEqual(response.data.get("name"), self.gene.name)
            self.assertEqual(response.data.get("created"), self.gene.created)
            self.assertEqual(response.data.get("modified"), self.gene.modified)

        def test_variant_set_of_gene(APITestCase):
            response = self.client.get('/api/genes/{}'.format(self.gene.id))
            self.assertEqual(len(response.data.get("variant_set")), 2)
            
            self.assertCountEqual(response.data.get("variant_set")[0],
                ['nucleotide_change', 'protein_change', 'other_mappings',
                'alias', 'region','reported_classification',
                'source', 'last_evaluated', 'last_updated', 'url'])
            
            self.assertCountEqual(response.data.get("variant_set")[1],
                ['nucleotide_change', 'protein_change', 'other_mappings',
                'alias', 'region','reported_classification',
                'source', 'last_evaluated', 'last_updated', 'url'])
            
            self.assertEqual(response.data.get("variant_set")[0], {
                'nucleotide_change': self.variant1.nucleotide_change,
                'protein_change': self.variant1.protein_change,
                'other_mappings': self.variant1.other_mappings,
                'alias': self.variant1.alias,
                'region': self.variant1.region,
                'reported_classification': self.variant1.reported_classification,
                'source': self.variant1.source,
                'last_evaluated': self.variant1.last_evaluated,
                'last_updated': self.variant1.last_updated,
                'url': self.variant1.url
            })
        
        def test_invalid_request(APITestCase):
            response = self.client.get('/api/genes/{}'.format(self.gene.id+1))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)