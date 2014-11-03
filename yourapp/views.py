import datetime
from django.core.cache import cache
from django.utils.encoding import force_text
from yourapp.models import Group, Profile
from yourapp.serializers import GroupSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.key_constructor.constructors import (
    DefaultKeyConstructor
)
from rest_framework_extensions.key_constructor.bits import (
    KeyBitBase,
    RetrieveSqlQueryKeyBit,
    ListSqlQueryKeyBit,
    PaginationKeyBit,
    KwargsKeyBit,
    ArgsKeyBit)

class UpdatedAtKeyBit(KeyBitBase):
    def get_data(self, **kwargs):
        key = 'api_updated_at_timestamp'
        value = cache.get(key, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(key, value=value)
        return force_text(value)


class CustomObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class CustomListKeyConstructor(DefaultKeyConstructor):
    args = ArgsKeyBit()
    kwargs = KwargsKeyBit(['territory'])
    all_kwargs = KwargsKeyBit()
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    updated_at = UpdatedAtKeyBit()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @cache_response(key_func=CustomObjectKeyConstructor())
    def retrieve(self, *args, **kwargs):
        return super(GroupViewSet, self).retrieve(*args, **kwargs)

    @cache_response(key_func=CustomListKeyConstructor())
    def list(self, *args, **kwargs):
        return super(GroupViewSet, self).list(*args, **kwargs)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @cache_response(key_func=CustomObjectKeyConstructor())
    def retrieve(self, *args, **kwargs):
        return super(ProfileViewSet, self).retrieve(*args, **kwargs)

    @cache_response(key_func=CustomListKeyConstructor())
    def list(self, *args, **kwargs):
        return super(ProfileViewSet, self).list(*args, **kwargs)
