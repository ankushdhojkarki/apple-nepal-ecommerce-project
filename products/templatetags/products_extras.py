from django import template

# Register the template library
register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    """
    Multiplies the value by the argument (arg).
    Used for simple math in templates.
    """
    try:
        # Convert both to float to ensure correct multiplication, 
        # especially when dealing with decimals like 0.13
        return float(value) * float(arg)
    except (ValueError, TypeError):
        # Handle cases where value or arg aren't numbers (e.g., None, string)
        return ''