# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.13
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperMembership(BaseModel):
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
        "super_membership_id": "str",
        "super_fund_id": "str",
        "employee_number": "float",
    }

    attribute_map = {
        "super_membership_id": "SuperMembershipID",
        "super_fund_id": "SuperFundID",
        "employee_number": "EmployeeNumber",
    }

    def __init__(
        self, super_membership_id=None, super_fund_id=None, employee_number=None
    ):  # noqa: E501
        """SuperMembership - a model defined in OpenAPI"""  # noqa: E501

        self._super_membership_id = None
        self._super_fund_id = None
        self._employee_number = None
        self.discriminator = None

        if super_membership_id is not None:
            self.super_membership_id = super_membership_id
        self.super_fund_id = super_fund_id
        self.employee_number = employee_number

    @property
    def super_membership_id(self):
        """Gets the super_membership_id of this SuperMembership.  # noqa: E501

        Xero unique identifier for Super membership  # noqa: E501

        :return: The super_membership_id of this SuperMembership.  # noqa: E501
        :rtype: str
        """
        return self._super_membership_id

    @super_membership_id.setter
    def super_membership_id(self, super_membership_id):
        """Sets the super_membership_id of this SuperMembership.

        Xero unique identifier for Super membership  # noqa: E501

        :param super_membership_id: The super_membership_id of this SuperMembership.  # noqa: E501
        :type: str
        """

        self._super_membership_id = super_membership_id

    @property
    def super_fund_id(self):
        """Gets the super_fund_id of this SuperMembership.  # noqa: E501

        Xero identifier for super fund  # noqa: E501

        :return: The super_fund_id of this SuperMembership.  # noqa: E501
        :rtype: str
        """
        return self._super_fund_id

    @super_fund_id.setter
    def super_fund_id(self, super_fund_id):
        """Sets the super_fund_id of this SuperMembership.

        Xero identifier for super fund  # noqa: E501

        :param super_fund_id: The super_fund_id of this SuperMembership.  # noqa: E501
        :type: str
        """
        if super_fund_id is None:
            raise ValueError(
                "Invalid value for `super_fund_id`, must not be `None`"
            )  # noqa: E501

        self._super_fund_id = super_fund_id

    @property
    def employee_number(self):
        """Gets the employee_number of this SuperMembership.  # noqa: E501

        The memberhsip number assigned to the employee by the super fund.  # noqa: E501

        :return: The employee_number of this SuperMembership.  # noqa: E501
        :rtype: float
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this SuperMembership.

        The memberhsip number assigned to the employee by the super fund.  # noqa: E501

        :param employee_number: The employee_number of this SuperMembership.  # noqa: E501
        :type: float
        """
        if employee_number is None:
            raise ValueError(
                "Invalid value for `employee_number`, must not be `None`"
            )  # noqa: E501

        self._employee_number = employee_number
