"""Maps reported type to schema.

Used to determine which schema to validate against depending on reported_type.
"""

from enum import StrEnum

from pydantic import BaseModel

from ..enums.aggregates_enums import (
    PaymentTypeEMoney,
    PaymentTypeMoneyRemittances,
    PaymentTypeOTC,
    PaymentTypePaymentInitiationServices,
)
from ..enums.direct_debits_enums import PaymentTypeDirectDebits
from ..enums.payment_system_operators_enums import (
    PaymentSystemMetricConcentration,
    PaymentSystemMetricParticipants,
    PaymentSystemMetricTransactions,
)
from ..enums.quantity_items_enums import (
    QuantityItemsATMs,
    QuantityItemsCard,
    QuantityItemsEMoneyTerminal,
    QuantityItemsPaymentAccounts,
    QuantityItemsPosTerminal,
)
from ..enums.transaction_enums import (
    PaymentTypeCardPaymentAcquirer,
    PaymentTypeCardPaymentIssuer,
    PaymentTypeCashTransactionATMOwners,
    PaymentTypeCreditTransfer,
    PaymentTypeInstantCreditTransfer,
)
from ..schemas.aggregate_schemas import (
    OTC,
    EMoney,
    MoneyRemittances,
    PaymentInitiationServices,
)
from ..schemas.card_transaction_schemas import (
    CardPaymentAcquirer,
    CardPaymentIssuer,
)
from ..schemas.direct_debits_schema import DirectDebits
from ..schemas.payment_system_operators_schemas import (
    ConcentrationRatio,
    ParticipantsInPaymentSystems,
    TransactionsInPaymentSystems,
)
from ..schemas.quantity_items_schemas import (
    ATMs,
    Cards,
    EMoneyTerminals,
    PaymentAccounts,
    PosTerminals,
)
from ..schemas.transaction_schemas import (
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
