from rest_framework import serializers
from .models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inquiry
        fields = "__all__"






"""
1. Receive input containing an ID number and loan amount.

2. Verify if the loan amount falls within the specified range defined by the Program. If not, reject the inquiry.

3. Determine the age of the Borrower based on the provided ID number (using the first 6 digits YYMMDD as the DOB). If the age is outside the applicable range, reject the inquiry.

4. Implement a random logic to determine if the individual is a Sole Proprietor (e.g., generate a random boolean value). If the logic indicates they are, reject the inquiry.

5. Check if the ID number is present in the Untrusted List. If it is, reject the inquiry.

6. Save the inquiry as a PreviousApplication.

7. Provide an approval or rejection status and the reason for rejection.
"""