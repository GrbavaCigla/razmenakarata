from urllib.parse import parse_qs

from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware


# TODO: Secure this
@database_sync_to_async
def get_user_from_session(token_string):
    try:
        user = Token.objects.get(key=token_string).user
    except:
        user = AnonymousUser()
    return user


class TokenAuthMiddleWare(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        query_string = scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        token = query_dict["token"][0]
        user = await get_user_from_session(token)
        scope["user"] = user
        return await super().__call__(scope, receive, send)
