from django.db import models


class Person(models.Model):

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'), 
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)

    age = models.DecimalField(decimal_places=0, max_digits=3)

    gender = models.CharField(max_length=1, choices = gender_choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.name + ', ' + str(self.age)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        fields = []
        for field in self._meta.fields:
            if field.name == 'created_at' or field.name == 'updated_at':
                continue
            value = getattr(self, field.name)
            fields.append(f"{field.name}: {value}")
        return f"{self.__class__.__name__}({', '.join(fields)})"



class OwnerFamily(models.Model):
    name = models.CharField(max_length=255)
    net_worth = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'owner families'
    


class Holding(models.Model):
    name = models.CharField(max_length=255)
    net_worth = models.BigIntegerField()
    owner_family = models.OneToOneField(to=OwnerFamily, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=255)
    net_worth = models.BigIntegerField()
    holding = models.ForeignKey(to=Holding, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'companies'
