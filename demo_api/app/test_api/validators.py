from django.core.exceptions import ValidationError

def validate_number(value):
        if value > 99999:
                raise ValidationError(u'Asegúrese de que este valor tenga menos de 5 dígitos no negativos.')