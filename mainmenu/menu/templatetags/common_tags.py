from django import template

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu = Menu.objects.all()
    menu_items = MenuItem.objects.all()
    output = {}
    for menu_item in menu_items:
        if menu_item.parent is None:
            output[str(menu_item.name)] = {"item": menu_item, "sub_menu": []}
        else:

            output[str(menu_item.parent)]["sub_menu"].append(menu_item)

    data = {"data": list(output.values())}

    return {
        "menus": menu,
        "menu_items": menu_items,
        "output": data,
    }