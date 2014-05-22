"""A simple Django templatetag that renders Google Analytics asynchronous
Javascript code.
"""

from django.conf import settings
from django import template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


@register.simple_tag(takes_context=True)
def ganalytics(context):
    """Render Google Analytics tracking code if, and only if, the user has
    defined a ``GANALYTICS_TRACKING_CODE`` setting.
    """
    if hasattr(settings, 'GANALYTICS_TRACKING_CODE') and settings.GANALYTICS_TRACKING_CODE:
        subcontext = Context({ 'GANALYTICS_TRACKING_CODE': settings.GANALYTICS_TRACKING_CODE })
        # Only send User-Id if asked, you will need to accept the corresponding
        # Google TOS beforehand
        if hasattr(settings, 'GANALYTICS_SEND_USER_ID') and settings.GANALYTICS_SEND_USER_ID:
            subcontext['user'] = context['user']
        return get_template('ganalytics/ganalytics.js').render(subcontext)
    return ''
