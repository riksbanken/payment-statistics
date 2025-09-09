"""Enums containing metadata for Pydantic Fields."""

from enum import Enum


class EnvironmentMeta(Enum):
    """Metadata for environment."""

    description = "If the report is a test (T) or for production (P)."

    description_swe = "Om rapporten är ett test (T) eller om den är för produktion (P)."

    examples = None

    name = "Environment"

    name_swe = "Miljö"

    field = "environment"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReporterIdMeta(Enum):
    """Metadata for reporter_id."""

    description = "The reporting institution's corporate registration number."

    description_swe = "Uppgiftslämnarens organisationsnummer."

    examples = ["55XXXX-XXXX"]

    name = "Reporter id"

    name_swe = "Rapportörens id"

    field = "reporter_id"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportDatetimeMeta(Enum):
    """Metadata for report_datetime."""

    description = "Date and time when the report file is created. Reported as UTC+1."

    description_swe = "Datum och tid när rapporten skapades. Rapporteras som UTC+1."

    examples = ["2026-11-06 12:20:01"]

    name = "Report date"

    name_swe = "Rapporteringsdatum"

    field = "report_datetime"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class SchemaVersionMeta(Enum):
    """Metadata for schema_version."""

    description = "Refers to which version of the schema is used for reporting."

    description_swe = "Avser vilken version av schemat som används vid rapporteringen."

    examples = None

    name = "Schema version"

    name_swe = "Schemaversion"

    field = "schema_version"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportPartMeta(Enum):
    """Metadata for report_part."""

    description = "The attribute is used to split the same item into different JSON files. The attribute is optional to use, but if used, the attribute must always be named the same for the flow of transactions that the file corresponds to."

    description_swe = "Attributet används för att dela upp en och samma post i olika JSON-filer. Attributet är frivilligt att använda, men om det används måste attributet alltid heta samma sak för det flöde av transaktioner som filen motsvarar."

    examples = ["system1", "cross-border", "schemeX"]

    name = "Report part"

    name_swe = "Rapportdel"

    field = "report_part"

    mandatory = "No"

    mandatory_swe = "Nej"


