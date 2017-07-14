import calendar
import uuid
from datetime import date,time,timezone
from django.contrib.auth.models import User
from django.db import models
def calc_category_value(instance):
    today = date.today()
    days = calendar.monthrange(today.year,today.month)[1]
    range_start = "%s-%s-%s" % (today.year,today.month,1)
    range_end = "%s-%s-%s" % (today.year,today.month,days)
    category = Category.objects.get(id=instance.category.id)
    expenses = Expense.objects.filter(date__range=[range_start,range_end],category=category)
    total = 0
    for e in expenses:
        total += e.amount
    category.value = total
    category.save()

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date added', auto_now_add=True)
    modify_date = models.DateTimeField('date modified', default=timezone.now)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    value = models.DecimalField(max_digits=11,decimal_places=2, default=0)
    create_date = models.DateTimeField('date added', auto_now_add=True)
    modify_date = models.DateTimeField('date modified', default=timezone.now)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name + ' (' + str(self.value) + ')'


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    create_date = models.DateTimeField('date added', auto_now_add=True)
    modify_date = models.DateTimeField('date modified', default=timezone.now)

    def save(self, *args, **kwargs):
        super(Expense, self).save(*args, **kwargs)
        today = date.today()
        days = calendar.monthrange(today.year, today.month)[1]
        range_start = "%s-%s-%s" % (today.year, today.month, 1)
        range_end = "%s-%s-%s" % (today.year, today.month, days)
        expenses = Expense.objects.filter(date__range=[range_start, range_end], category=self.category)
        total = 0
        for e in expenses:
            total += e.amount
        self.category.value = total
        self.category.save()

        class Meta:
            verbose_name_plural = "Expenses"
            order_with_respect_to = 'category'

        def __unicode__(self):
            return self.title + ', ' + str(self.amount) + ' (' + self.category.name + ')'