from restaurant_finder.models import Restaurant
from django.contrib import admin


# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'address', 'created_at', 'modified_at')

admin.register(Restaurant, RestaurantAdmin)
