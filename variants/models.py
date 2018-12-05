from django.db import models

class TimeStampedModel(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class Gene(TimeStampedModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Variant(TimeStampedModel):
    nucleotide_change       = models.CharField(max_length=200, default="")
    protein_change          = models.CharField(max_length=100)
    other_mappings          = models.TextField(blank=True)
    alias                   = models.CharField(max_length=80)
    transcripts             = models.TextField(blank=True)
    region                  = models.CharField(max_length=100)
    reported_classification = models.CharField(max_length=100)
    inferred_classification = models.CharField(max_length=100)
    source                  = models.CharField(max_length=10)
    last_evaluated          = models.CharField(max_length=20)
    last_updated            = models.CharField(max_length=20)
    url                     = models.URLField()
    submitter_content       = models.TextField(blank=True)
    assembly                = models.CharField(max_length=10)
    chr                    = models.CharField(max_length=5)
    genomic_start           = models.CharField(max_length=20)
    genomic_stop            = models.CharField(max_length=20)
    ref                     = models.CharField(max_length=100)
    alt                     = models.CharField(max_length=100)
    accession               = models.CharField(max_length=20)
    reported_ref            = models.CharField(max_length=100)
    reported_alt            = models.CharField(max_length=100)
    
    # foreign key
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return '{} : {} : {}'.format(
            self.gene, self.nucleotide_change, 
            self.protein_change)
