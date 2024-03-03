from django import template

register = template.Library()


@register.filter
def ru_plural(value, variants):
    variants = variants.split(",")
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    else:
        variant = 1

    return variants[variant]
