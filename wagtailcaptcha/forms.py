from __future__ import absolute_import, unicode_literals

import wagtail
from django.utils.module_loading import import_string
from captcha.fields import ReCaptchaField
from .settings import WAGTAIL_RECAPTCHA_WIDGET

if wagtail.VERSION >= (2, 0):
    from wagtail.contrib.forms.forms import FormBuilder
else:
    from wagtail.wagtailforms.forms import FormBuilder


class WagtailCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = "wagtailcaptcha"

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        try:
            recaptcha_widget = import_string(WAGTAIL_RECAPTCHA_WIDGET)
        except ImportError:
            recaptcha_widget = None

        fields = super(WagtailCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(
            label="", widget=recaptcha_widget
        )

        return fields


def remove_captcha_field(form):
    form.fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
    form.cleaned_data.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
