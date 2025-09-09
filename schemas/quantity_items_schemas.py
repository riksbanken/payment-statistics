"""Quantity items schemas.

These schemas are used to report quantity items, Section 3 in the regulations.
Item 13. Cards,
item 14. Payment accounts,
item 15. POS terminals,
item 16. E-money card terminals,
item 17. ATMs.
"""

from typing import Self

from pydantic import BaseModel, Field, field_validator, model_validator

from payment_statistics_utils.enums.field_metadata_enums import (
    CardFunctionMeta,
    CardTypeMeta,
    ContactlessFunctionMeta,
    EMoneyFunctionMeta,
    IdMeta,
    MerchantLocationQuantityMeta,
    NumberOfQuanityItemsMeta,
    PaymentSchemeMeta,
    PaymentServiceUserMeta,
    QuantityItemsMeta,
    TerminalFunctionMeta,
    TypeOfAccountMeta,
)
from payment_statistics_utils.enums.full_enums import (
    CardFunction,
    ContactlessFunction,
    EmoneyFunction,
    TypeOfAccount,
)
from payment_statistics_utils.enums.quantity_items_enums import (
    CardTypeCard,
    PaymentSchemeCard,
    PaymentServiceUserCard,
    PaymentServiceUserPaymentAccounts,
    QuantityItemsATMs,
    QuantityItemsCard,
    QuantityItemsEMoneyTerminal,
    QuantityItemsPaymentAccounts,
    QuantityItemsPosTerminal,
    TerminalFunctionATMs,
    TerminalFunctionEMoneyTerminals,
    TerminalFunctionPosTerminal,
)
from payment_statistics_utils.utils.field_validaton_functions import validate_country
from payment_statistics_utils.utils.types import Country


class BaseQuantityItems(BaseModel, extra="forbid"):
    """Base quantity items.

    Class Base quantity items consist of all attributes that are relevant for all the quantity items in the regulation.
    """

    id: str = Field(
        ...,
        description=IdMeta.description.value,
        examples=IdMeta.examples.value,
        json_schema_extra={"meta_class": "IdMeta"},
    )

    number_of: int = Field(
        ge=0,
        description=NumberOfQuanityItemsMeta.description.value,
        examples=NumberOfQuanityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "NumberOfQuanityItemsMeta"},
    )


class BaseQuantityItemsMerchantLocation(BaseQuantityItems, extra="forbid"):
    """Base quantity items with merchant location.

    Class Base quantity items with merchant location consist of all attributes that are relevant for item 15 POS terminals,
    item 16 E-money card terminals, and item 17 ATMs,
    in addition to the base quantity items attributes.
    """

    merchant_location: Country = Field(
        ...,
        description=MerchantLocationQuantityMeta.description.value,
        examples=MerchantLocationQuantityMeta.examples.value,
        json_schema_extra={"meta_class": "MerchantLocationQuantityMeta"},
    )

    @field_validator("merchant_location", mode="after")
    @classmethod
    def validate_merchant_loaction(cls, merchant_location: str) -> str:
        """Validate that counterparty_country is None or alpha_2."""
        return validate_country(merchant_location)


class Cards(BaseQuantityItems, extra="forbid"):
    """Cards.

    Class Cards consists of all additional attributes,
    in addition to the base quantity items attributes,
    that should be reported for Cards (item 13).
    """

    quantity_item: QuantityItemsCard = Field(
        ...,
        description=QuantityItemsMeta.description.value,
        examples=QuantityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "QuantityItemsMeta"},
    )

    payment_service_user: PaymentServiceUserCard = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    payment_scheme: PaymentSchemeCard = Field(
        ...,
        description=PaymentSchemeMeta.description.value,
        examples=PaymentSchemeMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSchemeMeta"},
    )

    card_type: CardTypeCard = Field(
        ...,
        description=CardTypeMeta.description.value,
        examples=CardTypeMeta.examples.value,
        json_schema_extra={"meta_class": "CardTypeMeta"},
    )

    card_function: CardFunction = Field(
        ...,
        description=CardFunctionMeta.description.value,
        examples=CardFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "CardFunctionMeta"},
    )

    e_money_function: EmoneyFunction | None = Field(
        None,
        description=EMoneyFunctionMeta.description.value,
        examples=EMoneyFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "EMoneyFunctionMeta"},
    )

    contactless_function: ContactlessFunction = Field(
        ...,
        description=ContactlessFunctionMeta.description.value,
        examples=ContactlessFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "ContactlessFunctionMeta"},
    )

    # Validation that the attribute emoney function is reported if e-money function is reported in attribute card_function.
    # Validation that the attribute emoney function not is reported if e-money function not is reported in attribute card_function.
    @model_validator(mode="after")
    def validate_emoney_function_and_card_function(self) -> Self:
        """E money function and card function validation.

        Attribute e-money function should be reported when the card has e-money functions.
        Attribute e-money function should not be reported when the card hasn't e-money functions.
        """
        if not self.e_money_function and self.card_function in ["CF3", "CF5", "CF6"]:
            raise ValueError(
                "Attribute e-money function has to be reported when the card has e-money functions."
            )

        if self.e_money_function and self.card_function in ["CF1", "CF2", "CF4"]:
            raise ValueError(
                "Attribute e-money function should not to be reported when the card hasn't e-money functions."
            )

        return self


