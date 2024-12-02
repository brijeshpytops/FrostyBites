from datetime import datetime
from django import template

register = template.Library()  # This is required for Django to register the filter

@register.filter
def format_datetime_iso(value):
    try:
        # Parse the ISO format and convert to datetime
        dt = datetime.fromisoformat(value.rstrip("Z"))
        # Format it with AM/PM notation
        return dt.strftime('%d-%b-%Y %I:%M:%S %p')
    except Exception as e:
        return value  # Return the original value if parsing fails
