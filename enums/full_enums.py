"""Commen enumn for schemas."""

from enum import IntEnum, StrEnum


class Environment(StrEnum):
    """Environment."""

    T = "T"

    P = "P"


class RoleInTransaction(IntEnum):
    """Role in transaction."""

    PayersPSP = 1

    PayeesPSP = 2


class PaymentServiceUser(StrEnum):
    """Payment service user."""

    P = "P"

    NMFIXP = "NMFIXP"

    MFI = "MFI"


class TransactionType(StrEnum):
    """Transaction type."""

    PUR = "PUR"

    RET = "RET"

    ORC = "ORC"

    P2P = "P2P"

    REV = "REV"

    CHB = "CHB"

    REP = "REP"


class RemoteInitiation(StrEnum):
    """Remote initiation."""

    R = "R"

    NR = "NR"


class Contactless(StrEnum):
    """Contactless."""

    CNT = "CNT"

    CNTL1 = "CNTL1"

    MAG = "MAG"

    OTH = "OTH"


class PaymentType(StrEnum):
    """Payment types."""

    CT0 = "CT0"

    CT1 = "CT1"

    DD = "DD"

    CPI = "CPI"

    CPA = "CPA"

    CWI = "CWI"

    CW0 = "CW0"

    CD0 = "CD0"

    CADVI = "CADVI"

    CADVA = "CADVA"

    EMP0 = "EMP0"

    MREM = "MREM"

    PI = "PI"

    CWOTC = "CWOTC"

    CDOTC = "CDOTC"


class CardFunction(StrEnum):
    """Card function."""

    CF1 = "CF1"
    CF2 = "CF2"
    CF3 = "CF3"
    CF4 = "CF4"
    CF5 = "CF5"
    CF6 = "CF6"


class EmoneyFunction(IntEnum):
    """E-money function."""

    Stored = 41

    Access = 42


class ContactlessFunction(IntEnum):
    """Contactless function."""

    ContactFunction = 10

    ContactlessFunction = 11

    Both = 12


class PaymentScheme(StrEnum):
    """Payment scheme."""

    PCS_MCRD = "PCS_MCRD"

    PCS_VISA = "PCS_VISA"

    PCS_CUP = "PCS_CUP"

    PCS_JCB = "PCS_JCB"

    PCS_AMEX = "PCS_AMEX"

    PCS_DINE = "PCS_DINE"

    PCS_OTH = "PCS_OTH"

    CTS_NPCI = "CTS_NPCI"

    CTS_SEPAI = "CTS_SEPAI"

    CTS_NPCOLO = "CTS_NPCOLO"

    CTS_EPCOLO = "CTS_EPCOLO"

    CTS_OTHSIP = "CTS_OTHSIP"

    CTS_SEPA = "CTS_SEPA"

    CTS_NPC = "CTS_NPC"

    CTS_OTHRIX = "CTS_OTHRIX"

    CTS_OTHXB = "CTS_OTHXB"

    CTS_ONUS = "CTS_ONUS"

    CTS_OTHO = "CTS_OTHO"


class CardType(IntEnum):
    """Card type."""

    Debit = 11

    DebitOnlyConsumer = 111

    DelayedDebit = 12

    Credit = 13

    CreditOnlyConsumer = 131

    Corporate = 16


class InitiationChannel(IntEnum):
    """Initiation channel."""

    NonElectronic = 1000

    PaperBased = 1200

    FileBatch = 2100

    SinglePayment = 2200

    OnlineBanking = 2210

    ECommerce = 2211

    MerchantInitiated = 2212

    OtherOnline = 2213

    Terminal = 2220

    ATM = 2221

    POSTerminal = 2222

    MobilePayment = 2230

    P2PMobile = 2231

    OtherMobile = 2232

    EMoneyStoredCard = 2240

    EMoneyAccountCard = 2251

    EMoneyOther = 2252

    RecurringSwish = 2270

    Other = 3000

    PISP = 5000


class PispInitiatedTransaction(StrEnum):
    """Pisp Initiated Transaction."""

    ICT0 = "ICT0"

    ICT1 = "ICT1"

    OTH = "OTH"


class QuantityItems(StrEnum):
    """Quantity Items, all Quantity Items."""

    CARD = "CARD"
    PA = "PA"
    POS = "POS"
    EMT = "EMT"
    ATM = "ATM"


class TypeOfAccount(StrEnum):
    """Type of account."""

    PA = "PA"

    EMA = "EMA"


class TerminalFunction(IntEnum):
    """Terminal function, all terminal functions."""

    AcceptingEMoney = 1

    NotAcceptingEmoney = 2

    EMoneyLoadUnload = 3

    EMoneyAndCard = 4

    CashWithdrawal = 5

    CashDeposit = 6

    CreditTransfer = 7

    CashWithdrawalAndDeposit = 8

    CashDepositAndCreditTransfer = 9

    CashWithdrawalAndCreditTransfer = 10

    CashWitdrawalDepositsAndCreditTransfer = 11


class ConcentrationRatioType(IntEnum):
    """Concentration ratio type."""

    ConcentrationByValue = 2

    ConcentrationByVolume = 3


class PaymentSystem(StrEnum):
    """Payment system."""

    RIX = "RIX"

    RIXI = "RIXI"

    BG = "BG"

    DC = "DC"


class ParticipantSector(StrEnum):
    """Participant sector."""

    S122C = "S122C"

    S121 = "S121"

    S13 = "S13"

    S125D1 = "S125D1"

    S12P = "S12P"

    SZP = "SZP"


class ParticipantType(IntEnum):
    """Participant type."""

    DirectParticipant = 1

    IndirectParticipant = 2


class PaymentSystemMetric(StrEnum):
    """Payment system metric."""

    T = "T"

    C = "C"

    P = "P"
