from django.db import models

class Company(models.Model):
    owner = models.CharField(max_length=70)

    def __str__(self):
        return self.owner

class Product(models.Model):
    share_date = models.DateField()
    title = models.CharField(max_length=200)
    prod_content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    # Now you can make migrations and then migrate to create database the database tables automatically

# You can check install_migrate_db directory to make it in command prompt for your OS (Windows, Linux, MacOS etc.)
# Or quickly open your terminal in VsCode by pressing (CTRL + ` or you can go Viev > Terminal) then just apply these
# instructions in your manage.py located directory with example below

# py manage.py makemigrations
# py manage.py migrate

# That's it