class ItemsMeta(Enum):
    """Metadata for items."""

    description = "Refers to the actual data to be reported and consists of transaction data or aggregated data across transactions or quantity items."

    description_swe = "Avser den faktiska data som ska rapporteras och består av antingen transaktionsdata eller aggregerad data över transaktioner eller antalsposter."

    examples = None

    name = "Items"

    name_swe = "Poster"

    field = "items"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class DateFromMeta(Enum):
    """Metadata for date_from."""

    description = (
        "The date from which the file contains data from, inclusive. Reported as UTC+1."
    )

    description_swe = (
        "Det datum som filen innehåller data i från, inklusiv. Rapporteras som UTC+1"
    )

    examples = ["2025-01-02"]

    name = "Date from"

    name_swe = "Datum från"

    field = "date_from"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class DateToMeta(Enum):
    """Metadata for date_to."""

    description = (
        "The date the file contains data up to and including. Reported as UTC+1."
    )

    description_swe = (
        "Det datum som filen innehåller data till och med. Rapporteras som UTC+1."
    )

    examples = ["2025-01-02"]

    name = "Date to"

    name_swe = "Datum till"

    field = "date_to"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportedPaymentTypeTransactionsMeta(Enum):
    """Metadata for reported_payment_type."""

    description = "Type of item according to Section 3 (1-6) of the regulations that the JSON file contains data about."

    description_swe = (
        "Typ av post enligt 3 § 1-6 i föreskrifterna som JSON-filen innehåller data om."
    )

    examples = None

    name = "Reported payment type"

    name_swe = "Rapporterad betalningstyp"

    field = "reported_payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportedPaymentTypeAggregateMeta(Enum):
    """Metadata for reported_payment_type."""

    description = "Type of item according to Section 3 (8-12) of the regulations that the JSON file contains data about."

    description_swe = "Typ av post enligt 3 § 8-12 i föreskrifterna som JSON-filen innehåller data om."

    examples = None

    name = "Reported payment type"

    name_swe = "Rapporterad betalningstyp"

    field = "reported_payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportedPaymentTypeDDMeta(Enum):
    """Metadata for reported_payment_type."""

    description = "Type of item according to Section 3 (7) of the regulations that the JSON file contains data about."

    description_swe = (
        "Typ av post enligt 3 § 7 i föreskrifterna som JSON-filen innehåller data om."
    )

    examples = None

    name = "Reported payment type"

    name_swe = "Rapporterad betalningstyp"

    field = "reported_payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportedQuantityItemMeta(Enum):
    """Metadata for reported_quantity_item."""

    description = "Type of item according to Section 3 (13-17) of the regulations that the JSON file contains data about."

    description_swe = "Typ av post enligt enligt 3 § 13-17 i föreskrifterna som JSON-filen innehåller data om."

    examples = None

    name = "Reported quantity item"

    name_swe = "Rapporterad antalspost"

    field = "reported_quantity_item"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ReportedPaymentSystemMetricMeta(Enum):
    """Metadata for payment_system_metric."""

    description = "Refers to the type of data the JSON file contains. Whether it is transaction data, concentration rates or participant information."

    description_swe = "Avser vilken typ av data som JSON-filen innehåller. Om det är transaktionsdata, koncentrationsgrader eller deltagarinformation."

    examples = None

    name = "Reported payment system metric"

    name_swe = "Rapporterad betalningssystemsmetrik"

    field = "reported_payment_system_metric"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PeriodMeta(Enum):
    """Metadata for period."""

    description = "Refers to the last day of the period (month, quarter, half-year or year) to which the reporting relates."

    description_swe = "Avser sista dagen i den period (månad, kvartal, halvår eller år) som rapporteringen avser."

    examples = None

    name = "Period"

    name_swe = "Period "  # Using a whitespace to not be equal to name

    field = "period"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class IdMeta(Enum):
    """Metadata for id."""

    description = "Id for each transaction or aggregate. Each reporter decides how it is generated, but must not contain any personal information. Only used for communication about reported data."

    description_swe = "Id för varje transaktion eller aggregat. Varje reportör bestämmer själva hur det genereras, men det får inte innehålla några personuppgifter. Används endast för kommunikation om rapporterad data."

    examples = None

    name = "Id"

    name_swe = "Id "  # Using a whitespace to not be equal to name

    field = "id"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TransactionInitiatedMeta(Enum):
    """Metadata for transaction_initiated."""

    description = "Local (merchant's) date and time when the transaction is initiated, can be rounded to nearest hour. Reported as 'Y-m-d H:M:S'."

    description_swe = "Lokalt (handlarens) datum och tid när transaktionen initieras, kan avrundas till närmaste timme. Rapporteras som 'Y-m-d H:M:S'."

    examples = ["2025-01-02 12:00:00", "2025-01-02 12:20:01"]

    name = "Transaction initiated"

    name_swe = "Transaktion initierad"

    field = "transaction_initiated"

    mandatory = "Partly. The attribute is mandatory for Mastercard transactions, for other schemes the attribute is reported if available."

    mandatory_swe = "Delvis. Attributet är obligatoriskt för Mastercard transaktioner, för övriga betalningsordrar/scheme rapporteras attributet om det finns tillgängligt. "


class TransactionTimeMeta(Enum):
    """Metadata for transaction_time."""

    description = "Date and time when the payer's or payee's account is debited or credited, can be rounded to neares hour. Reported as 'Y-m-d H:M:S' in UTC+1."

    description_swe = "Datum och tid när betalarens eller betalningsmottagarens konto debiteras eller krediteras, kan avrundas till närmaste timme. Rapporteras som 'Y-m-d H:M:S i UTC+1."

    examples = ["2025-01-02 12:00:00", "2025-01-02 12:20:01"]

    name = "Transaction time"

    name_swe = "Transaktionstidpunkt"

    field = "transaction_time"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TransactionClearedMeta(Enum):
    """Meatadata for transaction_cleared."""

    description = "Date when the transaction is cleared. Reported as 'Y-m-d' in UTC+1."

    description_swe = (
        "Datum när transaktionen clearas. Rapporteras som 'Y-m-d' in UTC+1."
    )

    examples = ["2024-01-01, 2024-12-31"]

    name = "Transaction cleared"

    name_swe = "Transaktion clearad"

    field = "transaction_cleared"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class CounterPartyCountryCardMeta(Enum):
    """Metadata for counterparty_country."""

    description = "The payer's PSP states the country of residence of the payee's PSP. The payee's PSP states the country of residence of the payer's PSP. According to ISO 3166-1, alpha-2 country code."

    description_swe = "Betalarens betaltjänstleverantör anger hemvistland för betalningsmottagarens betaltjänstleverantör. Betalningsmottagarens betaltjänstleverantör anger hemvistland för betalarens betaltjänstleverantör. Enligt ISO 3166-1, alpha-2 landkoder."

    examples = ["SE", "NO"]

    name = "Counterparty country"

    name_swe = "Motpartsland"

    field = "counterparty_country"

    mandatory = (
        "No. Card issuers report this attribute if the information is available. "
    )

    mandatory_swe = "Nej. Kortutgivare rapporterar detta attribut i den mån dessa uppgifter finns tillgängliga."


