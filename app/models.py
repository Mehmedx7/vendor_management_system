from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def update_performance_metrics(self):
        total_orders = self.purchaseorder_set.count()
        if total_orders > 0:
            self.on_time_delivery_rate = (
                self.purchaseorder_set.filter(status='Delivered').count() / total_orders
            ) * 100
            self.quality_rating_avg = (
                self.purchaseorder_set.exclude(quality_rating__isnull=True)
                .aggregate(models.Avg('quality_rating'))['quality_rating__avg'] or 0
            )
            self.average_response_time = (
                self.purchaseorder_set.exclude(acknowledgment_date__isnull=True)
                .aggregate(models.Avg(models.F('acknowledgment_date') - models.F('order_date')))
                ['acknowledgment_date__avg'].total_seconds() / 3600 or 0
            )
            self.fulfillment_rate = (
                self.purchaseorder_set.filter(status='Fulfilled').count() / total_orders
            ) * 100
        self.save()

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def acknowledge(self):
        if not self.acknowledgment_date:
            self.acknowledgment_date = timezone.now()
            self.save()
            self.vendor.update_performance_metrics()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()