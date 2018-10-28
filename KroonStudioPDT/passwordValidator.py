from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re


class ComplexPasswordValidator:
    """
    Validate whether the password contains minimum one uppercase, one digit and one symbol.
    """

    def validate(self, password, user=None):
        # Check for password validity
        if re.search('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', password) is None:
            raise ValidationError(
                _("Your password must contain at least 1 number, 1 uppercase and 1 non-alphanumeric character.."),
                code='password_is_weak',
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 number, 1 uppercase and 1 non-alphanumeric character.")