class CounterPartyCountryCardAcquirersMeta(Enum):
    """Metadata for counterparty_country."""

    description = "The payer's PSP states the country of residence of the payee's PSP. The payee's PSP states the country of residence of the payer's PSP. According to ISO 3166-1, alpha-2 country code."

    description_swe = "Betalarens betaltjänstleverantör anger hemvistland för betalningsmottagarens betaltjänstleverantör. Betalningsmottagarens betaltjänstleverantör anger hemvistland för betalarens betaltjänstleverantör. Enligt ISO 3166-1, alpha-2 landkoder."

    examples = ["SE", "NO"]

    name = "Counterparty country"

    name_swe = "Motpartsland"

    field = "counterparty_country"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class CounterPartyCountryOtherMeta(Enum):
    """Metadata for counterparty_country."""

    description = "The payer's PSP states the country of residence of the payee's PSP. The payee's PSP states the country of residence of the payer's PSP. IBAN is primarily used as an identifier (secondarily BIC), and the counterparty country is then de facto the country of the payer's or payee's account number. According to ISO 3166-1, alpha-2 country code."

    description_swe = "Betalarens betaltjänstleverantör anger hemvistland för betalningsmottagarens betaltjänstleverantör. Betalningsmottagarens betaltjänstleverantör anger hemvistland för betalarens betaltjänstleverantör. IBAN används i första hand som identifierare (andra hand BIC) och motpartslandet är de facto då landet för betalarens eller betalningsmottagarens kontonummer. Enligt ISO 3166-1, alpha-2 landkoder."

    examples = ["SE", "NO"]

    name = "Counterparty country"

    name_swe = "Motpartsland"

    field = "counterparty_country"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class CounterPartyCountryPaymentSystemOperatorsMeta(Enum):
    """Metadata for counterparty_country."""

    description = "Cross-border transactions should be distinguished from domestic transactions and reported according to the residence of the sending and receiving participants. Distributed by individual countries according to ISO 3166-1, alpha-2 country code."

    description_swe = "Transaktioner över landsgränser ska särskiljas från inhemska transaktioner och rapporteras efter var de sändande och mottagande deltagarna har sin hemvist. Fördelas på enskilda länder enligt ISO 3166-1, alpha-2 landkoder."

    examples = ["SE", "NO"]

    name = "Counterparty country"

    name_swe = "Motpartsland"

    field = "counterparty_country"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class QuantityItemsMeta(Enum):
    """Metadata for quantity_items."""

    description = "Type of quantity item the reporting refers to according to Section 3 (13-17) in the regulations."

    description_swe = " Typ av antalspost som rapporteringen avser enligt 3 § (13-17) i föreskrifterna."

    examples = None

    name = "Quantity item"

    name_swe = "Post"

    field = "quantity_item"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class MerchantLocationMeta(Enum):
    """Metadata for merchant_location."""

    description = "For card-based transactions that are not initiated remotely, the country is the location where the physical terminal is located. For card-based transactions initiated remotely, the country is where the merchant is located. According to ISO 3166-1, alpha-2 country code."

    description_swe = "För kortbaserade transaktioner som inte initieras på distans är landet den plats där den fysiska terminalen är belägen. För kortbaserade transaktioner som initieras på distans är landet där handlaren är belägen. Enligt ISO 3166-1, alpha-2 landskod."

    examples = ["SE", "NO"]

    name = "Merchant location"

    name_swe = "Handlarens plats"

    field = "merchant_location"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class MerchantLocationQuantityMeta(Enum):
    """Metadata for merchant_location."""

    description = "Refers to the country where the terminal is located. According to ISO 3166-1, alpha-2 country code."

    description_swe = (
        "Avser land där terminal är belägen. Enligt ISO 3166-1, alpha-2 landskod."
    )

    examples = ["SE", "NO"]

    name = "Merchant location"

    name_swe = "Handlarens plats"

    field = "merchant_location"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class MerchantLocationATMtransactionMeta(Enum):
    """Metadata for merchant_location."""

    description = "Refers to the country where the ATM is located. According to ISO 3166-1, alpha-2 country code."

    description_swe = "Avser land där uttagsautomaten är belägen. Enligt ISO 3166-1, alpha-2 landskod."

    examples = ["SE", "NO"]

    name = "Merchant location"

    name_swe = "Handlarens plats"

    field = "merchant_location"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentTypeTransactionsMeta(Enum):
    """Metadata for payment_type."""

    description = "Type of item according to Section 3 (1-6) of the regulations to which the reporting relates."

    description_swe = (
        "Typ av post enligt enligt 3 § 1-6 i föreskrifterna som rapporteringen avser."
    )

    examples = None

    name = "Payment type"

    name_swe = "Betalningstyp"

    field = "payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentTypeAggregateMeta(Enum):
    """Metadata for payment_type."""

    description = "Type of item according to Section 3 (8-12) of the regulations to which the reporting relates."

    description_swe = (
        "Typ av post enligt enligt 3 § 8-12 i föreskrifterna som rapporteringen avser."
    )

    examples = None

    name = "Payment type"

    name_swe = "Betalningstyp"

    field = "payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentTypePaymentSystemOperatorsMeta(Enum):
    """Metadata for payment_type."""

    description = "Type of transaction according to Section 7 (3-11) of the regulations to which the reporting relates."

    description_swe = (
        "Typ av transaktion enligt 7 § 3-11 i föreskrifterna som rapporteringen avser."
    )

    examples = None

    name = "Payment type"

    name_swe = "Betalningstyp"

    field = "payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentTypeDDMeta(Enum):
    """Metadata for payment_type."""

    description = "Type of item according to Section 3 (7) of the regulations to which the reporting relates."

    description_swe = (
        "Typ av post enligt enligt 3 § 7 i föreskrifterna som rapporteringen avser."
    )

    examples = None

    name = "Payment type"

    name_swe = "Betalningstyp"

    field = "payment_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TransactionDayMeta(Enum):
    """Metadata for transaction_day."""

    description = "Date when the payer's or payee's account is debited or credited. Reported as 'Y-m-d' in UTC+1."

    description_swe = "Datum när betalarens eller betalningsmottagarens konto debiteras eller krediteras. Rapporteras som 'Y-m-d i UTC+1."

    examples = ["2024-01-01"]

    name = "Transaction day"

    name_swe = "Transaktionsdag"

    field = "transaction_day"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class InitiationCountryMeta(Enum):
    """Metadata for initiation_country."""

    description = "Country of domicile of the payer. Accorting to ISO 3166-1, alpha-2 country code."

    description_swe = "Betalarens hemvistland. Enligt ISO 3166-1, alpha-2 landkoder."

    examples = ["SE", "NO"]

    name = "Initiation country"

    name_swe = "Initieringsland"

    field = "initiation_country"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class RoleInTransactionMeta(Enum):
    """Metadata for role_in_transaction."""

    description = (
        "Indicates whether the transaction is reported from the payer's or payee's PSP."
    )

    description_swe = "Avser om transaktionen rapporteras från betalarens eller betalningsmottagarens betaltjänstleverantör."

    examples = None

    name = "Role in the transaction"

    name_swe = "Betaltjänstleverantörens roll i transaktionen"

    field = "role_in_transaction"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentServiceUserMeta(Enum):
    """Metadata for payment_service_user."""

    description = "Refers to a natural or legal person using a payment service as a payer, payee or both."

    description_swe = "Avser en fysisk eller en juridisk person som utnyttjar en betaltjänst i egenskap av betalare, betalningsmottagare eller båda."

    examples = None

    name = "Type of payment service user"

    name_swe = "Typ av betaltjänstanvändare"

    field = "payment_service_user"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TransactionTypeMeta(Enum):
    """Metadata for transaction_type."""

    description = "Refers to the type of card transaction reported."

    description_swe = "Avser vilken typ av korttransaktion som rapporteras."

    examples = None

    name = "Transaction type"

    name_swe = "Transaktionstyp"

    field = "transaction_type"

    mandatory = "Partly. The attribute is mandatory when payment type (payment_type) is Card-based payment transactions."

    mandatory_swe = "Delvis. Attributet är obligatoriskt när betalningstyp (payment_type) är kortbaserade betalningstransaktioner."


