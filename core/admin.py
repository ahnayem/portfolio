from django.contrib import admin
from .models import Contact, PortfolioUpdate, Theme, Skill

# Admin Site Config
admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'bitslab'
admin.site.index_title = 'portfolio'



#classes

class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'subject', 'message', 'date')
    readonly_fields = ('date',)
    list_display = ('name', 'email', 'subject', 'short_msg', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'subject')

class PortfolioUpdateAdmin(admin.ModelAdmin):
    fields = ('user','name', 'title', 'about', 'phone', 'email','city','country','facebook','github','uni','uni_subject','uni_result','uni_passing','clg','clg_group','clg_result','clg_passing','skills','company1','designation1','period1','company2','designation2','period2','theme','image')
    list_display = ('user', 'name', 'title', 'phone', 'email','city','country','theme')
    search_fields = ('user__username',)

class ThemeAdmin(admin.ModelAdmin):
    fields = ('name','html','designer','designerurl','popularity','date')
    list_display = ('name','html','designer','popularity','date')
    list_filter = ('date',)
    search_fields = ('name','html','designer')

class SkillAdmin(admin.ModelAdmin):
    fields = ('name', 'skicon')
    list_display = ('name', 'skicon')
    search_fields = ('name', 'skicon')


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(PortfolioUpdate, PortfolioUpdateAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Skill, SkillAdmin)