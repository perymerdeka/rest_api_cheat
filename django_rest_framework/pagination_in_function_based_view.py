# Resources Docs: https://www.django-rest-framework.org/api-guide/pagination/

from rest_framework.pagination import PageNumberPagination

@api_view(['GET',])

@permission_classes([AllowAny,])

def PersonView(request):

    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = Person.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = PersonSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