class PosTerminals(BaseQuantityItemsMerchantLocation, extra="forbid"):
    """POS-terminals.

    Class POS-terminals consists of all additional attributes,
    in addition to the Base quantity items and Base quantity items merchant location attributes,
    that should be reported for POS-terminals (item 15).
    """

    quantity_item: QuantityItemsPosTerminal = Field(
        ...,
        description=QuantityItemsMeta.description.value,
        examples=QuantityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "QuantityItemsMeta"},
    )

    terminal_function: TerminalFunctionPosTerminal = Field(
        ...,
        description=TerminalFunctionMeta.description.value,
        examples=TerminalFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "TerminalFunctionMeta"},
    )

    contactless_function: ContactlessFunction = Field(
        ...,
        description=ContactlessFunctionMeta.description.value,
        examples=ContactlessFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "ContactlessFunctionMeta"},
    )


class EMoneyTerminals(BaseQuantityItemsMerchantLocation, extra="forbid"):
    """E-Money terminals.

    Class E-money terminals consists of all additional attributes,
    in addition to the Base quantity items and Base quantity items merchant location attributes,
    that should be reported for E-money terminals (item 16).
    """

    quantity_item: QuantityItemsEMoneyTerminal = Field(
        ...,
        description=QuantityItemsMeta.description.value,
        examples=QuantityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "QuantityItemsMeta"},
    )

    terminal_function: TerminalFunctionEMoneyTerminals = Field(
        ...,
        description=TerminalFunctionMeta.description.value,
        examples=TerminalFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "TerminalFunctionMeta"},
    )


class ATMs(BaseQuantityItemsMerchantLocation, extra="forbid"):
    """ATMs.

    Class ATMs consists of all additional attributes,
    in addition to the Base quantity items and Base quantity items merchant location attributes,
    that should be reported for ATMs (item 17).
    """

    quantity_item: QuantityItemsATMs = Field(
        ...,
        description=QuantityItemsMeta.description.value,
        examples=QuantityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "QuantityItemsMeta"},
    )

    terminal_function: TerminalFunctionATMs = Field(
        ...,
        description=TerminalFunctionMeta.description.value,
        examples=TerminalFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "TerminalFunctionMeta"},
    )

    contactless_function: ContactlessFunction = Field(
        ...,
        description=ContactlessFunctionMeta.description.value,
        examples=ContactlessFunctionMeta.examples.value,
        json_schema_extra={"meta_class": "ContactlessFunctionMeta"},
    )


class PaymentAccounts(BaseQuantityItems, extra="forbid"):
    """Payment Accounts.

    Class Payment accounts consists of all additional attributes,
    in addition to the base quantity items attributes,
    that should be reported for Payment accounts (item 14).
    """

    quantity_item: QuantityItemsPaymentAccounts = Field(
        ...,
        description=QuantityItemsMeta.description.value,
        examples=QuantityItemsMeta.examples.value,
        json_schema_extra={"meta_class": "QuantityItemsMeta"},
    )

    payment_service_user: PaymentServiceUserPaymentAccounts = Field(
        ...,
        description=PaymentServiceUserMeta.description.value,
        examples=PaymentServiceUserMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentServiceUserMeta"},
    )

    type_of_account: TypeOfAccount = Field(
        ...,
        description=TypeOfAccountMeta.description.value,
        examples=TypeOfAccountMeta.examples.value,
        json_schema_extra={"meta_class": "TypeOfAccountMeta"},
    )
