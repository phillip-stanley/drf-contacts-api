from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=f"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",
    message="Invalid phone number"
)
