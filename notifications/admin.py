from django.contrib import admin
from notifications.models import Topic


class TopicAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner',)
    list_display = ('owner', 'name', 'status', 'url')
    list_filter = ('status',)
    search_fields = ('owner__first_name', 'owner__last_name', 'owner__email', 'status', 'name', 'url')


admin.site.register(Topic, TopicAdmin)
