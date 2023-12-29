from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Programs, Borrower, Inquiry, Untrusted
from .serializers import ProgramSerializer, BorrowerSerializer, InquirySerializer
import random
from datetime import datetime


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Programs.objects.all()
    serializer_class = ProgramSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def create(self, request, *args, **kwargs):
        data = request.data


        program = data.get('program')
        borrower = data.get('borrower')
        loan_amount = data.get('loan_amount')
        rejection_reasons = []
        is_approved = True

        # Verify loan amount falls within specified range
        try:
            if not (program.min_amount <= loan_amount <= program.max_amount):
                is_approved = False
                rejection_reasons.append('Loan amount not within specified range')
        except Programs.DoesNotExist:
            return Response({'detail': 'Invalid program ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Determine age of Borrower
        dob_date = datetime.strptime(borrower.date_of_birth, '%Y-%m-%d')
        today = datetime.today()
        borrower_age = today.year - dob_date.year
        if not (program.min_age <= borrower_age <= program.max_age):
            is_approved = False
            rejection_reasons.append('Borrower age not within applicable range')


        # is Sole Proprietor
        is_sole_proprietor = random.choice([True, False])
        if is_sole_proprietor:
            is_approved = False
            rejection_reasons.append('Sole Proprietor cannot apply for loan')

        if Untrusted.objects.filter(identification_number=borrower.identification_number).exists():
            is_approved = False
            rejection_reasons.append('Untrusted ID')

        # Save the inquiry
        inquiry_serializer = self.get_serializer(data=data)
        inquiry_serializer.is_valid(raise_exception=True)
        inquiry = inquiry_serializer.save()

        # Check status of the inquiry
        if is_approved:
            inquiry.status = Inquiry.Status.APPROVED
        else:
            inquiry.status = Inquiry.Status.REJECTED
            inquiry.reason_for_rejection = ', '.join(rejection_reasons)

        inquiry.save()

        return Response({'detail': 'Inquiry processed successfully', 'status': inquiry.status},
                        status=status.HTTP_201_CREATED)