class TransactionValueOtherMeta(Enum):
    """Metadata for transaction_value."""

    description = "The value of the transaction/-s in the currency of the transaction."

    description_swe = "Avser transaktionsbelopp i transaktionsvalutan."

    examples = None

    name = "Transaction amount in transaction currency"

    name_swe = "Transaktionsbelopp i transaktionsvaluta"

    field = "transaction_value"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TransactionCurrencyMeta(Enum):
    """Metadata for transaction_currency."""

    description = (
        "Currency code of the transaction currency. Accorting to ISO 4217-1, alpha-3."
    )

    description_swe = "Valutakod för transaktionsvalutan. Enligt ISO 4217-1, alpha-3."

    examples = ["SEK", "NOK"]

    name = "Currency code transaction currency"

    name_swe = "Valutakod transaktionsvaluta"

    field = "transaction_currency"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class AccountValueMeta(Enum):
    """Metadata for account_value."""

    description = "The value of the transaction in account currency or card currency, for example SEK if the account is in SEK or if it is a Swedish-issued card. That is, the amount debited from the account or card."

    description_swe = "Transaktionens värde i kontovaluta eller kortvaluta, exempelvis SEK om kontot är i SEK eller om det är ett svenskt utgivet kort. Det vill säga det belopp som debiteras kontot eller kortet."

    examples = None

    name = "Transaction amount in account currency"

    name_swe = "Transaktionsbelopp i kontovaluta"

    field = "account_value"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class AccountCurrencyMeta(Enum):
    """Metadata for account_currency."""

    description = (
        "Currency code of the account currency. According to ISO 4217-1, alpha-3"
    )

    description_swe = "Valutakod för kontovalutan. Enligt ISO 4217-1, alpha-3"

    examples = ["SEK", "NOK"]

    name = "Currency code account currency"

    name_swe = "Valutakod kontovalutan"

    field = "account_currency"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class AccountValueInstantCreditTransfersMeta(Enum):
    """Metadata for account_value."""

    description = "The value of the transaction in account currency, for example SEK if the account is in SEK. That is, the amount debited from the account."

    description_swe = "Transaktionens värde i kontovalutan, exempelvis SEK om kontot är i SEK. Det vill säga det belopp som debiteras kontot."

    examples = None

    name = "Transaction amount in account currency"

    name_swe = "Transaktionsbelopp i kontovaluta"

    field = "account_value"

    mandatory = (
        "Partly. Mandatory and should only be specified for sent/outgoing transactions."
    )

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges för skickade/avgående transaktioner."


