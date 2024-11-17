from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin
from rest_framework.reverse import reverse

from network.models import Contacts, Network


def clear_arrears(modeladmin, request, queryset):
    """Функция, которая обнуляет задолженность"""
    queryset.update(arrears=None)


clear_arrears.short_description = "Очистить задолженность"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city',)
    list_filter = ('country',)


@admin.register(Network)
class NetworkAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'contacts_country', 'supplier_link', 'arrears', 'level',)
    list_filter = ('contacts__city',)
    actions = (clear_arrears,)

    @admin.display(description='Поставщик')
    def supplier_link(self, obj):
        """Метод добавляет ссылку на «Поставщика»"""
        if obj.supplier:
            link = reverse("admin:network_network_change", args=[obj.supplier_id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)

    @admin.display(ordering='contacts__county',
                   description='Страна')
    def contacts_country(self, obj):
        """Метод возвращает отображение поля «Страна» модели «Контакты»"""
        return obj.contacts.country
