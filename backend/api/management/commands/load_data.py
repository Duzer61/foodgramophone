from csv import DictReader

from django.conf import settings as conf_settings
from django.core.management.base import BaseCommand
from recipes.models import Ingredient

#data_dir = '..data/'

csv_files = [
    {'model': Ingredient, 'filename': 'ingredients.csv',
     'fieldnames': ['name', 'measurement_unit']},
]


class Command(BaseCommand):
    help = "Загружает данные из файлов csv"

    def csv_loader(self, cf):
        csv_file = 'static/data/ingredients.csv'#'{}\\data\\{}'.format(data_dir[0], cf['filename'])
        with open(csv_file, encoding='utf-8', newline='') as csvfile:
            reader = DictReader(csvfile, fieldnames=cf['fieldnames'])
            print(f'Загрузка в таблицу модели {cf["model"].__name__}')

            i, err, r = 1, 0, 0

            for row in reader:
                if i != 0:
                    try:
                        id = i  # row.pop('id')
                        cf['model'].objects.update_or_create(
                            id=id, defaults=row)
                        r += 1
                    except Exception as error:
                        print(row)
                        print(
                            f'Ошибка записи в таблицу модели '
                            f'{cf["model"].__name__}, '
                            f'{str(error)}')
                        err += 1
                i += 1
            print(
                f'Всего: {i-1} строк. Загружено: {r} строк. '
                f'Ошибки: {err} строк.')

    def handle(self, *args, **options):
        print("Идет загрузка данных")
        for сf in csv_files:
            self.csv_loader(сf)
        print('Загрука завершена.')
