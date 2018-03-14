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


class JSONTx(object):
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
        'data_schema': 'str',
        'vsn': 'int'
    }

    attribute_map = {
        'data_schema': 'data_schema',
        'vsn': 'vsn'
    }

    discriminator_value_class_map = {
        'OracleResponseTxJSON': 'OracleResponseTxJSON',
        'CoinbaseTxJSON': 'CoinbaseTxJSON',
        'NameClaimTxObject': 'NameClaimTxObject',
        'NameUpdateTxObject': 'NameUpdateTxObject',
        'NameRevokeTxObject': 'NameRevokeTxObject',
        'NamePreclaimTxObject': 'NamePreclaimTxObject',
        'NameTransferTxObject': 'NameTransferTxObject',
        'SpendTxJSON': 'SpendTxJSON',
        'OracleExtendTxJSON': 'OracleExtendTxJSON',
        'OracleQueryTxJSON': 'OracleQueryTxJSON',
        'OracleRegisterTxJSON': 'OracleRegisterTxJSON'
    }

    def __init__(self, data_schema=None, vsn=None):  # noqa: E501
        """JSONTx - a model defined in Swagger"""  # noqa: E501

        self._data_schema = None
        self._vsn = None
        self.discriminator = 'data_schema'

        self.data_schema = data_schema
        if vsn is not None:
            self.vsn = vsn

    @property
    def data_schema(self):
        """Gets the data_schema of this JSONTx.  # noqa: E501


        :return: The data_schema of this JSONTx.  # noqa: E501
        :rtype: str
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this JSONTx.


        :param data_schema: The data_schema of this JSONTx.  # noqa: E501
        :type: str
        """
        if data_schema is None:
            raise ValueError("Invalid value for `data_schema`, must not be `None`")  # noqa: E501

        self._data_schema = data_schema

    @property
    def vsn(self):
        """Gets the vsn of this JSONTx.  # noqa: E501


        :return: The vsn of this JSONTx.  # noqa: E501
        :rtype: int
        """
        return self._vsn

    @vsn.setter
    def vsn(self, vsn):
        """Sets the vsn of this JSONTx.


        :param vsn: The vsn of this JSONTx.  # noqa: E501
        :type: int
        """

        self._vsn = vsn

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, JSONTx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
