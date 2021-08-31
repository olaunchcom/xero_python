# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Payment(BaseModel):
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
        "invoice": "Invoice",
        "credit_note": "CreditNote",
        "prepayment": "Prepayment",
        "overpayment": "Overpayment",
        "invoice_number": "str",
        "credit_note_number": "str",
        "account": "Account",
        "code": "str",
        "date": "date[ms-format]",
        "currency_rate": "float",
        "amount": "float",
        "bank_amount": "float",
        "reference": "str",
        "is_reconciled": "bool",
        "status": "str",
        "payment_type": "str",
        "updated_date_utc": "datetime[ms-format]",
        "payment_id": "str",
        "batch_payment_id": "str",
        "bank_account_number": "str",
        "particulars": "str",
        "details": "str",
        "has_account": "bool",
        "has_validation_errors": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "invoice": "Invoice",
        "credit_note": "CreditNote",
        "prepayment": "Prepayment",
        "overpayment": "Overpayment",
        "invoice_number": "InvoiceNumber",
        "credit_note_number": "CreditNoteNumber",
        "account": "Account",
        "code": "Code",
        "date": "Date",
        "currency_rate": "CurrencyRate",
        "amount": "Amount",
        "bank_amount": "BankAmount",
        "reference": "Reference",
        "is_reconciled": "IsReconciled",
        "status": "Status",
        "payment_type": "PaymentType",
        "updated_date_utc": "UpdatedDateUTC",
        "payment_id": "PaymentID",
        "batch_payment_id": "BatchPaymentID",
        "bank_account_number": "BankAccountNumber",
        "particulars": "Particulars",
        "details": "Details",
        "has_account": "HasAccount",
        "has_validation_errors": "HasValidationErrors",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        invoice=None,
        credit_note=None,
        prepayment=None,
        overpayment=None,
        invoice_number=None,
        credit_note_number=None,
        account=None,
        code=None,
        date=None,
        currency_rate=None,
        amount=None,
        bank_amount=None,
        reference=None,
        is_reconciled=None,
        status=None,
        payment_type=None,
        updated_date_utc=None,
        payment_id=None,
        batch_payment_id=None,
        bank_account_number=None,
        particulars=None,
        details=None,
        has_account=False,
        has_validation_errors=False,
        status_attribute_string=None,
        validation_errors=None,
    ):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501

        self._invoice = None
        self._credit_note = None
        self._prepayment = None
        self._overpayment = None
        self._invoice_number = None
        self._credit_note_number = None
        self._account = None
        self._code = None
        self._date = None
        self._currency_rate = None
        self._amount = None
        self._bank_amount = None
        self._reference = None
        self._is_reconciled = None
        self._status = None
        self._payment_type = None
        self._updated_date_utc = None
        self._payment_id = None
        self._batch_payment_id = None
        self._bank_account_number = None
        self._particulars = None
        self._details = None
        self._has_account = None
        self._has_validation_errors = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        if invoice is not None:
            self.invoice = invoice
        if credit_note is not None:
            self.credit_note = credit_note
        if prepayment is not None:
            self.prepayment = prepayment
        if overpayment is not None:
            self.overpayment = overpayment
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if credit_note_number is not None:
            self.credit_note_number = credit_note_number
        if account is not None:
            self.account = account
        if code is not None:
            self.code = code
        if date is not None:
            self.date = date
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if amount is not None:
            self.amount = amount
        if bank_amount is not None:
            self.bank_amount = bank_amount
        if reference is not None:
            self.reference = reference
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if status is not None:
            self.status = status
        if payment_type is not None:
            self.payment_type = payment_type
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if payment_id is not None:
            self.payment_id = payment_id
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if particulars is not None:
            self.particulars = particulars
        if details is not None:
            self.details = details
        if has_account is not None:
            self.has_account = has_account
        if has_validation_errors is not None:
            self.has_validation_errors = has_validation_errors
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def invoice(self):
        """Gets the invoice of this Payment.  # noqa: E501


        :return: The invoice of this Payment.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Payment.


        :param invoice: The invoice of this Payment.  # noqa: E501
        :type: Invoice
        """

        self._invoice = invoice

    @property
    def credit_note(self):
        """Gets the credit_note of this Payment.  # noqa: E501


        :return: The credit_note of this Payment.  # noqa: E501
        :rtype: CreditNote
        """
        return self._credit_note

    @credit_note.setter
    def credit_note(self, credit_note):
        """Sets the credit_note of this Payment.


        :param credit_note: The credit_note of this Payment.  # noqa: E501
        :type: CreditNote
        """

        self._credit_note = credit_note

    @property
    def prepayment(self):
        """Gets the prepayment of this Payment.  # noqa: E501


        :return: The prepayment of this Payment.  # noqa: E501
        :rtype: Prepayment
        """
        return self._prepayment

    @prepayment.setter
    def prepayment(self, prepayment):
        """Sets the prepayment of this Payment.


        :param prepayment: The prepayment of this Payment.  # noqa: E501
        :type: Prepayment
        """

        self._prepayment = prepayment

    @property
    def overpayment(self):
        """Gets the overpayment of this Payment.  # noqa: E501


        :return: The overpayment of this Payment.  # noqa: E501
        :rtype: Overpayment
        """
        return self._overpayment

    @overpayment.setter
    def overpayment(self, overpayment):
        """Sets the overpayment of this Payment.


        :param overpayment: The overpayment of this Payment.  # noqa: E501
        :type: Overpayment
        """

        self._overpayment = overpayment

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Payment.  # noqa: E501

        Number of invoice or credit note you are applying payment to e.g.INV-4003  # noqa: E501

        :return: The invoice_number of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Payment.

        Number of invoice or credit note you are applying payment to e.g.INV-4003  # noqa: E501

        :param invoice_number: The invoice_number of this Payment.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def credit_note_number(self):
        """Gets the credit_note_number of this Payment.  # noqa: E501

        Number of invoice or credit note you are applying payment to e.g. INV-4003  # noqa: E501

        :return: The credit_note_number of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._credit_note_number

    @credit_note_number.setter
    def credit_note_number(self, credit_note_number):
        """Sets the credit_note_number of this Payment.

        Number of invoice or credit note you are applying payment to e.g. INV-4003  # noqa: E501

        :param credit_note_number: The credit_note_number of this Payment.  # noqa: E501
        :type: str
        """

        self._credit_note_number = credit_note_number

    @property
    def account(self):
        """Gets the account of this Payment.  # noqa: E501


        :return: The account of this Payment.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Payment.


        :param account: The account of this Payment.  # noqa: E501
        :type: Account
        """

        self._account = account

    @property
    def code(self):
        """Gets the code of this Payment.  # noqa: E501

        Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)  # noqa: E501

        :return: The code of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Payment.

        Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)  # noqa: E501

        :param code: The code of this Payment.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def date(self):
        """Gets the date of this Payment.  # noqa: E501

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :return: The date of this Payment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Payment.

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :param date: The date of this Payment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def currency_rate(self):
        """Gets the currency_rate of this Payment.  # noqa: E501

        Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500  # noqa: E501

        :return: The currency_rate of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this Payment.

        Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500  # noqa: E501

        :param currency_rate: The currency_rate of this Payment.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501

        The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00  # noqa: E501

        :return: The amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.

        The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00  # noqa: E501

        :param amount: The amount of this Payment.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def bank_amount(self):
        """Gets the bank_amount of this Payment.  # noqa: E501

        The amount of the payment in the currency of the bank account.  # noqa: E501

        :return: The bank_amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._bank_amount

    @bank_amount.setter
    def bank_amount(self, bank_amount):
        """Sets the bank_amount of this Payment.

        The amount of the payment in the currency of the bank account.  # noqa: E501

        :param bank_amount: The bank_amount of this Payment.  # noqa: E501
        :type: float
        """

        self._bank_amount = bank_amount

    @property
    def reference(self):
        """Gets the reference of this Payment.  # noqa: E501

        An optional description for the payment e.g. Direct Debit  # noqa: E501

        :return: The reference of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Payment.

        An optional description for the payment e.g. Direct Debit  # noqa: E501

        :param reference: The reference of this Payment.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def is_reconciled(self):
        """Gets the is_reconciled of this Payment.  # noqa: E501

        An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET  # noqa: E501

        :return: The is_reconciled of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        """Sets the is_reconciled of this Payment.

        An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET  # noqa: E501

        :param is_reconciled: The is_reconciled of this Payment.  # noqa: E501
        :type: bool
        """

        self._is_reconciled = is_reconciled

    @property
    def status(self):
        """Gets the status of this Payment.  # noqa: E501

        The status of the payment.  # noqa: E501

        :return: The status of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Payment.

        The status of the payment.  # noqa: E501

        :param status: The status of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORISED", "DELETED", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def payment_type(self):
        """Gets the payment_type of this Payment.  # noqa: E501

        See Payment Types.  # noqa: E501

        :return: The payment_type of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this Payment.

        See Payment Types.  # noqa: E501

        :param payment_type: The payment_type of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ACCRECPAYMENT",
            "ACCPAYPAYMENT",
            "ARCREDITPAYMENT",
            "APCREDITPAYMENT",
            "AROVERPAYMENTPAYMENT",
            "ARPREPAYMENTPAYMENT",
            "APPREPAYMENTPAYMENT",
            "APOVERPAYMENTPAYMENT",
            "None",
        ]  # noqa: E501

        if payment_type:
            if payment_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_type` ({0}), must be one of {1}".format(  # noqa: E501
                        payment_type, allowed_values
                    )
                )

        self._payment_type = payment_type

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Payment.  # noqa: E501

        UTC timestamp of last update to the payment  # noqa: E501

        :return: The updated_date_utc of this Payment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Payment.

        UTC timestamp of last update to the payment  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Payment.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def payment_id(self):
        """Gets the payment_id of this Payment.  # noqa: E501

        The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The payment_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this Payment.

        The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param payment_id: The payment_id of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def batch_payment_id(self):
        """Gets the batch_payment_id of this Payment.  # noqa: E501

        Present if the payment was created as part of a batch.  # noqa: E501

        :return: The batch_payment_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        """Sets the batch_payment_id of this Payment.

        Present if the payment was created as part of a batch.  # noqa: E501

        :param batch_payment_id: The batch_payment_id of this Payment.  # noqa: E501
        :type: str
        """

        self._batch_payment_id = batch_payment_id

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this Payment.  # noqa: E501

        The suppliers bank account number the payment is being made to  # noqa: E501

        :return: The bank_account_number of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this Payment.

        The suppliers bank account number the payment is being made to  # noqa: E501

        :param bank_account_number: The bank_account_number of this Payment.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def particulars(self):
        """Gets the particulars of this Payment.  # noqa: E501

        The suppliers bank account number the payment is being made to  # noqa: E501

        :return: The particulars of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        """Sets the particulars of this Payment.

        The suppliers bank account number the payment is being made to  # noqa: E501

        :param particulars: The particulars of this Payment.  # noqa: E501
        :type: str
        """

        self._particulars = particulars

    @property
    def details(self):
        """Gets the details of this Payment.  # noqa: E501

        The information to appear on the supplier's bank account  # noqa: E501

        :return: The details of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Payment.

        The information to appear on the supplier's bank account  # noqa: E501

        :param details: The details of this Payment.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def has_account(self):
        """Gets the has_account of this Payment.  # noqa: E501

        A boolean to indicate if a contact has an validation errors  # noqa: E501

        :return: The has_account of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._has_account

    @has_account.setter
    def has_account(self, has_account):
        """Sets the has_account of this Payment.

        A boolean to indicate if a contact has an validation errors  # noqa: E501

        :param has_account: The has_account of this Payment.  # noqa: E501
        :type: bool
        """

        self._has_account = has_account

    @property
    def has_validation_errors(self):
        """Gets the has_validation_errors of this Payment.  # noqa: E501

        A boolean to indicate if a contact has an validation errors  # noqa: E501

        :return: The has_validation_errors of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._has_validation_errors

    @has_validation_errors.setter
    def has_validation_errors(self, has_validation_errors):
        """Sets the has_validation_errors of this Payment.

        A boolean to indicate if a contact has an validation errors  # noqa: E501

        :param has_validation_errors: The has_validation_errors of this Payment.  # noqa: E501
        :type: bool
        """

        self._has_validation_errors = has_validation_errors

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Payment.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Payment.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Payment.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Payment.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Payment.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Payment.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Payment.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
