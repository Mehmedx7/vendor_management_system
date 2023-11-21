from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from faker import Faker
from django.utils import timezone

# fake = Faker()

# def create_vendor_with_related_data():
#     vendor = Vendor.objects.create(
#         name=fake.company(),
#         contact_details=fake.address(),
#         address=fake.address(),
#         vendor_code=fake.unique.random_number(digits=8),
#         on_time_delivery_rate=fake.random_number(digits=2),
#         quality_rating_avg=fake.random_number(digits=2),
#         average_response_time=fake.random_number(digits=2),
#         fulfillment_rate=fake.random_number(digits=2),
#     )

#     purchase_order = PurchaseOrder.objects.create(
#         po_number=fake.unique.random_number(digits=8),
#         vendor=vendor,
#         order_date=fake.date_time_this_decade(),
#         delivery_date=fake.date_time_this_decade(),
#         items=[{"name": fake.word(), "price": fake.random_number(digits=3)} for _ in range(3)],
#         quantity=fake.random_number(digits=2),
#         status=fake.random_element(elements=("Pending", "Shipped", "Delivered")),
#         quality_rating=fake.random_number(digits=2),
#         issue_date=fake.date_time_this_decade(),
#         acknowledgment_date=fake.date_time_this_decade(),
#     )

#     historical_performance = HistoricalPerformance.objects.create(
#         vendor=vendor,
#         date=fake.date_time_this_decade(),
#         on_time_delivery_rate=fake.random_number(digits=2),
#         quality_rating_avg=fake.random_number(digits=2),
#         average_response_time=fake.random_number(digits=2),
#         fulfillment_rate=fake.random_number(digits=2),
#     )

class VendorListCreateView(generics.ListCreateAPIView):
    # for _ in range(200):
    #     create_vendor_with_related_data()

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id')

        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        return queryset

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceRetrieveView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        acknowledgment_date = self.request.data.get('acknowledgment_date')
        instance = serializer.save(acknowledgment_date=acknowledgment_date)
        instance.acknowledge()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
