# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.encoded_hash import EncodedHash  # noqa: F401,E501


class OracleQueryResponse(object):
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
        'tx_hash': 'EncodedHash',
        'query_id': 'EncodedHash'
    }

    attribute_map = {
        'tx_hash': 'tx_hash',
        'query_id': 'query_id'
    }

    def __init__(self, tx_hash=None, query_id=None):  # noqa: E501
        """OracleQueryResponse - a model defined in Swagger"""  # noqa: E501

        self._tx_hash = None
        self._query_id = None
        self.discriminator = None

        if tx_hash is not None:
            self.tx_hash = tx_hash
        if query_id is not None:
            self.query_id = query_id

    @property
    def tx_hash(self):
        """Gets the tx_hash of this OracleQueryResponse.  # noqa: E501


        :return: The tx_hash of this OracleQueryResponse.  # noqa: E501
        :rtype: EncodedHash
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this OracleQueryResponse.


        :param tx_hash: The tx_hash of this OracleQueryResponse.  # noqa: E501
        :type: EncodedHash
        """

        self._tx_hash = tx_hash

    @property
    def query_id(self):
        """Gets the query_id of this OracleQueryResponse.  # noqa: E501


        :return: The query_id of this OracleQueryResponse.  # noqa: E501
        :rtype: EncodedHash
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this OracleQueryResponse.


        :param query_id: The query_id of this OracleQueryResponse.  # noqa: E501
        :type: EncodedHash
        """

        self._query_id = query_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OracleQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
