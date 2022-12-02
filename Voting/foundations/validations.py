from django.core.exceptions import ValidationError


def string_validate(value:str):
    if any(map(str.isdigit, value)):
        raise ValidationError(
            ("%(value)s must be letter"),
            params={'value' : value}
        )