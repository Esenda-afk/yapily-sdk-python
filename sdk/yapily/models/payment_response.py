# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.319
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PaymentResponse(object):
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
        'id': 'str',
        'institution_consent_id': 'str',
        'payment_idempotency_id': 'str',
        'payment_lifecycle_id': 'str',
        'status': 'str',
        'status_details': 'PaymentStatusDetails',
        'payer': 'Payer',
        'payee_details': 'Payee',
        'reference': 'str',
        'amount': 'float',
        'currency': 'str',
        'amount_details': 'Amount',
        'created_at': 'datetime',
        'first_payment_amount': 'Amount',
        'first_payment_date_time': 'datetime',
        'next_payment_amount': 'Amount',
        'next_payment_date_time': 'datetime',
        'final_payment_amount': 'Amount',
        'final_payment_date_time': 'datetime',
        'number_of_payments': 'int',
        'previous_payment_amount': 'Amount',
        'previous_payment_date_time': 'datetime',
        'charge_details': 'list[ChargeDetails]',
        'scheduled_payment_type': 'str',
        'scheduled_payment_date_time': 'datetime',
        'frequency': 'FrequencyResponse',
        'currency_of_transfer': 'str',
        'purpose': 'str',
        'priority': 'str',
        'exchange_rate': 'ExchangeRateInformationResponse',
        'refund_account': 'RefundAccount',
        'bulk_amount_sum': 'float'
    }

    attribute_map = {
        'id': 'id',
        'institution_consent_id': 'institutionConsentId',
        'payment_idempotency_id': 'paymentIdempotencyId',
        'payment_lifecycle_id': 'paymentLifecycleId',
        'status': 'status',
        'status_details': 'statusDetails',
        'payer': 'payer',
        'payee_details': 'payeeDetails',
        'reference': 'reference',
        'amount': 'amount',
        'currency': 'currency',
        'amount_details': 'amountDetails',
        'created_at': 'createdAt',
        'first_payment_amount': 'firstPaymentAmount',
        'first_payment_date_time': 'firstPaymentDateTime',
        'next_payment_amount': 'nextPaymentAmount',
        'next_payment_date_time': 'nextPaymentDateTime',
        'final_payment_amount': 'finalPaymentAmount',
        'final_payment_date_time': 'finalPaymentDateTime',
        'number_of_payments': 'numberOfPayments',
        'previous_payment_amount': 'previousPaymentAmount',
        'previous_payment_date_time': 'previousPaymentDateTime',
        'charge_details': 'chargeDetails',
        'scheduled_payment_type': 'scheduledPaymentType',
        'scheduled_payment_date_time': 'scheduledPaymentDateTime',
        'frequency': 'frequency',
        'currency_of_transfer': 'currencyOfTransfer',
        'purpose': 'purpose',
        'priority': 'priority',
        'exchange_rate': 'exchangeRate',
        'refund_account': 'refundAccount',
        'bulk_amount_sum': 'bulkAmountSum'
    }

    def __init__(self, id=None, institution_consent_id=None, payment_idempotency_id=None, payment_lifecycle_id=None, status=None, status_details=None, payer=None, payee_details=None, reference=None, amount=None, currency=None, amount_details=None, created_at=None, first_payment_amount=None, first_payment_date_time=None, next_payment_amount=None, next_payment_date_time=None, final_payment_amount=None, final_payment_date_time=None, number_of_payments=None, previous_payment_amount=None, previous_payment_date_time=None, charge_details=None, scheduled_payment_type=None, scheduled_payment_date_time=None, frequency=None, currency_of_transfer=None, purpose=None, priority=None, exchange_rate=None, refund_account=None, bulk_amount_sum=None, local_vars_configuration=None):  # noqa: E501
        """PaymentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._institution_consent_id = None
        self._payment_idempotency_id = None
        self._payment_lifecycle_id = None
        self._status = None
        self._status_details = None
        self._payer = None
        self._payee_details = None
        self._reference = None
        self._amount = None
        self._currency = None
        self._amount_details = None
        self._created_at = None
        self._first_payment_amount = None
        self._first_payment_date_time = None
        self._next_payment_amount = None
        self._next_payment_date_time = None
        self._final_payment_amount = None
        self._final_payment_date_time = None
        self._number_of_payments = None
        self._previous_payment_amount = None
        self._previous_payment_date_time = None
        self._charge_details = None
        self._scheduled_payment_type = None
        self._scheduled_payment_date_time = None
        self._frequency = None
        self._currency_of_transfer = None
        self._purpose = None
        self._priority = None
        self._exchange_rate = None
        self._refund_account = None
        self._bulk_amount_sum = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if institution_consent_id is not None:
            self.institution_consent_id = institution_consent_id
        if payment_idempotency_id is not None:
            self.payment_idempotency_id = payment_idempotency_id
        if payment_lifecycle_id is not None:
            self.payment_lifecycle_id = payment_lifecycle_id
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if payer is not None:
            self.payer = payer
        if payee_details is not None:
            self.payee_details = payee_details
        if reference is not None:
            self.reference = reference
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if amount_details is not None:
            self.amount_details = amount_details
        if created_at is not None:
            self.created_at = created_at
        if first_payment_amount is not None:
            self.first_payment_amount = first_payment_amount
        if first_payment_date_time is not None:
            self.first_payment_date_time = first_payment_date_time
        if next_payment_amount is not None:
            self.next_payment_amount = next_payment_amount
        if next_payment_date_time is not None:
            self.next_payment_date_time = next_payment_date_time
        if final_payment_amount is not None:
            self.final_payment_amount = final_payment_amount
        if final_payment_date_time is not None:
            self.final_payment_date_time = final_payment_date_time
        if number_of_payments is not None:
            self.number_of_payments = number_of_payments
        if previous_payment_amount is not None:
            self.previous_payment_amount = previous_payment_amount
        if previous_payment_date_time is not None:
            self.previous_payment_date_time = previous_payment_date_time
        if charge_details is not None:
            self.charge_details = charge_details
        if scheduled_payment_type is not None:
            self.scheduled_payment_type = scheduled_payment_type
        if scheduled_payment_date_time is not None:
            self.scheduled_payment_date_time = scheduled_payment_date_time
        if frequency is not None:
            self.frequency = frequency
        if currency_of_transfer is not None:
            self.currency_of_transfer = currency_of_transfer
        if purpose is not None:
            self.purpose = purpose
        if priority is not None:
            self.priority = priority
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if refund_account is not None:
            self.refund_account = refund_account
        if bulk_amount_sum is not None:
            self.bulk_amount_sum = bulk_amount_sum

    @property
    def id(self):
        """Gets the id of this PaymentResponse.  # noqa: E501


        :return: The id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponse.


        :param id: The id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def institution_consent_id(self):
        """Gets the institution_consent_id of this PaymentResponse.  # noqa: E501


        :return: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_consent_id

    @institution_consent_id.setter
    def institution_consent_id(self, institution_consent_id):
        """Sets the institution_consent_id of this PaymentResponse.


        :param institution_consent_id: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._institution_consent_id = institution_consent_id

    @property
    def payment_idempotency_id(self):
        """Gets the payment_idempotency_id of this PaymentResponse.  # noqa: E501


        :return: The payment_idempotency_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_idempotency_id

    @payment_idempotency_id.setter
    def payment_idempotency_id(self, payment_idempotency_id):
        """Sets the payment_idempotency_id of this PaymentResponse.


        :param payment_idempotency_id: The payment_idempotency_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_idempotency_id = payment_idempotency_id

    @property
    def payment_lifecycle_id(self):
        """Gets the payment_lifecycle_id of this PaymentResponse.  # noqa: E501


        :return: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_lifecycle_id

    @payment_lifecycle_id.setter
    def payment_lifecycle_id(self, payment_lifecycle_id):
        """Sets the payment_lifecycle_id of this PaymentResponse.


        :param payment_lifecycle_id: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_lifecycle_id = payment_lifecycle_id

    @property
    def status(self):
        """Gets the status of this PaymentResponse.  # noqa: E501


        :return: The status of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponse.


        :param status: The status of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "COMPLETED_SETTLEMENT_IN_PROCESS", "EXPIRED", "UNKNOWN", "ACTIVE", "INACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this PaymentResponse.  # noqa: E501


        :return: The status_details of this PaymentResponse.  # noqa: E501
        :rtype: PaymentStatusDetails
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this PaymentResponse.


        :param status_details: The status_details of this PaymentResponse.  # noqa: E501
        :type: PaymentStatusDetails
        """

        self._status_details = status_details

    @property
    def payer(self):
        """Gets the payer of this PaymentResponse.  # noqa: E501


        :return: The payer of this PaymentResponse.  # noqa: E501
        :rtype: Payer
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """Sets the payer of this PaymentResponse.


        :param payer: The payer of this PaymentResponse.  # noqa: E501
        :type: Payer
        """

        self._payer = payer

    @property
    def payee_details(self):
        """Gets the payee_details of this PaymentResponse.  # noqa: E501


        :return: The payee_details of this PaymentResponse.  # noqa: E501
        :rtype: Payee
        """
        return self._payee_details

    @payee_details.setter
    def payee_details(self, payee_details):
        """Sets the payee_details of this PaymentResponse.


        :param payee_details: The payee_details of this PaymentResponse.  # noqa: E501
        :type: Payee
        """

        self._payee_details = payee_details

    @property
    def reference(self):
        """Gets the reference of this PaymentResponse.  # noqa: E501


        :return: The reference of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentResponse.


        :param reference: The reference of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def amount(self):
        """Gets the amount of this PaymentResponse.  # noqa: E501


        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.


        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentResponse.  # noqa: E501


        :return: The currency of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentResponse.


        :param currency: The currency of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount_details(self):
        """Gets the amount_details of this PaymentResponse.  # noqa: E501


        :return: The amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """Sets the amount_details of this PaymentResponse.


        :param amount_details: The amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._amount_details = amount_details

    @property
    def created_at(self):
        """Gets the created_at of this PaymentResponse.  # noqa: E501


        :return: The created_at of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentResponse.


        :param created_at: The created_at of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def first_payment_amount(self):
        """Gets the first_payment_amount of this PaymentResponse.  # noqa: E501


        :return: The first_payment_amount of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._first_payment_amount

    @first_payment_amount.setter
    def first_payment_amount(self, first_payment_amount):
        """Sets the first_payment_amount of this PaymentResponse.


        :param first_payment_amount: The first_payment_amount of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._first_payment_amount = first_payment_amount

    @property
    def first_payment_date_time(self):
        """Gets the first_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The first_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._first_payment_date_time

    @first_payment_date_time.setter
    def first_payment_date_time(self, first_payment_date_time):
        """Sets the first_payment_date_time of this PaymentResponse.


        :param first_payment_date_time: The first_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._first_payment_date_time = first_payment_date_time

    @property
    def next_payment_amount(self):
        """Gets the next_payment_amount of this PaymentResponse.  # noqa: E501


        :return: The next_payment_amount of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._next_payment_amount

    @next_payment_amount.setter
    def next_payment_amount(self, next_payment_amount):
        """Sets the next_payment_amount of this PaymentResponse.


        :param next_payment_amount: The next_payment_amount of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._next_payment_amount = next_payment_amount

    @property
    def next_payment_date_time(self):
        """Gets the next_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The next_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._next_payment_date_time

    @next_payment_date_time.setter
    def next_payment_date_time(self, next_payment_date_time):
        """Sets the next_payment_date_time of this PaymentResponse.


        :param next_payment_date_time: The next_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._next_payment_date_time = next_payment_date_time

    @property
    def final_payment_amount(self):
        """Gets the final_payment_amount of this PaymentResponse.  # noqa: E501


        :return: The final_payment_amount of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._final_payment_amount

    @final_payment_amount.setter
    def final_payment_amount(self, final_payment_amount):
        """Sets the final_payment_amount of this PaymentResponse.


        :param final_payment_amount: The final_payment_amount of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._final_payment_amount = final_payment_amount

    @property
    def final_payment_date_time(self):
        """Gets the final_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The final_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._final_payment_date_time

    @final_payment_date_time.setter
    def final_payment_date_time(self, final_payment_date_time):
        """Sets the final_payment_date_time of this PaymentResponse.


        :param final_payment_date_time: The final_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._final_payment_date_time = final_payment_date_time

    @property
    def number_of_payments(self):
        """Gets the number_of_payments of this PaymentResponse.  # noqa: E501


        :return: The number_of_payments of this PaymentResponse.  # noqa: E501
        :rtype: int
        """
        return self._number_of_payments

    @number_of_payments.setter
    def number_of_payments(self, number_of_payments):
        """Sets the number_of_payments of this PaymentResponse.


        :param number_of_payments: The number_of_payments of this PaymentResponse.  # noqa: E501
        :type: int
        """

        self._number_of_payments = number_of_payments

    @property
    def previous_payment_amount(self):
        """Gets the previous_payment_amount of this PaymentResponse.  # noqa: E501


        :return: The previous_payment_amount of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._previous_payment_amount

    @previous_payment_amount.setter
    def previous_payment_amount(self, previous_payment_amount):
        """Sets the previous_payment_amount of this PaymentResponse.


        :param previous_payment_amount: The previous_payment_amount of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._previous_payment_amount = previous_payment_amount

    @property
    def previous_payment_date_time(self):
        """Gets the previous_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The previous_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._previous_payment_date_time

    @previous_payment_date_time.setter
    def previous_payment_date_time(self, previous_payment_date_time):
        """Sets the previous_payment_date_time of this PaymentResponse.


        :param previous_payment_date_time: The previous_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._previous_payment_date_time = previous_payment_date_time

    @property
    def charge_details(self):
        """Gets the charge_details of this PaymentResponse.  # noqa: E501


        :return: The charge_details of this PaymentResponse.  # noqa: E501
        :rtype: list[ChargeDetails]
        """
        return self._charge_details

    @charge_details.setter
    def charge_details(self, charge_details):
        """Sets the charge_details of this PaymentResponse.


        :param charge_details: The charge_details of this PaymentResponse.  # noqa: E501
        :type: list[ChargeDetails]
        """

        self._charge_details = charge_details

    @property
    def scheduled_payment_type(self):
        """Gets the scheduled_payment_type of this PaymentResponse.  # noqa: E501


        :return: The scheduled_payment_type of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_payment_type

    @scheduled_payment_type.setter
    def scheduled_payment_type(self, scheduled_payment_type):
        """Sets the scheduled_payment_type of this PaymentResponse.


        :param scheduled_payment_type: The scheduled_payment_type of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._scheduled_payment_type = scheduled_payment_type

    @property
    def scheduled_payment_date_time(self):
        """Gets the scheduled_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The scheduled_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_payment_date_time

    @scheduled_payment_date_time.setter
    def scheduled_payment_date_time(self, scheduled_payment_date_time):
        """Sets the scheduled_payment_date_time of this PaymentResponse.


        :param scheduled_payment_date_time: The scheduled_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._scheduled_payment_date_time = scheduled_payment_date_time

    @property
    def frequency(self):
        """Gets the frequency of this PaymentResponse.  # noqa: E501


        :return: The frequency of this PaymentResponse.  # noqa: E501
        :rtype: FrequencyResponse
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PaymentResponse.


        :param frequency: The frequency of this PaymentResponse.  # noqa: E501
        :type: FrequencyResponse
        """

        self._frequency = frequency

    @property
    def currency_of_transfer(self):
        """Gets the currency_of_transfer of this PaymentResponse.  # noqa: E501


        :return: The currency_of_transfer of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_of_transfer

    @currency_of_transfer.setter
    def currency_of_transfer(self, currency_of_transfer):
        """Sets the currency_of_transfer of this PaymentResponse.


        :param currency_of_transfer: The currency_of_transfer of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._currency_of_transfer = currency_of_transfer

    @property
    def purpose(self):
        """Gets the purpose of this PaymentResponse.  # noqa: E501


        :return: The purpose of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this PaymentResponse.


        :param purpose: The purpose of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def priority(self):
        """Gets the priority of this PaymentResponse.  # noqa: E501


        :return: The priority of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PaymentResponse.


        :param priority: The priority of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "URGENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and priority not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PaymentResponse.  # noqa: E501


        :return: The exchange_rate of this PaymentResponse.  # noqa: E501
        :rtype: ExchangeRateInformationResponse
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PaymentResponse.


        :param exchange_rate: The exchange_rate of this PaymentResponse.  # noqa: E501
        :type: ExchangeRateInformationResponse
        """

        self._exchange_rate = exchange_rate

    @property
    def refund_account(self):
        """Gets the refund_account of this PaymentResponse.  # noqa: E501


        :return: The refund_account of this PaymentResponse.  # noqa: E501
        :rtype: RefundAccount
        """
        return self._refund_account

    @refund_account.setter
    def refund_account(self, refund_account):
        """Sets the refund_account of this PaymentResponse.


        :param refund_account: The refund_account of this PaymentResponse.  # noqa: E501
        :type: RefundAccount
        """

        self._refund_account = refund_account

    @property
    def bulk_amount_sum(self):
        """Gets the bulk_amount_sum of this PaymentResponse.  # noqa: E501

        Control sum for bulk payments  # noqa: E501

        :return: The bulk_amount_sum of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._bulk_amount_sum

    @bulk_amount_sum.setter
    def bulk_amount_sum(self, bulk_amount_sum):
        """Sets the bulk_amount_sum of this PaymentResponse.

        Control sum for bulk payments  # noqa: E501

        :param bulk_amount_sum: The bulk_amount_sum of this PaymentResponse.  # noqa: E501
        :type: float
        """

        self._bulk_amount_sum = bulk_amount_sum

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PaymentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentResponse):
            return True

        return self.to_dict() != other.to_dict()
