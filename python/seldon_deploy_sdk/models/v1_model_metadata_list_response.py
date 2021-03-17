# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ModelMetadataListResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'models': 'list[V1Model]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'models': 'models',
        'next_page_token': 'nextPageToken'
    }

    def __init__(self, models=None, next_page_token=None):  # noqa: E501
        """V1ModelMetadataListResponse - a model defined in Swagger"""  # noqa: E501

        self._models = None
        self._next_page_token = None
        self.discriminator = None

        if models is not None:
            self.models = models
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def models(self):
        """Gets the models of this V1ModelMetadataListResponse.  # noqa: E501


        :return: The models of this V1ModelMetadataListResponse.  # noqa: E501
        :rtype: list[V1Model]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this V1ModelMetadataListResponse.


        :param models: The models of this V1ModelMetadataListResponse.  # noqa: E501
        :type: list[V1Model]
        """

        self._models = models

    @property
    def next_page_token(self):
        """Gets the next_page_token of this V1ModelMetadataListResponse.  # noqa: E501

        A pagination token returned from a previous call to `List` that indicates from where listing should continue.  # noqa: E501

        :return: The next_page_token of this V1ModelMetadataListResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this V1ModelMetadataListResponse.

        A pagination token returned from a previous call to `List` that indicates from where listing should continue.  # noqa: E501

        :param next_page_token: The next_page_token of this V1ModelMetadataListResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1ModelMetadataListResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ModelMetadataListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other