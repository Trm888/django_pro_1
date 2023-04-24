import json
import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f_n', '--folder_name', type=str, help='Папка с файлами',
                            default='examples_JSON_files_with_places')

    def handle(self, *args, **options):
        folder_name = options.get('folder_name')
        load_place(folder_name)


def load_place(folder_name):
    current_directory = os.path.join(os.getcwd(), folder_name)
    try:
        file_names = os.listdir(current_directory)
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не существует.")
        return
    for file_name in file_names:
        with open(os.path.join(current_directory, file_name), 'r', encoding='utf-8') as file:
            place = json.load(file)
            obj, created = Place.objects.get_or_create(
                title=place['title'],
                defaults={
                    'short_description': place['description_short'],
                    'long_description': place['description_long'],
                    'lat': place['coordinates']['lng'],
                    'lon': place['coordinates']['lat']
                }
            )
            for index, img_url in enumerate(place['imgs'], start=1):
                img_name = os.path.basename(img_url)
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()
                    if not Image.objects.filter(place=obj, image__contains=img_name).exists():
                        img_content = ContentFile(response.content)
                        image = Image.objects.create(place=obj, image_number=index, image=img_content)
                        image.image.save(img_name, img_content)
                except requests.exceptions.HTTPError:
                    print(f"URL '{img_url}' не существует")
                    continue
