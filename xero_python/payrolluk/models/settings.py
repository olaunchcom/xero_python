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


class Settings(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "settings": "Accounts",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "settings": "settings",
    }

    def __init__(self, pagination=None, problem=None, settings=None):  # noqa: E501
        """Settings - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._settings = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if settings is not None:
            self.settings = settings

    @property
    def pagination(self):
        """Gets the pagination of this Settings.  # noqa: E501


        :return: The pagination of this Settings.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Settings.


        :param pagination: The pagination of this Settings.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this Settings.  # noqa: E501


        :return: The problem of this Settings.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this Settings.


        :param problem: The problem of this Settings.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def settings(self):
        """Gets the settings of this Settings.  # noqa: E501


        :return: The settings of this Settings.  # noqa: E501
        :rtype: Accounts
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Settings.


        :param settings: The settings of this Settings.  # noqa: E501
        :type: Accounts
        """

        self._settings = settings
