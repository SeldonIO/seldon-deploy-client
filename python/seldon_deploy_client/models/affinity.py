# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Affinity(object):
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
        'node_affinity': 'NodeAffinity',
        'pod_affinity': 'PodAffinity',
        'pod_anti_affinity': 'PodAntiAffinity'
    }

    attribute_map = {
        'node_affinity': 'nodeAffinity',
        'pod_affinity': 'podAffinity',
        'pod_anti_affinity': 'podAntiAffinity'
    }

    def __init__(self, node_affinity=None, pod_affinity=None, pod_anti_affinity=None):  # noqa: E501
        """Affinity - a model defined in Swagger"""  # noqa: E501

        self._node_affinity = None
        self._pod_affinity = None
        self._pod_anti_affinity = None
        self.discriminator = None

        if node_affinity is not None:
            self.node_affinity = node_affinity
        if pod_affinity is not None:
            self.pod_affinity = pod_affinity
        if pod_anti_affinity is not None:
            self.pod_anti_affinity = pod_anti_affinity

    @property
    def node_affinity(self):
        """Gets the node_affinity of this Affinity.  # noqa: E501


        :return: The node_affinity of this Affinity.  # noqa: E501
        :rtype: NodeAffinity
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this Affinity.


        :param node_affinity: The node_affinity of this Affinity.  # noqa: E501
        :type: NodeAffinity
        """

        self._node_affinity = node_affinity

    @property
    def pod_affinity(self):
        """Gets the pod_affinity of this Affinity.  # noqa: E501


        :return: The pod_affinity of this Affinity.  # noqa: E501
        :rtype: PodAffinity
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        """Sets the pod_affinity of this Affinity.


        :param pod_affinity: The pod_affinity of this Affinity.  # noqa: E501
        :type: PodAffinity
        """

        self._pod_affinity = pod_affinity

    @property
    def pod_anti_affinity(self):
        """Gets the pod_anti_affinity of this Affinity.  # noqa: E501


        :return: The pod_anti_affinity of this Affinity.  # noqa: E501
        :rtype: PodAntiAffinity
        """
        return self._pod_anti_affinity

    @pod_anti_affinity.setter
    def pod_anti_affinity(self, pod_anti_affinity):
        """Sets the pod_anti_affinity of this Affinity.


        :param pod_anti_affinity: The pod_anti_affinity of this Affinity.  # noqa: E501
        :type: PodAntiAffinity
        """

        self._pod_anti_affinity = pod_anti_affinity

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
        if issubclass(Affinity, dict):
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
        if not isinstance(other, Affinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other