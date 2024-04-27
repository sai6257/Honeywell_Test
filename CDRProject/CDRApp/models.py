from django.db import models

class CallDetailRecord(models.Model):
    call_date = models.DateTimeField()
    caller_number = models.CharField(max_length=20)
    callee_number = models.CharField(max_length=20)
    duration_seconds = models.IntegerField()
    call_cost = models.DecimalField(max_digits=10, decimal_places=2)
