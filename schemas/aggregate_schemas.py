"""Aggregate schemas.

This schema is used to report aggregated items, Section 3 in the regulations.
Item 8. Money remittances,
item 9. E-money payment transactions,
item 10. Payment initiation services,
item 11. Over the counter (OTC) cash deposits,
item 12. Over the counter (OTC) cash withdrawals.
"""

from decimal import Decimal
from typing import Self

from pydantic import (
    BaseModel,
    Field,
    PastDate,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_core import InitErrorDetails

from payment_statistics_utils.enums.aggregates_enums import (
    InitiationChannelEMoney,
    PaymentServiceUserEMoney,
    PaymentServiceUserOTC,
    PaymentTypeAggregates,
    PaymentTypeEMoney,
    PaymentTypeMoneyRemittances,
    PaymentTypeOTC,
    PaymentTypePaymentInitiationServices,
)
from payment_statistics_utils.enums.field_metadata_enums import (
    CounterPartyCountryOtherMeta,
    DateFromMeta,
    DateToMeta,
    IdMeta,
    InitiationChannelMeta,
    InitiationCountryMeta,
    NumberOfMeta,
    PaymentServiceUserMeta,
    PaymentTypeAggregateMeta,
    PispInitiatedTransactionMeta,
    RemoteInitiationMeta,
    ReportedPaymentTypeAggregateMeta,
    RoleInTransactionMeta,
    TransactionCurrencyMeta,
    TransactionDayMeta,
    TransactionValueOtherMeta,
)
from payment_statistics_utils.enums.full_enums import (
    PaymentServiceUser,
    PispInitiatedTransaction,
    RemoteInitiation,
    RoleInTransaction,
)
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_country,
    validate_currency,
    validate_date,
)
from payment_statistics_utils.utils.model_validation_functions import (
    valdate_transaction_day_between_dates,
    validate_payment_type_and_reported_payment_type,
)
from payment_statistics_utils.utils.types import Country, Currency


