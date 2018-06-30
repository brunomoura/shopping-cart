from rest_framework import serializers


class CustomHyperLinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """Custom HyperlinkedModelSerializer to support url namespace"""

    api_version = ''

    def build_url_field(self, field_name, model_class):

        field_class, field_kwargs = super(CustomHyperLinkedModelSerializer, self).\
            build_url_field(field_name, model_class)

        field_kwargs['view_name'] = 'api:{}:{}'.format(
            self.api_version, field_kwargs['view_name']
        )

        return field_class, field_kwargs


class V1HyperLinkedModelSerializer(CustomHyperLinkedModelSerializer):

    api_version = 'v1'
