"""Transaction schemas.

These schemas are used to report transaction items, Section 3 in the regulations.
Item 1. Instant credit transfers,
item 2. Credit transfers,
item 4. ATM cash withdrawal,
item 6. ATM cash deposit.
"""

from datetime import datetime
from decimal import Decimal

from pydantic import (
    BaseModel,
    Field,
    PastDate,
    PastDatetime,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_core import InitErrorDetails
from typing_extensions import Self

from payment_statistics_utils.enums.field_metadata_enums import (
    AccountCurrencyInstantCreditTransfersMeta,
    AccountValueInstantCreditTransfersMeta,
    CounterPartyCountryCardAcquirersMeta,
    CounterPartyCountryOtherMeta,
    DateFromMeta,
    DateToMeta,
    IdMeta,
    InitiationChannelCreditTransferMeta,
    LocalityMeta,
    MerchantLocationATMtransactionMeta,
    PaymentSchemeMeta,
    PaymentServiceUserMeta,
    PaymentTypeTransactionsMeta,
    RemoteInitiationCreditTransfersMeta,
    ReportedPaymentTypeTransactionsMeta,
    RoleInTransactionMeta,
    SniCodeMeta,
    TransactionCurrencyMeta,
    TransactionDayMeta,
    TransactionTimeMeta,
    TransactionValueOtherMeta,
)
from payment_statistics_utils.enums.full_enums import (
    PaymentServiceUser,
    RemoteInitiation,
    RoleInTransaction,
)
from payment_statistics_utils.enums.transaction_enums import (
    InitiationChannelCreditTransfer,
    InitiationChannelInstantCreditTransfer,
    PaymentSchemeCashTransactionsATMOwners,
    PaymentSchemeCreditTransfer,
    PaymentSchemeInstantCreditTransfer,
    PaymentTypeCashTransactionATMOwners,
    PaymentTypeCreditTransfer,
    PaymentTypeInstantCreditTransfer,
    PaymentTypeTransactions,
)
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_country,
    validate_currency,
    validate_date,
    validate_locality,
    validate_sni_code,
)
from payment_statistics_utils.utils.model_validation_functions import (
    model_validation_error,
    valdate_transaction_day_between_dates,
    valdate_transaction_time_between_dates,
    validate_payment_type_and_reported_payment_type,
)
from payment_statistics_utils.utils.types import (
    Country,
    Currency,
    Locality,
    SniCode,
)


class BaseTransaction(BaseModel, extra="forbid"):
    """Base transaction.

    Class Base transaction consist of all attributes that are relevant for all the items in the regulation that are reported transaction by transaction.
    Note that the class BaseTransaction also is used in the card_transaction_schemas.py.
    """

    id: str = Field(
        ...,
        description=IdMeta.description.value,
        examples=IdMeta.examples.value,
        json_schema_extra={"meta_class": "IdMeta"},
    )

    transaction_value: Decimal = Field(
        ge=0.00,
        decimal_places=2,
        description=TransactionValueOtherMeta.description.value,
        examples=TransactionValueOtherMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionValueOtherMeta"},
    )

    transaction_currency: Currency = Field(
        ...,
        description=TransactionCurrencyMeta.description.value,
        examples=TransactionCurrencyMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionCurrencyMeta"},
    )

    role_in_transaction: RoleInTransaction = Field(
        ...,
        description=RoleInTransactionMeta.description.value,
        examples=RoleInTransactionMeta.examples.value,
        json_schema_extra={"meta_class": "RoleInTransactionMeta"},
    )

    reported_payment_type: PaymentTypeTransactions | None = Field(
        default=None,
        exclude=True,
        description=ReportedPaymentTypeTransactionsMeta.description.value,
        examples=ReportedPaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentTypeTransactionsMeta"},
    )

    date_from: PastDate | None = Field(
        default=None,
        exclude=True,
        description=DateFromMeta.description.value,
        examples=DateFromMeta.examples.value,
        json_schema_extra={"meta_class": "DateFromMeta"},
    )

    date_to: PastDate | None = Field(
        default=None,
        exclude=True,
        description=DateToMeta.description.value,
        examples=DateToMeta.examples.value,
        json_schema_extra={"meta_class": "DateToMeta"},
    )

    @field_validator("transaction_currency", mode="after")
    @classmethod
    def validate_transaction_currency(cls, transaction_currency: str) -> str:
        """Validate that transaction_currency is alpha_3."""
        return validate_currency(transaction_currency)


