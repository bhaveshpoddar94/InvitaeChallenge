The Invitae Gene Variant Challenge is live at https://intense-temple-88427.herokuapp.com

Features implemented:
1. An endpoint that returns suggestions of gene names starting with some term
2. An endpoint that returns details of a gene along with a list of related genomic variants

Steps to install and run the tests:
1. clone the repository
2. cd into the root directory
3. run "python manage.py migrate"
4. run "python helper.py" (this will populate the database)
5. run "python manage.py test" (this will run the tests)
6. run "python manage.py runserver" (this runs the web app locally)
