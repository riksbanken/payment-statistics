"""Payment system operators schemas.

These schemas are reported by Payment system operators when they report the items in Section 7 in the regulations.
"""

from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from ..enums.field_metadata_enums import (
    ConcentrationRatioTypeMeta,
    ConcentrationRatioValueMeta,
    CounterPartyCountryPaymentSystemOperatorsMeta,
    IdMeta,
    NumberOfParticipantsMeta,
    NumberOfPaymentsystemoperatorsMeta,
    ParticipantSectorMeta,
    ParticipantTypeMeta,
    PaymentSystemMeta,
    PaymentSystemMetricMeta,
    PaymentTypePaymentSystemOperatorsMeta,
    ValueOfTransactionsMeta,
)
from ..enums.full_enums import (
    ConcentrationRatioType,
    ParticipantSector,
    ParticipantType,
    PaymentSystem,
)
from ..enums.payment_system_operators_enums import (
    PaymentSystemMetricConcentration,
    PaymentSystemMetricParticipants,
    PaymentSystemMetricTransactions,
    PaymentTypePaymentSystems,
)
from ..utils.field_validaton_functions import validate_country
from ..utils.types import Country


class BasePaymentSystemOperators(BaseModel, extra="forbid"):
    """Base payment system operators.

    Class Base payment system operators consist of all attributes that are relevant for all the items in the regulation,
    that payment service operators should report.

    """

    id: str = Field(
        ...,
        description=IdMeta.description.value,
        examples=IdMeta.examples.value,
        json_schema_extra={"meta_class": "IdMeta"},
    )

    payment_system: PaymentSystem = Field(
        ...,
        description=PaymentSystemMeta.description.value,
        examples=PaymentSystemMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSystemMeta"},
    )


class TransactionsInPaymentSystems(BasePaymentSystemOperators, extra="forbid"):
    """Transactions in payment systems.

    Class transaction in payment systems consists of all additional attributes,
    in addition to the Base payment system operators attributes,
    that should be reported for transactions in payment systems.
    """

    payment_system_metric: PaymentSystemMetricTransactions = Field(
        ...,
        description=PaymentSystemMetricMeta.description.value,
        examples=PaymentSystemMetricMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSystemMetricMeta"},
    )

    payment_type: PaymentTypePaymentSystems = Field(
        ...,
        description=PaymentTypePaymentSystemOperatorsMeta.description.value,
        examples=PaymentTypePaymentSystemOperatorsMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypePaymentSystemOperatorsMeta"},
    )

    number_of: int = Field(
        ge=1,
        description=NumberOfPaymentsystemoperatorsMeta.description.value,
        examples=NumberOfPaymentsystemoperatorsMeta.examples.value,
        json_schema_extra={"meta_class": "NumberOfPaymentsystemoperatorsMeta"},
    )

    value_of_transactions: Decimal = Field(
        ge=0.00,
        decimal_places=2,
        description=ValueOfTransactionsMeta.description.value,
        examples=ValueOfTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "ValueOfTransactionsMeta"},
    )

    counterparty_country: Country = Field(
        ...,
        description=CounterPartyCountryPaymentSystemOperatorsMeta.description.value,
        examples=CounterPartyCountryPaymentSystemOperatorsMeta.examples.value,
        json_schema_extra={
            "meta_class": "CounterPartyCountryPaymentSystemOperatorsMeta"
        },
    )

    @field_validator("counterparty_country", mode="after")
    @classmethod
    def validate_counterparty_country(cls, counterparty_country: str) -> str:
        """Validate that counterparty_country is alpha_2."""
        return validate_country(counterparty_country)


class ConcentrationRatio(BasePaymentSystemOperators, extra="forbid"):
    """Concentration ratio.

    Class concentration ratio consists of all additional attributes,
    in addition to the Base payment system operators attributes,
    that should be reported for concentration ratio.
    """

    payment_system_metric: PaymentSystemMetricConcentration = Field(
        ...,
        description=PaymentSystemMetricMeta.description.value,
        examples=PaymentSystemMetricMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSystemMetricMeta"},
    )

    concentration_ratio_type: ConcentrationRatioType = Field(
        ...,
        description=ConcentrationRatioTypeMeta.description.value,
        examples=ConcentrationRatioTypeMeta.examples.value,
        json_schema_extra={"meta_class": "ConcentrationRatioTypeMeta"},
    )

    concentration_ratio_value: Decimal = Field(
        ge=0.00,
        le=1.00,
        decimal_places=2,
        description=ConcentrationRatioValueMeta.description.value,
        examples=ConcentrationRatioValueMeta.examples.value,
        json_schema_extra={"meta_class": "ConcentrationRatioValueMeta"},
    )


class ParticipantsInPaymentSystems(BasePaymentSystemOperators, extra="forbid"):
    """Partitcipants in payment systems.

    Class participants in payments systems consists of all additional attributes,
    in addition to the Base payment system operators attributes,
    that should be reported for participants in payment systems.
    """

    payment_system_metric: PaymentSystemMetricParticipants = Field(
        ...,
        description=PaymentSystemMetricMeta.description.value,
        examples=PaymentSystemMetricMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentSystemMetricMeta"},
    )

    number_of_participants: int = Field(
        ge=0,
        description=NumberOfParticipantsMeta.description.value,
        examples=NumberOfParticipantsMeta.examples.value,
        json_schema_extra={"meta_class": "NumberOfParticipantsMeta"},
    )

    participant_type: ParticipantType = Field(
        ...,
        description=ParticipantTypeMeta.description.value,
        examples=ParticipantTypeMeta.examples.value,
        json_schema_extra={"meta_class": "ParticipantTypeMeta"},
    )

    participant_sector: ParticipantSector = Field(
        ...,
        description=ParticipantSectorMeta.description.value,
        examples=ParticipantSectorMeta.examples.value,
        json_schema_extra={"meta_class": "ParticipantSectorMeta"},
    )