class AccountCurrencyInstantCreditTransfersMeta(Enum):
    """Metadata for account_currency."""

    description = (
        "Currency code of the account currency. According to ISO 4217-1, alpha-3."
    )

    description_swe = "Valutakod för kontovalutan. Enligt ISO 4217-1, alpha-3."

    examples = ["SEK", "NOK"]

    name = "Currency code account currency"

    name_swe = "Valutakod kontovalutan"

    field = "account_currency"

    mandatory = (
        "Partly. Mandatory and should only be specified for sent/outgoing transactions."
    )

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges för skickade/avgående transaktioner."


class NumberOfMeta(Enum):
    """Metadata for number_of."""

    description = (
        "Number of transactions included in each aggregate. Stated in integers."
    )

    description_swe = (
        "Antal transaktioner som ingår i respektive aggregat. Anges i heltal."
    )

    examples = None

    name = "Number of transactions"

    name_swe = "Antal transaktioner"

    field = "number_of"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class NumberOfPaymentsystemoperatorsMeta(Enum):
    """Metadata for number_of."""

    description = (
        "Number of transactions processed in the payment system. Stated in integers."
    )

    description_swe = (
        "Antal transaktioner som är processade i betalningssystemet. Anges i heltal."
    )

    examples = None

    name = "Number"

    name_swe = "Antal"

    field = "number_of"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class NumberOfQuanityItemsMeta(Enum):
    """Metadata for number_of."""

    description = "Refers to the number of the quantity item to which the reporting refers according to Section 3 (13-17) of the regulations. Stated in intergers."

    description_swe = "Avser antalet av den antalspost som rapporteringen avser i 3 § (13-17) i föreskrifterna. Anges i heltal."

    examples = None

    name = "Number of"

    name_swe = "Antal"

    field = "number_of"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class SniCodeMeta(Enum):
    """Metadata for sni_code."""

    description = "Refers to industry classification at the 5-digit level. For foreign counterparties, or in exceptional cases where an SNI code is missing, '00000' is indicated."

    description_swe = "Avser näringsgrensindelning på 5-siffrig nivå. För utländska motparter eller om SNI kod, i undantagsfall, saknas anges '00000'."

    examples = None

    name = "SNI-Code"

    name_swe = "SNI-kod"

    field = "sni_code"

    mandatory = "Partly. Mandatory and should only be specified when a non-MFI excl. private persons is the payee. "

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges när icke-MFI exkl. privatpersoner är betalningsmottagare."


