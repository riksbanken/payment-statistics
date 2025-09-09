"""Maps reported type to schema.

Used to determine which schema to validate against depending on reported_type.
"""

from enum import StrEnum

from pydantic import BaseModel

from payment_statistics_utils.enums.aggregates_enums import (
    PaymentTypeEMoney,
    PaymentTypeMoneyRemittances,
    PaymentTypeOTC,
    PaymentTypePaymentInitiationServices,
)
from payment_statistics_utils.enums.direct_debits_enums import PaymentTypeDirectDebits
from payment_statistics_utils.enums.payment_system_operators_enums import (
    PaymentSystemMetricConcentration,
    PaymentSystemMetricParticipants,
    PaymentSystemMetricTransactions,
)
from payment_statistics_utils.enums.quantity_items_enums import (
    QuantityItemsATMs,
    QuantityItemsCard,
    QuantityItemsEMoneyTerminal,
    QuantityItemsPaymentAccounts,
    QuantityItemsPosTerminal,
)
from payment_statistics_utils.enums.transaction_enums import (
    PaymentTypeCardPaymentAcquirer,
    PaymentTypeCardPaymentIssuer,
    PaymentTypeCashTransactionATMOwners,
    PaymentTypeCreditTransfer,
    PaymentTypeInstantCreditTransfer,
)
from payment_statistics_utils.schemas.aggregate_schemas import (
    OTC,
    EMoney,
    MoneyRemittances,
    PaymentInitiationServices,
)
from payment_statistics_utils.schemas.card_transaction_schemas import (
    CardPaymentAcquirer,
    CardPaymentIssuer,
)
from payment_statistics_utils.schemas.direct_debits_schema import DirectDebits
from payment_statistics_utils.schemas.payment_system_operators_schemas import (
    ConcentrationRatio,
    ParticipantsInPaymentSystems,
    TransactionsInPaymentSystems,
)
from payment_statistics_utils.schemas.quantity_items_schemas import (
    ATMs,
    Cards,
    EMoneyTerminals,
    PaymentAccounts,
    PosTerminals,
)
from payment_statistics_utils.schemas.transaction_schemas import (
    CashTransactionsATMOwners,
    CreditTransfer,
    InstantCreditTransfer,
)


VALIDATOR_MAPPING: dict[str, type[BaseModel]] = {}
types_to_validator: dict[type[StrEnum], type[BaseModel]] = {
    # Transactions
    PaymentTypeCardPaymentAcquirer: CardPaymentAcquirer,
    PaymentTypeCardPaymentIssuer: CardPaymentIssuer,
    PaymentTypeCashTransactionATMOwners: CashTransactionsATMOwners,
    PaymentTypeCreditTransfer: CreditTransfer,
    PaymentTypeInstantCreditTransfer: InstantCreditTransfer,
    # Direct debits
    PaymentTypeDirectDebits: DirectDebits,
    # Aggregates
    PaymentTypeEMoney: EMoney,
    PaymentTypeOTC: OTC,
    PaymentTypeMoneyRemittances: MoneyRemittances,
    PaymentTypePaymentInitiationServices: PaymentInitiationServices,
    # Payment system operators
    PaymentSystemMetricParticipants: ParticipantsInPaymentSystems,
    PaymentSystemMetricConcentration: ConcentrationRatio,
    PaymentSystemMetricTransactions: TransactionsInPaymentSystems,
    # Quantity items
    QuantityItemsATMs: ATMs,
    QuantityItemsCard: Cards,
    QuantityItemsEMoneyTerminal: EMoneyTerminals,
    QuantityItemsPosTerminal: PosTerminals,
    QuantityItemsPaymentAccounts: PaymentAccounts,
}

for types, validator in types_to_validator.items():
    for _type in list(types):
        VALIDATOR_MAPPING[_type] = validator
