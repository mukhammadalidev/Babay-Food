from django.contrib import admin
from .models import Basket,BasketItem
# Register your models here.
class  BasketItemInline(admin.TabularInline):
    model = BasketItem
    extra = 1


class BasketAdmin(admin.ModelAdmin):
    inlines = [BasketItemInline]

    class Meta:
        model = Basket
        fields = '__all__'



admin.site.register(Basket,BasketAdmin)