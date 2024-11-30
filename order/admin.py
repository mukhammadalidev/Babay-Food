from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    class Meta:
        model = Order
        fields = '__all__'


admin.site.register(Order,OrderAdmin)