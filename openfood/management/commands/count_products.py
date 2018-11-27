from django.core.management.base import BaseCommand, CommandError
from openfood.models import Product, Category, Position
from django.db import models
from datetime import datetime

import sys
import requests


class Counter:
    """
    Just count products and write it on a log file.
    """

    def __init__(self):
        pass

    def count(self):
        total = len(Product.objects.all())
        favorites = len(Product.objects.exclude(favorized=0))
        no_favorites = len(Product.objects.filter(favorized=0))

        print("There is {} products registered in database:".format(total))
        print("\t- {} of them are registered as favorites.".format(favorites))
        print("\t- {} are not registered as favorites.".format(no_favorites))

        



class Command(BaseCommand):
    """
    Django command to refresh data.
    """
    def handle(self, *args, **options):
        counter = Counter()

        orig_stdout = sys.stdout

        if 'win' in sys.platform:
            filename = 'refresh_logs/product-count-{}.txt'.format(datetime.strftime(datetime.now(), "%d-%m-%Y@%H-%M-%S"))
        else:
            filename = '/home/gil/oc-projet-10/refresh_logs/product-count-{}.txt'.format(datetime.strftime(datetime.now(), "%d-%m-%Y@%H-%M-%S"))
        
        log = open(filename, 'w')
        sys.stdout = log

        print("Operation started at {}.\n-".format(datetime.strftime(datetime.now(), "%H:%M:%S")))

        counter.count()

        print("-\nOperation ended at {}.".format(datetime.strftime(datetime.now(), "%H:%M:%S")))

        sys.stdout = orig_stdout