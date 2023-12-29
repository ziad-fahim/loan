from django.contrib import admin

from loans.models import Inquiry, Untrusted, Borrower, Programs

# Register your models here.

admin.site.register(Inquiry)
admin.site.register(Untrusted)
admin.site.register(Borrower)
admin.site.register(Programs)
