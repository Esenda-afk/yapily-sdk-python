"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from yapily.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from yapily.exceptions import ApiAttributeError


def lazy_import():
    from yapily.model.address_details import AddressDetails
    from yapily.model.amount import Amount
    from yapily.model.currency_exchange import CurrencyExchange
    from yapily.model.enrichment import Enrichment
    from yapily.model.iso_bank_transaction_code import IsoBankTransactionCode
    from yapily.model.merchant import Merchant
    from yapily.model.payee import Payee
    from yapily.model.payer import Payer
    from yapily.model.proprietary_bank_transaction_code import ProprietaryBankTransactionCode
    from yapily.model.statement_reference import StatementReference
    from yapily.model.transaction_balance import TransactionBalance
    from yapily.model.transaction_charge_details import TransactionChargeDetails
    from yapily.model.transaction_status_enum import TransactionStatusEnum
    globals()['AddressDetails'] = AddressDetails
    globals()['Amount'] = Amount
    globals()['CurrencyExchange'] = CurrencyExchange
    globals()['Enrichment'] = Enrichment
    globals()['IsoBankTransactionCode'] = IsoBankTransactionCode
    globals()['Merchant'] = Merchant
    globals()['Payee'] = Payee
    globals()['Payer'] = Payer
    globals()['ProprietaryBankTransactionCode'] = ProprietaryBankTransactionCode
    globals()['StatementReference'] = StatementReference
    globals()['TransactionBalance'] = TransactionBalance
    globals()['TransactionChargeDetails'] = TransactionChargeDetails
    globals()['TransactionStatusEnum'] = TransactionStatusEnum


class Transaction(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'date': (datetime,),  # noqa: E501
            'booking_date_time': (datetime,),  # noqa: E501
            'value_date_time': (datetime,),  # noqa: E501
            'status': (TransactionStatusEnum,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'transaction_amount': (Amount,),  # noqa: E501
            'gross_amount': (Amount,),  # noqa: E501
            'currency_exchange': (CurrencyExchange,),  # noqa: E501
            'charge_details': (TransactionChargeDetails,),  # noqa: E501
            'reference': (str,),  # noqa: E501
            'statement_references': ([StatementReference],),  # noqa: E501
            'description': (str,),  # noqa: E501
            'transaction_information': ([str],),  # noqa: E501
            'address_details': (AddressDetails,),  # noqa: E501
            'iso_bank_transaction_code': (IsoBankTransactionCode,),  # noqa: E501
            'proprietary_bank_transaction_code': (ProprietaryBankTransactionCode,),  # noqa: E501
            'balance': (TransactionBalance,),  # noqa: E501
            'payee_details': (Payee,),  # noqa: E501
            'payer_details': (Payer,),  # noqa: E501
            'merchant': (Merchant,),  # noqa: E501
            'enrichment': (Enrichment,),  # noqa: E501
            'supplementary_data': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'date': 'date',  # noqa: E501
        'booking_date_time': 'bookingDateTime',  # noqa: E501
        'value_date_time': 'valueDateTime',  # noqa: E501
        'status': 'status',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'transaction_amount': 'transactionAmount',  # noqa: E501
        'gross_amount': 'grossAmount',  # noqa: E501
        'currency_exchange': 'currencyExchange',  # noqa: E501
        'charge_details': 'chargeDetails',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'statement_references': 'statementReferences',  # noqa: E501
        'description': 'description',  # noqa: E501
        'transaction_information': 'transactionInformation',  # noqa: E501
        'address_details': 'addressDetails',  # noqa: E501
        'iso_bank_transaction_code': 'isoBankTransactionCode',  # noqa: E501
        'proprietary_bank_transaction_code': 'proprietaryBankTransactionCode',  # noqa: E501
        'balance': 'balance',  # noqa: E501
        'payee_details': 'payeeDetails',  # noqa: E501
        'payer_details': 'payerDetails',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'enrichment': 'enrichment',  # noqa: E501
        'supplementary_data': 'supplementaryData',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            date (datetime): [optional]  # noqa: E501
            booking_date_time (datetime): [optional]  # noqa: E501
            value_date_time (datetime): [optional]  # noqa: E501
            status (TransactionStatusEnum): [optional]  # noqa: E501
            amount (float): [optional]  # noqa: E501
            currency (str): [optional]  # noqa: E501
            transaction_amount (Amount): [optional]  # noqa: E501
            gross_amount (Amount): [optional]  # noqa: E501
            currency_exchange (CurrencyExchange): [optional]  # noqa: E501
            charge_details (TransactionChargeDetails): [optional]  # noqa: E501
            reference (str): [optional]  # noqa: E501
            statement_references ([StatementReference]): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            transaction_information ([str]): [optional]  # noqa: E501
            address_details (AddressDetails): [optional]  # noqa: E501
            iso_bank_transaction_code (IsoBankTransactionCode): [optional]  # noqa: E501
            proprietary_bank_transaction_code (ProprietaryBankTransactionCode): [optional]  # noqa: E501
            balance (TransactionBalance): [optional]  # noqa: E501
            payee_details (Payee): [optional]  # noqa: E501
            payer_details (Payer): [optional]  # noqa: E501
            merchant (Merchant): [optional]  # noqa: E501
            enrichment (Enrichment): [optional]  # noqa: E501
            supplementary_data ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            date (datetime): [optional]  # noqa: E501
            booking_date_time (datetime): [optional]  # noqa: E501
            value_date_time (datetime): [optional]  # noqa: E501
            status (TransactionStatusEnum): [optional]  # noqa: E501
            amount (float): [optional]  # noqa: E501
            currency (str): [optional]  # noqa: E501
            transaction_amount (Amount): [optional]  # noqa: E501
            gross_amount (Amount): [optional]  # noqa: E501
            currency_exchange (CurrencyExchange): [optional]  # noqa: E501
            charge_details (TransactionChargeDetails): [optional]  # noqa: E501
            reference (str): [optional]  # noqa: E501
            statement_references ([StatementReference]): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            transaction_information ([str]): [optional]  # noqa: E501
            address_details (AddressDetails): [optional]  # noqa: E501
            iso_bank_transaction_code (IsoBankTransactionCode): [optional]  # noqa: E501
            proprietary_bank_transaction_code (ProprietaryBankTransactionCode): [optional]  # noqa: E501
            balance (TransactionBalance): [optional]  # noqa: E501
            payee_details (Payee): [optional]  # noqa: E501
            payer_details (Payer): [optional]  # noqa: E501
            merchant (Merchant): [optional]  # noqa: E501
            enrichment (Enrichment): [optional]  # noqa: E501
            supplementary_data ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")