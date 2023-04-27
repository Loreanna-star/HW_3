import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for line in phones:
                id = line['id']
                name = line['name']
                image = line['image']
                price = line['price']
                release_date = line['release_date']
                lte_exists = line['lte_exists']
                slug = slugify(name)
                phone = Phone(id, name, image, price, release_date, lte_exists, slug)
                phone.save()
            
