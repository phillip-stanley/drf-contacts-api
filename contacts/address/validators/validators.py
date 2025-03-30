from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError

def validate_uk_postcode(value: str) -> None:
    """Django validator for UK postcodes

    Returns:
        None (raise ValidationError if value is invalid)
    """
    regex = r'^[A-Za-z]{1,2}[0-9][A-Za-z0-9]? [0-9][A-Za-z]{2}$'
    validator = RegexValidator(
        regex=regex,
        message='Enter a valid postcode',
        code='invalid_postcode',
    )

    try:
        validator(value)
    except ValidationError:
        raise ValidationError(
            f'{value} is not a valid postcode',
            code='invalid_postcode',
        )

def validate_uk_mobile(value: str) -> None:
    """Django validator for UK mobile numbers.

    Note:
        Accepts formats:
        - 07123456789
        - 07123 456 789
        - +44712345679
        - +44 7123 456 789

    Returns:
        None (raise ValidationError if value is invalid)
    """
    regex = r'^(?:(?:\+44|0)(?:\s|-)?7(?:\d(?:\s|-)?){9})$'
    validator = RegexValidator(
        regex=regex,
        message="Enter a valid UK mobile number",
        code="invalid_uk_mobile",
    )

    try:
        validator(value)
    except ValidationError:
        raise ValidationError(
            f'%(value)s is not a valid UK mobile number',
            code='invalid_uk_mobile',
        )


def validate_uk_landline(value: str) -> None:
    """Django validator for UK landline numbers.

    Note:
        Accepts formats:
        - 01234567890
        - 01234 456789
        - 01234-456789
    """
    regex = r'^(?:(?:\+44|0)(?:\s|-)?(?:1|2)(?:\d(?:\s|-)?){8,9})$'
    validator = RegexValidator(
        regex=regex,
        message="Enter a valid UK landline number",
        code="invalid_uk_landline",
    )

    try:
        validator(value)
    except ValidationError:
        raise ValidationError(
            f'%(value)s is not a valid UK landline number',
            code='invalid_uk_landline',
        )