class CashTransactionsATMOwners(BaseTransaction, extra="forbid"):
    """ATM cash withdrawals and deposits.

    Class Cash transactions ATM owners consists of all additional attributes,
    in addition to the base transaction attributes,
    that should be reported for ATM cash withdrawals and deposits  (item 4 and 6).
    The class Cash transaction ATM owners should be reported of the owners of the ATMs.
    """

    payment_type: PaymentTypeCashTransactionATMOwners = Field(
        ...,
        description=PaymentTypeTransactionsMeta.description.value,
        examples=PaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeTransactionsMeta"},
    )
    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryCardAcquirersMeta.description.value,
        examples=CounterPartyCountryCardAcquirersMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryCardAcquirersMeta"},
    )

    transaction_day: PastDate = Field(
        ...,
        description=TransactionDayMeta.description.value,
        examples=TransactionDayMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionDayMeta"},
    )

    merchant_location: Country = Field(
        ...,
        description=MerchantLocationATMtransactionMeta.description.value,
        examples=MerchantLocationATMtransactionMeta.examples.value,
        json_schema_extra={"meta_class": "MerchantLocationATMtransactionMeta"},
    )

    locality: Locality | None = Field(
        None,
        description=LocalityMeta.description.value,
        examples=LocalityMeta.examples.value,
        json_schema_extra={"meta_class": "LocalityMeta"},
    )

    payment_scheme: PaymentSchemeCashTransactionsATMOwners = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    # Validations that correct codes are used for respective attribute.
    # For attribute that does not have any control, all codes in the code list can be used.
    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @field_validator("merchant_location", mode="after")
    @classmethod
    def validate_merchant_location(cls, merchant_location: str) -> str:
        """Validate that merchant_location is alpha_2."""
        return validate_country(merchant_location)

    @field_validator("locality", mode="after")
    @classmethod
    def validate_locality(cls, locality: str) -> str:
        """Validate locality."""
        return validate_locality(locality)

    @field_validator("transaction_day", mode="before")
    @classmethod
    def validate_timestamp_transaction_day(cls, v: str) -> str:
        """Validate timestamp."""
        return validate_date(v)

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """Validates model."""
        errors: list[InitErrorDetails] = []

        if self.merchant_location == "SE" and not self.locality:
            errors.append(
                model_validation_error(
                    ("merchant_location", "locality"),
                    f"{self.merchant_location}, {self.locality}",
                    "When merchant_location is SE locality have to be reported.",
                )
            )

        if self.merchant_location != "SE" and self.locality:
            errors.append(
                model_validation_error(
                    ("merchant_location", "locality"),
                    f"{self.merchant_location}, {self.locality}",
                    "Locality should not be reported when merchant location is not SE.",
                )
            )

        if self.payment_type == "CW0" and self.role_in_transaction != 1:
            errors.append(
                model_validation_error(
                    ("payment_type", "role_in_transaction"),
                    f"{self.payment_type}, {self.role_in_transaction}",
                    "Cash withdrawals should be reported from the payers PSP.",
                )
            )

        if self.payment_type == "CD0" and self.role_in_transaction != 2:
            errors.append(
                model_validation_error(
                    ("payment_type", "role_in_transaction"),
                    f"{self.payment_type}, {self.role_in_transaction}",
                    "Cash deposits should be reported from the payee's PSP.",
                )
            )

        if self.reported_payment_type:
            if result := validate_payment_type_and_reported_payment_type(
                self.payment_type, self.reported_payment_type
            ):
                errors.append(result)

        if self.date_from and self.date_to and self.transaction_day:
            if result := valdate_transaction_day_between_dates(
                self.transaction_day, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self


class CreditTransfer(BaseTransaction, extra="forbid"):
    """Credit transfer.

    Class credit transfer consists of all additional attributes,
    in addition to the base transaction attributes,
    that should be reported for credit transfer (item 2).
    """

    payment_type: PaymentTypeCreditTransfer = Field(
        ...,
        description=PaymentTypeTransactionsMeta.description.value,
        examples=PaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeTransactionsMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryOtherMeta.description.value,
        examples=CounterPartyCountryOtherMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryOtherMeta"},
    )

    transaction_day: PastDate = Field(
        ...,
        description=TransactionDayMeta.description.value,
        examples=TransactionDayMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionDayMeta"},
    )

    payment_service_user: PaymentServiceUser = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    sni_code: SniCode | None = Field(
        None,
        description=SniCodeMeta.description.value,
        examples=SniCodeMeta.examples.value,
        json_schema_extra={"meta_class": "SniCodeMeta"},
    )

    initiation_channel: InitiationChannelCreditTransfer | None = Field(
        None,
        description=InitiationChannelCreditTransferMeta.description.value,
        examples=InitiationChannelCreditTransferMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelCreditTransferMeta"},
    )

    remote_initiation: RemoteInitiation | None = Field(
        None,
        description=RemoteInitiationCreditTransfersMeta.description.value,
        examples=RemoteInitiationCreditTransfersMeta.examples.value,
        json_schema_extra={"meta_class": "RemoteInitiationCreditTransfersMeta"},
    )

    payment_scheme: PaymentSchemeCreditTransfer = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is None or alpha_2."""
        return validate_country(counterparty_country)

    @field_validator("sni_code", mode="after")
    @classmethod
    def validate_sni_code(cls, sni_code: str) -> str:
        """Validate sni code."""
        return validate_sni_code(sni_code)

    @field_validator("transaction_day", mode="before")
    @classmethod
    def validate_timestamp_transaction_day(cls, v: str) -> str:
        """Validate timestamp."""
        return validate_date(v)

    @model_validator(mode="after")
    def validate_model(self) -> Self:  # noqa: C901
        """Validates model."""
        errors: list[InitErrorDetails] = []

        if self.initiation_channel == 2220 and self.remote_initiation == "R":
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    "Terminal initiated payments can not be done remotely.",
                )
            )

        if (
            self.initiation_channel in (2100, 2210, 2211, 2213, 2231, 2232, 5000)
            and self.remote_initiation == "NR"
        ):
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    f"Transaction with initiation channel {self.initiation_channel} have to be initiated remotely.",
                )
            )

        if self.payment_scheme == "CTS_SEPA" and self.transaction_currency != "EUR":
            errors.append(
                model_validation_error(
                    ("payment_scheme", "transaction_currency"),
                    f"{self.payment_scheme}, {self.transaction_currency}",
                    "Payments via SEPA have to be in transaction currency EUR.",
                )
            )

        if self.initiation_channel is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("initiation_channel", "role_in_transaction"),
                    f"{self.initiation_channel}, {self.role_in_transaction}",
                    "Field required. Initiation_channel can not be missing.",
                )
            )

        if self.initiation_channel and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("initiation_channel", "role_in_transaction"),
                    f"{self.initiation_channel}, {self.role_in_transaction}",
                    "Initiation_channel should not be reported when role_in_transaction is 2, payee's PSP.",
                )
            )

        if self.remote_initiation is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("remote_initiation", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Field required. Remote_initiation can not be missing when role in transaction is '1'.",
                )
            )

        if self.remote_initiation and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("remote_initiation", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Remote_initiation should not be reported when role_in_transaction is '2', payee's PSP.",
                )
            )

        if (
            self.sni_code is None
            and self.role_in_transaction == 2
            and self.payment_service_user == "NMFIXP"
        ):
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction", "payment_service_user"),
                    f"{self.remote_initiation}, {self.role_in_transaction}, {self.payment_service_user}",
                    "Field required. When role_in_transaction is 2, payees PSP, and payment_service_user is a non-MFI excl. private persons, sni code can not be missing.",
                )
            )

        if (
            self.sni_code
            and self.role_in_transaction == 2
            and self.payment_service_user != "NMFIXP"
        ):
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction", "payment_service_user"),
                    f"{self.remote_initiation}, {self.role_in_transaction}, {self.payment_service_user}",
                    "Sni code should only be reported from the payee's PSPs and when the payment_service_user is a non-MFI excl. private persons.",
                )
            )

        if self.sni_code and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Sni code should not be reported from the payer's PSP.",
                )
            )

        # Test for payment_type vs reported_payment_type is redundant since credit_transfer is limited to one payment_type.
        # If payment_type != "CT0" the validation against PaymentTypeCreditTransfer will fail.

        if self.date_from and self.date_to and self.transaction_day:
            if result := valdate_transaction_day_between_dates(
                self.transaction_day, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self


class InstantCreditTransfer(BaseTransaction, extra="forbid"):
    """Instant credit transfer.

    Class Instant credit transfer consists of all additional attributes,
    in addition to the base transaction attributes,
    that should be reported for instant credit transfer (item 1).
    """

    payment_type: PaymentTypeInstantCreditTransfer = Field(
        ...,
        description=PaymentTypeTransactionsMeta.description.value,
        examples=PaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeTransactionsMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryOtherMeta.description.value,
        examples=CounterPartyCountryOtherMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryOtherMeta"},
    )

    transaction_time: PastDatetime = Field(
        ...,
        description=TransactionTimeMeta.description.value,
        examples=TransactionTimeMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionTimeMeta"},
    )

    account_value: float | None = Field(
        None,
        description=AccountValueInstantCreditTransfersMeta.description.value,
        examples=AccountValueInstantCreditTransfersMeta.examples.value,
        json_schema_extra={"meta_class": "AccountValueInstantCreditTransfersMeta"},
    )

    account_currency: Currency | None = Field(
        None,
        description=AccountCurrencyInstantCreditTransfersMeta.description.value,
        examples=AccountCurrencyInstantCreditTransfersMeta.examples.value,
        json_schema_extra={"meta_class": "AccountCurrencyInstantCreditTransfersMeta"},
    )

    payment_service_user: PaymentServiceUser = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    sni_code: SniCode | None = Field(
        None,
        description=SniCodeMeta.description.value,
        examples=SniCodeMeta.examples.value,
        json_schema_extra={"meta_class": "SniCodeMeta"},
    )

    initiation_channel: InitiationChannelInstantCreditTransfer | None = Field(
        None,
        description=InitiationChannelCreditTransferMeta.description.value,
        examples=InitiationChannelCreditTransferMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelCreditTransferMeta"},
    )

    remote_initiation: RemoteInitiation | None = Field(
        None,
        description=RemoteInitiationCreditTransfersMeta.description.value,
        examples=RemoteInitiationCreditTransfersMeta.examples.value,
        json_schema_extra={"meta_class": "RemoteInitiationCreditTransfersMeta"},
    )

    payment_scheme: PaymentSchemeInstantCreditTransfer = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @field_validator("sni_code", mode="after")
    @classmethod
    def validate_sni_code(cls, sni_code: str) -> str:
        """Validate sni code."""
        return validate_sni_code(sni_code)

    @field_validator("account_currency", mode="after")
    @classmethod
    def validate_account_currency(cls, account_currency: str) -> str:
        """Validate that account_currency is alpha_3."""
        return validate_currency(account_currency)

    @field_validator("transaction_time", mode="before")
    @classmethod
    def validate_timestamp_transaction_initiated(cls, v: datetime | str) -> datetime:
        """Validate timestamp."""
        if isinstance(v, datetime):
            return v

        try:
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(  # noqa: B904
                f"Transaction initiated has to be in format '%Y-%m-%d %H:%M:%S' got {type(v)}: {v}"
            )

    @model_validator(mode="after")
    def validate_model(self) -> Self:  # noqa: C901
        """Validates model."""
        errors: list[InitErrorDetails] = []

        if self.initiation_channel == 2220 and self.remote_initiation == "R":
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    "Terminal initiated payments can not be done remotely.",
                )
            )

        if (
            self.initiation_channel in (2100, 2210, 2211, 2213, 2231, 2232, 5000)
            and self.remote_initiation == "NR"
        ):
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    f"Transaction with initiation channel {self.initiation_channel} have to be initiated remotely.",
                )
            )

        if self.payment_scheme == "CTS_SEPAI" and self.transaction_currency != "EUR":
            errors.append(
                model_validation_error(
                    ("payment_scheme", "transaction_currency"),
                    f"{self.payment_scheme}, {self.transaction_currency}",
                    "Payments via SCT Inst have to be in transaction currency EUR.",
                )
            )

        if self.account_currency is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("account_currency", "role_in_transaction"),
                    f"{self.account_currency}, {self.role_in_transaction}",
                    "Field required. Account_currency can not be missing.",
                )
            )

        if self.account_currency and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("account_currency", "role_in_transaction"),
                    f"{self.account_currency}, {self.role_in_transaction}",
                    "Account_currency should not be reported when role_in_transaction is 2, payee's PSP.",
                )
            )

        if self.account_value is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("account_value", "role_in_transaction"),
                    f"{self.account_value}, {self.role_in_transaction}",
                    "Field required. Account_value can not be missing.",
                )
            )

        if self.account_value and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("account_value", "role_in_transaction"),
                    f"{self.account_value}, {self.role_in_transaction}",
                    "Account_value should not be reported when role_in_transaction is 2, payee's PSP.",
                )
            )

        if self.initiation_channel is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("initiation_channel", "role_in_transaction"),
                    f"{self.initiation_channel}, {self.role_in_transaction}",
                    "Field required. Initiation_channel can not be missing.",
                )
            )

        if self.initiation_channel and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("initiation_channel", "role_in_transaction"),
                    f"{self.initiation_channel}, {self.role_in_transaction}",
                    "Initiation_channel should not be reported when role_in_transaction is 2, payee's PSP.",
                )
            )

        if self.remote_initiation is None and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("remote_initiation", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Field required. Remote_initiation can not be missing.",
                )
            )

        if self.remote_initiation and self.role_in_transaction == 2:
            errors.append(
                model_validation_error(
                    ("remote_initiation", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Remote_initiation should not be reported when role_in_transaction is 2, payee's PSP.",
                )
            )

        if (
            self.sni_code is None
            and self.role_in_transaction == 2
            and self.payment_service_user == "NMFIXP"
        ):
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction", "payment_service_user"),
                    f"{self.remote_initiation}, {self.role_in_transaction},{self.payment_service_user}",
                    "Field required. When role_in_transaction is payees PSP and payment_service_user is a non-MFI excl. private persons, sni code can not be missing.",
                )
            )

        if (
            self.sni_code
            and self.role_in_transaction == 2
            and self.payment_service_user != "NMFIXP"
        ):
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction", "payment_service_user"),
                    f"{self.remote_initiation}, {self.role_in_transaction},{self.payment_service_user}",
                    "Sni code should only be reported from the payee's PSPs and when the payment_service_user is a non-MFI excl. private persons.",
                )
            )

        if self.sni_code and self.role_in_transaction == 1:
            errors.append(
                model_validation_error(
                    ("sni_code", "role_in_transaction"),
                    f"{self.remote_initiation}, {self.role_in_transaction}",
                    "Sni code should not be reported from the payer's PSP.",
                )
            )

        # Test for payment_type vs reported_payment_type is redundant since credit_transfer is limited to one payment_type.
        # If payment_type != "CT1" the validation against PaymentTypeInstantCreditTransfer will fail.

        if self.date_from and self.date_to and self.transaction_time:
            if result := valdate_transaction_time_between_dates(
                self.transaction_time, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self
