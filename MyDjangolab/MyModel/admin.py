from django.contrib import admin
from MyModel.models import MyDjangoLab, Contact, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class MyDjangoLabAdmin(admin.ModelAdmin):
    list_display = ('name', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('contact', 'name')


class ContactAdmin(admin.ModelAdmin):
    # 自定义表单 只显示 name 和 email 部分
    # fields = ('name', 'email')

    # 在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。我们可以使用内联显示，
    # 让 Tag 附加在 Contact 的编辑页面上显示。
    inlines = [TagInline]

    list_display = ('name', 'age', 'sex', 'email', 'addtime')
    search_fields = ('name', )
    # 将输入栏分块，每个栏也可以定义自己的格式
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse', ),
            'fields': ('sex', 'age'),
        }]
    )



# 注册多个模型并显示
# admin.site.register(MyDjangoLab)
# admin.site.register(Contact)
# admin.site.register(Tag)

# admin.site.register([MyDjangoLab, Contact, Tag])
# admin.site.register([MyDjangoLab, Tag])

admin.site.register(Contact, ContactAdmin)

admin.site.register(MyDjangoLab, MyDjangoLabAdmin)

admin.site.register(Tag, TagAdmin)


