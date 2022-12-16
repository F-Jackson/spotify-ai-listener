from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.documentation import DOCS as USER_DOCS
from catalog.documentation import DOCS as CATALOG_DOCS


DOCS = {
    'USER': USER_DOCS,
    'CATALOG': CATALOG_DOCS
}


class DocumentationView(APIView):
    parser_classes = [JSONParser]

    def get(self, request):
        return Response(DOCS)
