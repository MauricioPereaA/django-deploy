"""Post admin classes"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from posts.models import Post
from django.contrib.auth.models import User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display = (
        'user',
        'profile',
        'title',
        'photo'
    )


    search_fields = (
                     'user__email',
                     'user__first_name',
                     'user__last_name',
                     'user__username',
                    )

    # fieldsets = (
    #     ('Profile', {
    #         'fields': (('user', 'picture'),),
    #     }),
    #     ('Extra Info', {
    #         'fields': (
    #             ('website', 'phone_number'),
    #             ('biography')
    #         )
    #     }),
    #     ('Metadata', {
    #         'fields': (('created', 'modified'),),
    #     })
    # )
    #
    # readonly_fields = ('created', 'modified')
