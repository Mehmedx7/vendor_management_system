from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/acknowledge/', PurchaseOrderAcknowledgeView.as_view(), name='purchase_order_acknowledge'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('api/vendors/<int:pk>/performance/', HistoricalPerformanceRetrieveView.as_view(), name='historical-performance-retrieve'),
]
