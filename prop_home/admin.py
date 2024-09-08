from django.contrib import admin
from prop_home.models import BlogCategory, Blog, Comment, EmailModel, Privacy, FAQ

class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ("commenter", "created", "comment")
    extra = False

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("label", )
    date_hierarchy = "created"
    empty_value_display = "Empty"
    prepopulated_fields = {"slug": ["label"]}


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    inlines = [CommentInline]

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ["title"]}

@admin.register(EmailModel)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("subject", "from_email", "created")
    readonly_fields = ("subject", "from_email", "name", "phone", "message", "created")


class CustomSolarScheduleAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser and request.user.is_technical

