from django.conf import settings
WAGTAIL_RECAPTCHA_WIDGET = getattr(
    settings, "WAGTAIL_RECAPTCHA_WIDGET", "captcha.widgets.ReCaptchaV2Checkbox"
)

