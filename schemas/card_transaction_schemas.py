"""Card Transaction schemas.

These schemas are reported by Card acquirers and Card Issuers.

Card acquiers use these schemas to report the below items, Section 3 in the regulations.
Item 3. Card based payment transactions,
item 5. Cash advance at point of sale (POS) terminals.

Card issuers use these schemas to report below items, Section 3 in the regulations.
item 3. Card based payment transactions,
item 4. ATM cash withdrawal,
item 5. Cash advance at point of sale (POS) terminals.

Card transaction schemas uses the BaseTransaction as an input,
defined in transaction_schemas.py.
BaseTransaction consist of all attributes that are relevant for all the items in the regulation that are reported transactions by transaction.
"""

from decimal import Decimal

from pydantic import (
    Field,
    PastDate,
    PastDatetime,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_core import InitErrorDetails
from typing_extensions import Self

from payment_statistics_utils.codelists.codelists import country
from payment_statistics_utils.enums.field_metadata_enums import (
    AccountCurrencyMeta,
    AccountValueMeta,
    CardTypeMeta,
    ContactlessMeta,
    CounterPartyCountryCardAcquirersMeta,
    CounterPartyCountryCardMeta,
    InitiationChannelMeta,
    MerchantCategoryMeta,
    MerchantLocationMeta,
    PaymentSchemeMeta,
    PaymentServiceUserMeta,
    PaymentTypeTransactionsMeta,
    RemoteInitiationMeta,
    TransactionClearedMeta,
    TransactionInitiatedMeta,
    TransactionTypeMeta,
)
from payment_statistics_utils.enums.full_enums import (
    Contactless,
    RemoteInitiation,
    TransactionType,
)
from payment_statistics_utils.enums.transaction_enums import (
    CardTypeCardPaymentAcquirer,
    CardTypeCardPaymentIssuer,
    InitiationChannelCardPaymentAquierer,
    InitiationChannelCardPaymentIssuer,
    PaymentSchemeCardPaymentAcquirer,
    PaymentSchemeCardPaymentIssuer,
    PaymentServiceUserCardPaymentIssuer,
    PaymentTypeCardPaymentAcquirer,
    PaymentTypeCardPaymentIssuer,
)
from payment_statistics_utils.schemas.transaction_schemas import BaseTransaction
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_country,
    validate_currency,
    validate_date,
    validate_merchant_category_code,
    validate_timestamp,
)
from payment_statistics_utils.utils.model_validation_functions import (
    model_validation_error,
    valdate_transaction_cleared_between_dates,
    validate_payment_type_and_reported_payment_type,
)
from payment_statistics_utils.utils.types import (
    Country,
    Currency,
    MerchantCategory,
)


class BaseCardPayment(BaseTransaction, extra="forbid"):
    """Base card payment.

    Class Base card payment consist of all attributes that are relevant for both card acquirers and card issuers,
    in addition to the base transaction attributes.
    """

    transaction_initiated: PastDatetime | None = Field(
        None,
        description=TransactionInitiatedMeta.description.value,
        examples=TransactionInitiatedMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionInitiatedMeta"},
    )

    transaction_cleared: PastDate = Field(
        ...,
        description=TransactionClearedMeta.description.value,
        examples=TransactionClearedMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionClearedMeta"},
    )

    merchant_location: Country = Field(
        ...,
        description=MerchantLocationMeta.description.value,
        examples=MerchantLocationMeta.examples.value,
        json_schema_extra={"meta_class": "MerchantLocationMeta"},
    )

    remote_initiation: RemoteInitiation = Field(
        ...,
        description=RemoteInitiationMeta.description.value,
        examples=RemoteInitiationMeta.examples.value,
        json_schema_extra={"meta_class": "RemoteInitiationMeta"},
    )

    contactless: Contactless | None = Field(
        None,
        description=ContactlessMeta.description.value,
        examples=ContactlessMeta.examples.value,
        json_schema_extra={"meta_class": "ContactlessMeta"},
    )

    merchant_category: MerchantCategory = Field(
        ...,
        pattern=r"^(?:\d{4}|G\d{3})$",
        description=MerchantCategoryMeta.description.value,
        examples=MerchantCategoryMeta.examples.value,
        json_schema_extra={"meta_class": "MerchantCategoryMeta"},
    )

    @field_validator("merchant_location", mode="after")
    @classmethod
    def validate_merchant_location(cls, merchant_location: str) -> str:
        """Validate that merchant_location is alpha_2."""
        return validate_country(merchant_location)

    @field_validator("merchant_category", mode="after")
    @classmethod
    def validate_merchant_category(cls, merchant_category: str) -> str:
        """Validate that merchant_category is valid."""
        return validate_merchant_category_code(merchant_category)

    @field_validator("transaction_initiated", mode="before")
    @classmethod
    def validate_timestamp_transaction_initiated(cls, v: str | None) -> str | None:
        """Validate timestamp."""
        return validate_timestamp(v)

    @field_validator("transaction_cleared", mode="before")
    @classmethod
    def validate_timestamp_transaction_cleared(cls, v: str) -> str:
        """Validate timestamp."""
        return validate_date(v)


