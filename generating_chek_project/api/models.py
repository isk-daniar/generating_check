from django.db import models
from django.contrib.postgres.fields import JSONField


CHECK_TYPE = [
    ('kitchen', 'kitchen'),
    ('client', 'client')
]

STATUS = [
    ('new', 'new'),
    ('rendered', 'rendered'),
    ('printed', 'printed')
]


class Printer(models.Model):
    """ Принтер """

    name = models.CharField('название принтера', max_length=100)
    api_key = models.CharField('ключ доступа к API',max_length=100)
    check_type = models.CharField('тип чека которые печатает принтер', max_length=10, choices=CHECK_TYPE)
    point_id = models.IntegerField('точка к которой привязан принтер')

    def __str__(self):
        return f"{self.name} {self.point_id}"


class Check(models.Model):
    """ Чек """

    printer_id = models.ForeignKey(Printer, verbose_name='принтер', on_delete=models.CASCADE, blank=True)
    type = models.CharField('тип чека', max_length=10, choices=CHECK_TYPE)
    order = JSONField('информация о заказе')
    status = models.CharField('статус чека', max_length=10, choices=STATUS)
    pdf_file = models.FileField('ссылка на созданный PDF-файл')

