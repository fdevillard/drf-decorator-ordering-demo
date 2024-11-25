# drf-api-view-ordering

A simple demo to illustrate that:
```
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def my_view(request):
        pass
```

is different from:
```
    @permission_classes([IsAuthenticated])
    @api_view(['GET'])
    def my_view(request):
        pass
```

The order of `@api_view` and `@permission_classes` decorators matters, as in the latter the permission is ignored.

## How to run
Install the project
```
poetry install
```

Run Django tests:
```
poetry run python manage.py test
```

This is [clearly stated in the documentation](https://www.django-rest-framework.org/api-guide/views/#api-policy-decorators),
but it's easy to miss and can have huge impact on the security of the API.
