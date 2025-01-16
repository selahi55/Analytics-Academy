from django import template

register = template.Library()

@register.filter
def attr(obj, field_name):
    """
    Template filter to dynamically access object attributes.
    """
    value = getattr(obj, field_name, None)
    field = obj._meta.get_field(field_name)
    
    # Handle choice fields
    if hasattr(field, 'choices') and field.choices:
        value = dict(field.choices).get(value, value)
    
    return value