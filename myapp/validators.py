# import os
# from django.core.exceptions import ValidationError

# def validate_file_extension(value):
#     ext = os.path.splitext(value.name)[1]
#     valid_extension = ['pdf','doc','xlsx']

#     if not ext.lower() in valid_extension:
#         raise ValidationError('Unsupported file extension.')

from django.core.exceptions import ValidationError
import os
from django.utils.translation import gettext_lazy as _

def validate_file_size(value):
    filesize= value.size
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.pdf','.doc','.docx']

    if filesize > 10485760:
        raise ValidationError("You cannot upload file more than 10Mb")

    elif not ext.lower() in valid_extension:
        raise ValidationError(f'File format {ext} not suported')

    return value