class BaseAggregate(BaseModel, extra="forbid"):
    """Base aggregate.

    Class Base aggregate consist of all attributes that are relevant for all the items that are reported throught the aggregate schemas.
    """

    id: str = Field(
        ...,
        description=IdMeta.description.value,
        examples=IdMeta.examples.value,
        json_schema_extra={"meta_class": "IdMeta"},
    )

    transaction_day: PastDate = Field(
        ...,
        description=TransactionDayMeta.description.value,
        examples=TransactionDayMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionDayMeta"},
    )

    number_of: int = Field(
        ge=1,
        description=NumberOfMeta.description.value,
        examples=NumberOfMeta.examples.value,
        json_schema_extra={"meta_class": "NumberOfMeta"},
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

    reported_payment_type: PaymentTypeAggregates | None = Field(
        default=None,
        exclude=True,
        description=ReportedPaymentTypeAggregateMeta.description.value,
        examples=ReportedPaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentTypeAggregateMeta"},
    )

    date_from: PastDate | None = Field(
        default=None,
        exclude=True,
        description=DateFromMeta.description.value,
        json_schema_extra={"meta_class": "DateFromMeta"},
    )

    date_to: PastDate | None = Field(
        default=None,
        exclude=True,
        description=DateToMeta.description.value,
        json_schema_extra={"meta_class": "DateToMeta"},
    )

    @field_validator("transaction_day", mode="before")
    @classmethod
    def validate_timestamp_transaction_day(cls, v: str) -> str:
        """Validate date format."""
        return validate_date(v)

    @field_validator("transaction_currency", mode="after")
    @classmethod
    def validate_transaction_currency(cls, transaction_currency: str) -> str:
        """Validate that transaction_currency is alpha-3."""
        return validate_currency(transaction_currency)


class EMoney(BaseAggregate, extra="forbid"):
    """E-money transactions.

    Class E-money transactions consists of all additional attributes,
    in addition to the base aggregate attributes,
    that should be reported for E-money transactions (item 9).
    """

    payment_type: PaymentTypeEMoney = Field(
        ...,
        description=PaymentTypeAggregateMeta.description.value,
        examples=PaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeAggregateMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryOtherMeta.description.value,
        examples=CounterPartyCountryOtherMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryOtherMeta"},
    )

    role_in_transaction: RoleInTransaction = Field(
        ...,
        description=RoleInTransactionMeta.description.value,
        examples=RoleInTransactionMeta.examples.value,
        json_schema_extra={"meta_class": "RoleInTransactionMeta"},
    )

    payment_service_user: PaymentServiceUserEMoney = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    initiation_channel: InitiationChannelEMoney = Field(
        ...,
        description=InitiationChannelMeta.description.value,
        examples=InitiationChannelMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelMeta"},
    )

    remote_initiation: RemoteInitiation = Field(
        ...,
        description=RemoteInitiationMeta.description.value,
        examples=RemoteInitiationMeta.examples.value,
        json_schema_extra={"meta_class": "RemoteInitiationMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """Validates model."""
        errors: list[InitErrorDetails] = []

        # Test for payment_type vs reported_payment_type is redundant since credit_transfer is limited to one payment_type.
        # If payment_type != "EMP0" the validation against PaymentTypeEMoney will fail.

        if self.date_from and self.date_to and self.transaction_day:
            if result := valdate_transaction_day_between_dates(
                self.transaction_day, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self


class MoneyRemittances(BaseAggregate, extra="forbid"):
    """Money Remittances.

    Class Money remittances consists of all additional attributes,
    in addition to the base aggregate attributes,
    that should be reported for Money remittances (item 8).
    """

    payment_type: PaymentTypeMoneyRemittances = Field(
        ...,
        description=PaymentTypeAggregateMeta.description.value,
        examples=PaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeAggregateMeta"},
    )

    transaction_day: PastDate = Field(
        ...,
        description=TransactionDayMeta.description.value,
        examples=TransactionDayMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionDayMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryOtherMeta.description.value,
        examples=CounterPartyCountryOtherMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryOtherMeta"},
    )

    initiation_country: Country = Field(
        ...,
        description=InitiationCountryMeta.description.value,
        examples=InitiationCountryMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationCountryMeta"},
    )

    role_in_transaction: RoleInTransaction = Field(
        ...,
        description=RoleInTransactionMeta.description.value,
        examples=RoleInTransactionMeta.examples.value,
        json_schema_extra={"meta_class": "RoleInTransactionMeta"},
    )

    payment_service_user: PaymentServiceUser = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @field_validator("initiation_country", mode="after")
    @classmethod
    def validate_initiation_country(cls, initiation_country: str) -> str:
        """Validate that initiation_country is alpha_2."""
        return validate_country(initiation_country)

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """Validates model."""
        errors: list[InitErrorDetails] = []

        # Test for payment_type vs reported_payment_type is redundant since credit_transfer is limited to one payment_type.
        # If payment_type != "MREM" the validation against PaymentTypeMoneyRemitances will fail.

        if self.date_from and self.date_to and self.transaction_day:
            if result := valdate_transaction_day_between_dates(
                self.transaction_day, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self


class OTC(BaseAggregate, extra="forbid"):
    """Over the counter (OTC) Cash transactions.

    Class Over the counter (OTC) cash transaction consists of all additional attributes,
    in addition to the base aggregate attributes,
    that should be reported for Over the counter (OTC) cash withdrawals and deposits (items 11-12).
    """

    payment_type: PaymentTypeOTC = Field(
        ...,
        description=PaymentTypeAggregateMeta.description.value,
        examples=PaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeAggregateMeta"},
    )

    payment_service_user: PaymentServiceUserOTC = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """Validates model."""
        errors: list[InitErrorDetails] = []

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


class PaymentInitiationServices(BaseAggregate, extra="forbid"):
    """Payment initiation services.

    Class Payment initiation sevices consists of all additional attributes,
    in addition to the base aggregate attributes,
    that should be reported for Payment initiation services (item 10).
    """

    payment_type: PaymentTypePaymentInitiationServices = Field(
        ...,
        description=PaymentTypeAggregateMeta.description.value,
        examples=PaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeAggregateMeta"},
    )

    pisp_initiated_transaction: PispInitiatedTransaction = Field(
        ...,
        description=PispInitiatedTransactionMeta.description.value,
        examples=PispInitiatedTransactionMeta.examples.value,
        json_schema_extra={"meta_class": "PispInitiatedTransactionMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryOtherMeta.description.value,
        examples=CounterPartyCountryOtherMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryOtherMeta"},
    )

    initiation_country: Country = Field(
        ...,
        description=InitiationCountryMeta.description.value,
        examples=InitiationCountryMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationCountryMeta"},
    )

    payment_service_user: PaymentServiceUser = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    remote_initiation: RemoteInitiation = Field(
        ...,
        description=RemoteInitiationMeta.description.value,
        examples=RemoteInitiationMeta.examples.value,
        json_schema_extra={"meta_class": "RemoteInitiationMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @field_validator("initiation_country", mode="after")
    @classmethod
    def validate_initiation_country(cls, initiation_country: str) -> str:
        """Validate that initiation_country is alpha_2."""
        return validate_country(initiation_country)

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """Validates model."""
        errors: list[InitErrorDetails] = []

        # Test for payment_type vs reported_payment_type is redundant since credit_transfer is limited to one payment_type.
        # If payment_type != "PI" the validation against PaymentTypePaymentInitiationServices will fail.

        if self.date_from and self.date_to and self.transaction_day:
            if result := valdate_transaction_day_between_dates(
                self.transaction_day, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self