class CardPaymentIssuer(BaseCardPayment, extra="forbid"):
    """Card payment issuer.

    Class Card payment issuer consists of all additional attributes,
    in addition to the base transaction and base card payment attributes,
    that should be reported from the card issuers perspectiv when reporting items 3, 4 and 5.
    """

    payment_type: PaymentTypeCardPaymentIssuer = Field(
        ...,
        description=PaymentTypeTransactionsMeta.description.value,
        examples=PaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeTransactionsMeta"},
    )

    transaction_type: TransactionType | None = Field(
        None,
        description=TransactionTypeMeta.description.value,
        examples=TransactionTypeMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionTypeMeta"},
    )

    counterparty_country: Country | None = Field(
        None,
        description=CounterPartyCountryCardMeta.description.value,
        examples=CounterPartyCountryCardMeta.examples.value,
        json_schema_extra={"meta_class": "CounterPartyCountryCardMeta"},
    )

    account_value: Decimal = Field(
        ge=0.00,
        decimal_places=2,
        description=AccountValueMeta.description.value,
        examples=AccountValueMeta.examples.value,
        json_schema_extra={"meta_class": "AccountValueMeta"},
    )

    account_currency: Currency = Field(
        ...,
        description=AccountCurrencyMeta.description.value,
        examples=AccountCurrencyMeta.examples.value,
        json_schema_extra={"meta_class": "AccountCurrencyMeta"},
    )

    payment_service_user: PaymentServiceUserCardPaymentIssuer = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    initiation_channel: InitiationChannelCardPaymentIssuer = Field(
        ...,
        description=InitiationChannelMeta.description.value,
        examples=InitiationChannelMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelMeta"},
    )

    payment_scheme: PaymentSchemeCardPaymentIssuer = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    card_type: CardTypeCardPaymentIssuer = Field(
        ...,
        description=CardTypeMeta.description.value,
        examples=CardTypeMeta.examples.value,
        json_schema_extra={"meta_class": "CardTypeMeta"},
    )

    @field_validator("account_currency", mode="after")
    @classmethod
    def validate_account_currency(cls, account_currency: str) -> str:
        """Validate that account_currency is alpha_3."""
        return validate_currency(account_currency)

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is None or alpha_2."""
        if not counterparty_country or counterparty_country.upper() in country.keys():
            return counterparty_country.upper()
        else:
            raise ValueError(
                f"Country code is incorrect. Got {counterparty_country}, expected ISO 3166-1 alpha-2 country code or None."
            )

    @model_validator(mode="after")
    def validate_model(self) -> Self:  # noqa: C901
        """Validates model."""
        errors: list[InitErrorDetails] = []

        if self.initiation_channel in (2221, 2222) and self.remote_initiation == "R":
            errors.append(
                model_validation_error(
                    ("remote_initiation",),
                    self.remote_initiation,
                    "ATM and POS-terminal initiated payments can not be done remotely.",
                )
            )

        if (
            self.initiation_channel in (2211, 2212, 2230)
            and self.remote_initiation == "NR"
        ):
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    f"Transaction with initiation channel {self.initiation_channel} have to be initiated remotely.",
                )
            )

        if self.initiation_channel == 1000 and self.contactless != "OTH":
            errors.append(
                model_validation_error(
                    ("contactless",),
                    self.contactless,
                    "Non-electronic initiated payments should be reported with attribute contactless as 'OTH'.",
                )
            )

        if self.remote_initiation == "R" and self.contactless:
            errors.append(
                model_validation_error(
                    ("contactless",),
                    self.contactless,
                    "Field contactless should not be reported when the payment is initiated remotely.",
                )
            )

        if self.payment_type == "CPI" and self.transaction_type is None:
            errors.append(
                model_validation_error(
                    ("transaction_type",),
                    self.transaction_type,
                    "Card payments have to be reported with a transaction type.",
                )
            )

        if self.payment_scheme == "PCS_MCRD" and self.transaction_initiated is None:
            errors.append(
                model_validation_error(
                    ("transaction_initiated",),
                    self.transaction_initiated,
                    "Field transaction_initiated can't be missing when payment scheme is Mastercard.",
                )
            )

        if (
            self.transaction_initiated
            and self.transaction_cleared
            and self.transaction_initiated.date() > self.transaction_cleared
        ):
            errors.append(
                model_validation_error(
                    ("transaction_initiated", "transaction_cleared"),
                    f"{self.transaction_initiated}, {self.transaction_cleared}",
                    "Field transaction_cleared must be the same or after transaction_initiated.",
                )
            )

        if self.reported_payment_type:
            if result := validate_payment_type_and_reported_payment_type(
                self.payment_type, self.reported_payment_type
            ):
                errors.append(result)

        if self.date_from and self.date_to:
            if result := valdate_transaction_cleared_between_dates(
                self.transaction_cleared, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self


class CardPaymentAcquirer(BaseCardPayment, extra="forbid"):
    """Card payment acquirer.

    Class Card payment acquirer consists of all additional attributes,
    in addition to the base transaction and base card payment attributes,
    that should be reported from the card acquirers perspectiv when reporting items 3 and 5.
    """

    payment_type: PaymentTypeCardPaymentAcquirer = Field(
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

    transaction_type: TransactionType | None = Field(
        None,
        description=TransactionTypeMeta.description.value,
        examples=TransactionTypeMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionTypeMeta"},
    )

    initiation_channel: InitiationChannelCardPaymentAquierer = Field(
        ...,
        description=InitiationChannelMeta.description.value,
        examples=InitiationChannelMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelMeta"},
    )

    payment_scheme: PaymentSchemeCardPaymentAcquirer = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    card_type: CardTypeCardPaymentAcquirer = Field(
        ...,
        description=CardTypeMeta.description.value,
        examples=CardTypeMeta.examples.value,
        json_schema_extra={"meta_class": "CardTypeMeta"},
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)

    @model_validator(mode="after")
    def validate_model(self) -> Self:  # noqa: C901
        """Validates model."""
        errors: list[InitErrorDetails] = []

        if self.initiation_channel == 2222 and self.remote_initiation == "R":
            errors.append(
                model_validation_error(
                    ("remote_initiation",),
                    self.remote_initiation,
                    "POS-terminal initiated payments can not be done remotely.",
                )
            )

        if (
            self.initiation_channel in (2211, 2212, 2230)
            and self.remote_initiation == "NR"
        ):
            errors.append(
                model_validation_error(
                    ("initiation_channel", "remote_initiation"),
                    f"{self.initiation_channel}, {self.remote_initiation}",
                    f"Transaction with initiation channel {self.initiation_channel} have to be initiated remotely.",
                )
            )

        if self.initiation_channel == 1000 and self.contactless != "OTH":
            errors.append(
                model_validation_error(
                    ("contactless",),
                    self.contactless,
                    "Non-electronic initiated payments should be reported with attribute contactless as 'OTH'.",
                )
            )

        if self.remote_initiation == "R" and self.contactless:
            errors.append(
                model_validation_error(
                    ("contactless",),
                    self.contactless,
                    "Field contactless should not be reported when the payment is initiated remotely.",
                )
            )

        if self.payment_type == "CPA" and self.transaction_type is None:
            errors.append(
                model_validation_error(
                    ("transaction_type",),
                    self.transaction_type,
                    "Card payments have to be reported with a transaction type.",
                )
            )

        if self.payment_scheme == "PCS_MCRD" and self.transaction_initiated is None:
            errors.append(
                model_validation_error(
                    ("transaction_initiated",),
                    self.transaction_initiated,
                    "Field transaction_initiated can't be missing when payment scheme is Mastercard.",
                )
            )

        if (
            self.transaction_initiated
            and self.transaction_cleared
            and self.transaction_initiated.date() > self.transaction_cleared
        ):
            errors.append(
                model_validation_error(
                    ("transaction_initiated", "transaction_cleared"),
                    f"{self.transaction_initiated}, {self.transaction_cleared}",
                    "Field transaction_cleared must be the same or after transaction_initiated.",
                )
            )

        if self.reported_payment_type:
            if result := validate_payment_type_and_reported_payment_type(
                self.payment_type, self.reported_payment_type
            ):
                errors.append(result)

        if self.date_from and self.date_to:
            if result := valdate_transaction_cleared_between_dates(
                self.transaction_cleared, self.date_from, self.date_to
            ):
                errors.append(result)

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)

        return self
