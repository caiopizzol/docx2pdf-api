import connexion
import six

from openapi_server.models.file import File  # noqa: E501
from openapi_server.common import util
from openapi_server.common.file_converter import LibreOfficeError, docx2pdf

def file_convert(file):  # noqa: E501
    """converts a DOCX file into PDF

     # noqa: E501

    :param file: method to convert DOCX file into PDF
    :type file: dict | bytes

    :rtype: File
    """
    if connexion.request.is_json:
        file = File.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        out_file = File(file_type = 'PDF')
        out_file.file_base64 = docx2pdf(file.file_base64)
        return out_file.to_dict()

    except LibreOfficeError:
        raise InternalServerErrorError({'message': 'Error when converting file to PDF'})
    