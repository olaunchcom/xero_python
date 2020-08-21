# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.13
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PaymentLine(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "payment_line_id": "str",
        "amount": "float",
        "account_number": "str",
        "sort_code": "str",
        "account_name": "str",
    }

    attribute_map = {
        "payment_line_id": "paymentLineID",
        "amount": "amount",
        "account_number": "accountNumber",
        "sort_code": "sortCode",
        "account_name": "accountName",
    }

    def __init__(
        self,
        payment_line_id=None,
        amount=None,
        account_number=None,
        sort_code=None,
        account_name=None,
    ):  # noqa: E501
        """PaymentLine - a model defined in OpenAPI"""  # noqa: E501

        self._payment_line_id = None
        self._amount = None
        self._account_number = None
        self._sort_code = None
        self._account_name = None
        self.discriminator = None

        if payment_line_id is not None:
            self.payment_line_id = payment_line_id
        if amount is not None:
            self.amount = amount
        if account_number is not None:
            self.account_number = account_number
        if sort_code is not None:
            self.sort_code = sort_code
        if account_name is not None:
            self.account_name = account_name

    @property
    def payment_line_id(self):
        """Gets the payment_line_id of this PaymentLine.  # noqa: E501

        Xero identifier for payroll payment line  # noqa: E501

        :return: The payment_line_id of this PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._payment_line_id

    @payment_line_id.setter
    def payment_line_id(self, payment_line_id):
        """Sets the payment_line_id of this PaymentLine.

        Xero identifier for payroll payment line  # noqa: E501

        :param payment_line_id: The payment_line_id of this PaymentLine.  # noqa: E501
        :type: str
        """

        self._payment_line_id = payment_line_id

    @property
    def amount(self):
        """Gets the amount of this PaymentLine.  # noqa: E501

        The amount of the payment line  # noqa: E501

        :return: The amount of this PaymentLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentLine.

        The amount of the payment line  # noqa: E501

        :param amount: The amount of this PaymentLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def account_number(self):
        """Gets the account_number of this PaymentLine.  # noqa: E501

        The account number  # noqa: E501

        :return: The account_number of this PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentLine.

        The account number  # noqa: E501

        :param account_number: The account_number of this PaymentLine.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this PaymentLine.  # noqa: E501

        The account sort code  # noqa: E501

        :return: The sort_code of this PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this PaymentLine.

        The account sort code  # noqa: E501

        :param sort_code: The sort_code of this PaymentLine.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def account_name(self):
        """Gets the account_name of this PaymentLine.  # noqa: E501

        The account name  # noqa: E501

        :return: The account_name of this PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PaymentLine.

        The account name  # noqa: E501

        :param account_name: The account_name of this PaymentLine.  # noqa: E501
        :type: str
        """

        self._account_name = account_name