class PispInitiatedTransactionMeta(Enum):
    """Metadata for pisp_initiated_transaction."""

    description = "Refers to the type of payment that has been initiated."

    description_swe = "Avser vilken typ av betalning som har initierats."

    examples = None

    name = "PISP initiated transaction"

    name_swe = "PISP initierad transaktion"

    field = "pisp_initiated_transaction"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class LocalityMeta(Enum):
    """Metadata for locality."""

    description = "The postal locality where the cash withdrawal or deposit took place."

    description_swe = (
        "Den postort som kontantuttaget eller kontantinsättningen har skett i."
    )

    examples = ["KIL", "Luleå"]

    name = "Locality"

    name_swe = "Postort"

    field = "locality"

    mandatory = "Partly. Mandatory and should only be specified when attribute merchant location (merchant_location) is Sweden."

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges om attribut handlarens plats (merchant_location) är Sverige."


class InitiationChannelMeta(Enum):
    """Metadata for initiation_channel."""

    description = "Refers to a service for initiating a payment order at the request of the payment service user."

    description_swe = "Avser en tjänst för att initiera en betalningsorder på begäran av betaltjänstanvändaren."

    examples = None

    name = "Initiation channel"

    name_swe = "Initieringskanal"

    field = "initiation_channel"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class InitiationChannelCreditTransferMeta(Enum):
    """Metadata for initiation_channel."""

    description = "Refers to a service to initiate a payment order at the request of the payment service user."

    description_swe = "Avser en tjänst för att initiera en betalningsorder på begäran av betaltjänstanvändaren."

    examples = None

    name = "Initiation channel"

    name_swe = "Initieringskanal"

    field = "initiation_channel"

    mandatory = (
        "Partly. Mandatory and should only be specified for sent/outgoing transactions."
    )

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges för skickade/avgående transaktioner."


class RemoteInitiationMeta(Enum):
    """Metadata for remote_initiation."""

    description = "Indicates whether the transaction is initiated remotely or not. Same meaning as in the definition in Article 4(6) of Directive (EU) 2015/2366."

    description_swe = "Avser om transaktionen initieras på distans eller inte. Samma betydelse som framgår av definitionen i artikel 4.6 i direktiv (EU) 2015/2366."

    examples = None

    name = "Remote/non-remote"

    name_swe = "Distans/icke-distans"

    field = "remote_initiation"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class RemoteInitiationCreditTransfersMeta(Enum):
    """Metadata for remote_initiation."""

    description = "Refers to whether the transaction is initiated remotely or not. Same meaning as in the definition in Article 4(6) of Directive (EU) 2015/2366."

    description_swe = "Avser om transaktionen initieras på distans eller inte. Samma betydelse som framgår av definitionen i artikel 4.6 i direktiv (EU) 2015/2366."

    examples = None

    name = "Remote initiation"

    name_swe = "Distans/icke-distans"

    field = "remote_initiation"

    mandatory = (
        "Partly. Mandatory and should only be specified for sent/outgoing transactions."
    )

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges för skickade/avgående transaktioner."


