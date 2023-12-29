from django.db import models

# Create your models here.

class Programs(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.PositiveIntegerField()
    max_amount = models.PositiveIntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()


class Borrower(models.Model):
    identification_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)


class Inquiry(models.Model):
    class Status(models.IntegerChoices):
        APPROVED = 1, "Approved"
        REJECTED = 2, "Rejected"

    program = models.ForeignKey(Programs, related_name="inquiry_program", on_delete=models.CASCADE)
    borrower= models.ForeignKey(Borrower, related_name="inquiry_borrower", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, null=True, blank=True)
    rejection_reason = models.TextField(null=True, blank=True)

class Untrusted(models.Model):
    identification_number = models.CharField(max_length=20)




"""
Basheer Alsammarraie <basheer@audteye.com>
	
16:15 (27 minutes ago)
	
to me, Süheyb
Task: Implement a Django API for loan inquiries.

Utilize Django and Django REST framework for development and leverage Django Admin for managing app Models.

Models:

Program - Define minimum and maximum loan amounts and the applicable age range.

Borrower - Include an ID number and Date of Birth (DOB).

Inquiry - Record Program, Borrower, Loan Amount, Status (approved or rejected), and reason for rejection.

Untrusted ID - Maintain a list of untrusted ID numbers.

Previous Application - Save all previous loan applications.
"""