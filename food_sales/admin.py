from django.contrib import admin
from .models import Order_Detail

from import_export.admin import ImportExportModelAdmin

from .resources import OrderResource


@admin.register(Order_Detail)
class CommentAdmin(ImportExportModelAdmin):
    resource_class = OrderResource