class ContactlessMeta(Enum):
    """Metadata for contactless."""

    description = "Contactless payment is a payment made using a card or other means where the payer and the merchant (and/or their equipment) are in the same physical location and where the communication between the portable device and the point of sale is done using contactless technology. Contact is for example when the cardholder inserts the card into the POS terminal or swipes the card's magnetic stripe in the terminal."

    description_swe = "Kontaktlös betalning är med hjälp av ett kort eller andra medel där betalaren och handlaren (och/eller deras utrustning) befinner sig på samma fysiska plats och där kommunikationen mellan den bärbara enheten och försäljningsstället sker med kontaktlös teknik. Med kontakt är exempelvis när kortinnehavaren sätter in kortet i POS-terminalen eller drar kortets magnetspår i terminalen."

    examples = None

    name = "Contact/contactless"

    name_swe = "Kontakt/kontaktlös"

    field = "contactless"

    mandatory = "Partly. Mandatory and should only be specified when the payment is made non-remotely. "

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges om betalningen sker på icke-distans."


class PaymentSchemeMeta(Enum):
    """Metadata for payment_scheme."""

    description = "Payment scheme is a set of formal, standardised and common rules enabling the transfer of value between end-users by means of electronic payment instruments. It is managed by a governance body."

    description_swe = "Betalningsordning är en uppsättning formella, standardiserade och gemensamma regler som gör det möjligt att överföra värde mellan slutanvändare med hjälp av ett elektroniskt betalningsinstrument. Ordningen administreras av ett ledningsorgan."

    examples = None

    name = "Payment scheme"

    name_swe = "Betalningsordning"

    field = "payment_scheme"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class CardTypeMeta(Enum):
    """Metadata for card_type."""

    description = (
        "Refers to what type of card it is. Pre-paid cards are considered debit cards."
    )

    description_swe = (
        "Avser vilken typ av kort det är. Pre-paid kort räknas som debetkort."
    )

    examples = None

    name = "Card type"

    name_swe = "Typ av kort"

    field = "card_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class MerchantCategoryMeta(Enum):
    """Metadata for merchant_category."""

    description = "A four-digit number used to classify companies by the goods or services they provide. According to ISO 18245."

    description_swe = "Ett fyrsiffrigt nummer, som används för att klassificera företag efter de varor eller tjänster de tillhandahåller. Anges enligt ISO 18245."

    examples = ["0742", "6211"]

    name = "MCC-code"

    name_swe = "MCC-kod"

    field = "merchant_category"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TerminalFunctionMeta(Enum):
    """Metadata for terminal_function."""

    description = "Refers to the functions that terminals have."

    description_swe = "Avser vilka funktioner som terminalerna har."

    examples = None

    name = "Terminal function"

    name_swe = "Terminalfunktionalitet"

    field = "terminal_function"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ContactlessFunctionMeta(Enum):
    """Metadata for contactless_function."""

    description = "Refers to whether terminals and cards have contact and/or contactless functionality."

    description_swe = (
        "Avser om terminaler och kort har kontakt och/eller kontaktlös funktion."
    )

    examples = None

    name = "Contact/contactless function"

    name_swe = "Kontakt/kontaktlös funktion"

    field = "contactless_function"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class EMoneyFunctionMeta(Enum):
    """Metadata for e_money_function."""

    description = "Refers to whether e-money can be stored directly on the card or whether the card provides access to e-money stored in an e-money account."

    description_swe = "Avser om e-pengar kan förvaras direkt på kortet eller om kortet ger tillgång till e-pengar förvarade på ett e-pengakonto."

    examples = None

    name = "E-money functions"

    name_swe = "E-pengafunktioner"

    field = "e_money_function"

    mandatory = "Partly. Mandatory and should only be specified if attribute card_function is reported with e-money function."

    mandatory_swe = "Delvis. Obligatoriskt och ska endast anges om attribut card_function är rapporterat med e-penga funtion."


