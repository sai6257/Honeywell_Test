from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

class CallDetailRecord(models.Model):
    call_date = models.DateTimeField()
    caller_number = models.CharField(max_length=20)
    callee_number = models.CharField(max_length=20)
    duration_seconds = models.IntegerField()
    call_cost = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
