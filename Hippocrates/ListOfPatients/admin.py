from django.contrib import admin

from .models import ListPatPageOne


class ListPatPageOneAdmin(admin.ModelAdmin):
    list_display = ('Date', 'OnStartDay', 'Receive', 'TransferFrom', 'TransferTo', 'ReleaseTotal',
                    'RelTotalTo', 'Die', 'Remain')
    # list_display_links = ('')
    search_fields = ('Date',)


admin.site.register(ListPatPageOne, ListPatPageOneAdmin)
