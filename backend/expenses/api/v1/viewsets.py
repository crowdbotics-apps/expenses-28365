from rest_framework import authentication
from expenses.models import Expense
from .serializers import ExpenseSerializer
from rest_framework import viewsets


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Expense.objects.all()
