import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "genevariants.settings")
django.setup()

from variants.models import Gene, Variant

def add_data(path):
    with open(path) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        count = 1
        for row in reader:
            print("Record ", count)
            count += 1
            gene, _ = Gene.objects.get_or_create(name=row['Gene'])
            variant, created = Variant.objects.get_or_create(
                    gene=gene,
                    nucleotide_change=row['Nucleotide Change'],
                    protein_change=row['Protein Change'],
                    other_mappings=row['Other Mappings'],
                    alias=row['Alias'],
                    transcripts=row['Transcripts'],
                    region=row['Region'],
                    reported_classification=row['Reported Classification'],
                    inferred_classification=row['Inferred Classification'],
                    source=row['Source'],
                    last_evaluated=row['Last Evaluated'],
                    last_updated=row['Last Updated'],
                    url=row['URL'],
                    submitter_content=row['Submitter Comment'],
                    assembly=row['Assembly'],
                    chr=row['Chr'],
                    genomic_start=row['Genomic Start'],
                    genomic_stop=row['Genomic Stop'],
                    ref=row['Ref'],
                    alt=row['Alt'],
                    accession=row['Accession'],
                    reported_ref=row['Reported Ref'],
                    reported_alt=row['Reported Alt'],
                )

        # m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23 =\
        # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # for row in reader:
        #     m1 = max(m1, len(row['Nucleotide Change']))
        #     m2 = max(m2, len(row['Protein Change']))
        #     m3 = max(m3, len(row['Other Mappings']))
        #     m4 = max(m4, len(row['Alias']))
        #     m5 = max(m5, len(row['Transcripts']))
        #     m6 = max(m6, len(row['Region']))
        #     m7 = max(m7, len(row['Reported Classification']))
        #     m8 = max(m8, len(row['Inferred Classification']))
        #     m9 = max(m9, len(row['Source']))
        #     m10 = max(m10, len(row['Last Evaluated']))
        #     m11 = max(m11, len(row['Last Updated']))
        #     m12 = max(m12, len(row['URL']))
        #     m13 = max(m13, len(row['Submitter Comment']))
        #     m14 = max(m14, len(row['Assembly']))
        #     m15 = max(m15, len(row['Chr']))
        #     m16 = max(m16, len(row['Genomic Start']))
        #     m17 = max(m17, len(row['Genomic Stop']))
        #     m18 = max(m18, len(row['Ref']))
        #     m19 = max(m19, len(row['Alt']))
        #     m20 = max(m20, len(row['Accession']))
        #     m21 = max(m21, len(row['Reported Ref']))
        #     m22 = max(m22, len(row['Reported Alt']))
        #     m23 = max(m23, len())

        # print("Nucleotide Change", m1)
        # print("Protein Change", m2)
        # print("Other Mappings", m3)
        # print("Alias", m4)
        # print("Transcripts", m5)
        # print("Region", m6)
        # print("Reported Classification", m7)
        # print("Inferred Classification", m8)
        # print("Source", m9)
        # print("Last Evaluated", m10)
        # print("Last Updated", m11)
        # print("URL", m12)
        # print("Submitter Comment", m13)
        # print("Assembly", m14)
        # print("Chr", m15)
        # print("Genomic Start", m16)
        # print("Genomic Stop", m17)
        # print("Ref", m18)
        # print("Alt", m19)
        # print("Accession", m20)
        # print("Reported Ref", m21)
        # print("Reported Alt", m22)
        # print("Gene", m23)

add_data('variants/variants.tsv')