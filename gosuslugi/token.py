from rest_framework.authtoken.models import Token

token = Token.objects.create(user=123)
print(token.key)