class CardFunctionMeta(Enum):
    """Metadata for card_function."""

    description = "Refers to the functionalities the card has, such as cash or payment functions. If a customer has chosen to turn off any function on their card, this is not taken into account, it is the card's 'original' functions that define the card's functions."

    description_swe = "Avser vilka funktionaliteter kortet har som exempelvis kontant- eller betalfunktion. Om en kund har valt att slå av någon funktion på sitt kort tas ingen hänsyn till det utan kortets 'ursprungliga' funktioner är de som definierar kortets funktioner."

    examples = None

    name = "Card function"

    name_swe = "Kortfunktionalitet"

    field = "card_function"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class TypeOfAccountMeta(Enum):
    """Metadata for type_of_account."""

    description = "Refers to the type of payment account, whether the account is a payment account or e-money account."

    description_swe = "Avser vilken typ av betalkonto det är, om kontot är ett betalkonto eller e-pengakonto."

    examples = None

    name = "Type of payment account"

    name_swe = "Typ av betalkonto"

    field = "type_of_account"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentSystemMeta(Enum):
    """Metadata for payment_system."""

    description = "Name of the payment system to which the reporting relates."

    description_swe = "Namn på betalningssystemt som rapporteringen avser."

    examples = None

    name = "Payment system"

    name_swe = "Betalningssystem"

    field = "payment_system"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class PaymentSystemMetricMeta(Enum):
    """Metadata for payment_system."""

    description = "Refers to the type of data reported. Whether it is transaction data, concentration levels or participant information."

    description_swe = "Avser vilken typ av data som rapporteras. Om det är transaktionsdata, koncentrationsgrader eller deltagarinformation."

    name = "Payment system metric"

    examples = None

    name_swe = "Typ av information / Betalningssystemmetrik"

    field = "payment_system_metric"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ValueOfTransactionsMeta(Enum):
    """Metadata for value_of_transactions."""

    description = (
        "The value of the transactions processed in the payment system. Stated in SEK."
    )

    description_swe = "Värdet av de transaktioner som är processade i betalningssystemet. Anges i SEK."

    examples = None

    name = "Value"

    name_swe = "Värde"

    field = "value_of_transactions"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ConcentrationRatioTypeMeta(Enum):
    """Metadata for concentration_ratio_type."""

    description = "Concentration refers to the market share of the five largest senders of payment transactions within each system, including the central bank. Each participant with individual access to the system shall be counted separately, regardless of whether two or more participants are related or not. The attribute refers to whether it is a concentration degree for the value or number of transactions."

    description_swe = "Koncentrationsgrad avser marknadsandelen för de fem största avsändarna av betalningstransaktioner inom varje system inkl. centralbanken. Varje deltagare som har enskild åtkomst till systemet ska räknas separat, oberoende av om två eller flera deltagare är närstående eller ej. Attributet avser om det är en koncentrationsgrad för värdet eller antal transaktioner."

    examples = None

    name = "Concentration ratio type"

    name_swe = "Typ av koncentrationsgrad"

    field = "concentration_ratio_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ConcentrationRatioValueMeta(Enum):
    """Metadata for concentration_ratio_value."""

    description = "Refers to the value of the degree of concentration."

    description_swe = "Avser värdet av koncentrationgraden."

    examples = ["0.65"]

    name = "Concentration ratio value"

    name_swe = "Värdet av koncentrationsgraden"

    field = "concentration_ratio_value"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class NumberOfParticipantsMeta(Enum):
    """Metadata for number_of_participants."""

    description = (
        "The number of direct and indirect participants in the payment system."
    )

    description_swe = "Antal direkta och indirekta deltagare i betalningssystemet."

    examples = None

    name = "Number of participants"

    name_swe = "Antal"

    field = "number_of_participants"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ParticipantTypeMeta(Enum):
    """Metadata for participant_type."""

    description = (
        "Defines whether it is a direct or indirect participant in the payment system."
    )

    description_swe = (
        "Definierar om det är en direkt eller indirekt deltagare i betalningssystemet."
    )

    examples = None

    name = "Participant type"

    name_swe = "Typ av deltagare"

    field = "participant_type"

    mandatory = "Yes"

    mandatory_swe = "Ja"


class ParticipantSectorMeta(Enum):
    """Metadata for participant_sector."""

    description = "Institutional sector of the participant."

    description_swe = "Institutionell sektor för deltagaren."

    examples = None

    name = "Participant sector"

    name_swe = "Deltagarsektor"

    field = "participant_sector"

    mandatory = "Yes"

    mandatory_swe = "Ja"
