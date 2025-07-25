from AlgorithmImports import *

SECTOR_SYMBOLS = {
    "Grains": [
        Futures.Grains.CORN,
        Futures.Grains.SOYBEANS,
        Futures.Grains.SOYBEAN_OIL,
        Futures.Grains.SOYBEAN_MEAL,
        Futures.Grains.SRW_WHEAT,
        Futures.Grains.HRW_WHEAT,
    ],
    "Meats": [
        Futures.Meats.LIVE_CATTLE,
        Futures.Meats.LEAN_HOGS,
        Futures.Meats.FEEDER_CATTLE,
    ],
    "Currencies": [
        Futures.Currencies.MICRO_BTC,
        Futures.Currencies.MICRO_ETHER,
        Futures.Currencies.JPY,
        Futures.Currencies.EUR,
        Futures.Currencies.BRL,
        Futures.Currencies.GBP,
        Futures.Currencies.AUD,
        Futures.Currencies.CAD,
        Futures.Currencies.MXN,
        Futures.Currencies.NZD,
        Futures.Currencies.CHF,
    ],
    "Energies": [
        Futures.Energies.CRUDE_OIL_WTI,
        Futures.Energies.NATURAL_GAS,
        Futures.Energies.BRENT_LAST_DAY_FINANCIAL,
        Futures.Energies.HEATING_OIL,
        Futures.Energies.GASOLINE,
    ],
    "Indices": [
        Futures.Indices.SP_500_E_MINI,
        Futures.Indices.NASDAQ_100_E_MINI,
        Futures.Indices.RUSSELL_2000_E_MINI,
        Futures.Indices.DOW_30_E_MINI,
        Futures.Indices.NIKKEI_225_YEN_CME,
    ],
    "Financials": [
        Futures.Financials.Y_2_TREASURY_NOTE,
        Futures.Financials.Y_5_TREASURY_NOTE,
        Futures.Financials.Y_10_TREASURY_NOTE,
        Futures.Financials.ULTRA_TEN_YEAR_US_TREASURY_NOTE,
        Futures.Financials.Y_30_TREASURY_BOND,
        Futures.Financials.ULTRA_US_TREASURY_BOND,
        Futures.Financials.EURO_DOLLAR,
    ],
}

SYMBOL_TO_SECTOR = {
    symbol: sector for sector, symbols in SECTOR_SYMBOLS.items() for symbol in symbols
}


def future_symbols() -> list[Symbol]:
    # 37 symbols
    return [
        # Grains 6 symbols
        Symbol.create(Futures.Grains.CORN, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(Futures.Grains.SOYBEANS, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(Futures.Grains.SOYBEAN_OIL, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(Futures.Grains.SOYBEAN_MEAL, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(Futures.Grains.SRW_WHEAT, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(Futures.Grains.HRW_WHEAT, SecurityType.FUTURE, Market.CBOT),
        # Meats 3 symbols
        Symbol.create(Futures.Meats.LIVE_CATTLE, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Meats.LEAN_HOGS, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Meats.FEEDER_CATTLE, SecurityType.FUTURE, Market.CME),
        # Currencies 11 symbols
        Symbol.create(Futures.Currencies.MICRO_BTC, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.MICRO_ETHER, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.JPY, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.EUR, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.BRL, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.GBP, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.AUD, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.CAD, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.MXN, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.NZD, SecurityType.FUTURE, Market.CME),
        Symbol.create(Futures.Currencies.CHF, SecurityType.FUTURE, Market.CME),
        # Energies 5 symbols
        Symbol.create(
            Futures.Energies.CRUDE_OIL_WTI, SecurityType.FUTURE, Market.NYMEX
        ),
        Symbol.create(Futures.Energies.NATURAL_GAS, SecurityType.FUTURE, Market.NYMEX),
        Symbol.create(
            Futures.Energies.BRENT_LAST_DAY_FINANCIAL, SecurityType.FUTURE, Market.NYMEX
        ),
        Symbol.create(Futures.Energies.HEATING_OIL, SecurityType.FUTURE, Market.NYMEX),
        Symbol.create(Futures.Energies.GASOLINE, SecurityType.FUTURE, Market.NYMEX),
        # Indices 5 symbols
        Symbol.create(Futures.Indices.SP_500_E_MINI, SecurityType.FUTURE, Market.CME),
        Symbol.create(
            Futures.Indices.NASDAQ_100_E_MINI, SecurityType.FUTURE, Market.CME
        ),
        Symbol.create(
            Futures.Indices.RUSSELL_2000_E_MINI, SecurityType.FUTURE, Market.CME
        ),
        Symbol.create(Futures.Indices.DOW_30_E_MINI, SecurityType.FUTURE, Market.CBOT),
        Symbol.create(
            Futures.Indices.NIKKEI_225_YEN_CME, SecurityType.FUTURE, Market.CME
        ),
        # Financials 7 symbols
        Symbol.create(
            Futures.Financials.Y_2_TREASURY_NOTE, SecurityType.FUTURE, Market.CBOT
        ),
        Symbol.create(
            Futures.Financials.Y_5_TREASURY_NOTE, SecurityType.FUTURE, Market.CBOT
        ),
        Symbol.create(
            Futures.Financials.Y_10_TREASURY_NOTE, SecurityType.FUTURE, Market.CBOT
        ),
        Symbol.create(
            Futures.Financials.ULTRA_TEN_YEAR_US_TREASURY_NOTE,
            SecurityType.FUTURE,
            Market.CBOT,
        ),
        Symbol.create(
            Futures.Financials.Y_30_TREASURY_BOND, SecurityType.FUTURE, Market.CBOT
        ),
        Symbol.create(
            Futures.Financials.ULTRA_US_TREASURY_BOND, SecurityType.FUTURE, Market.CBOT
        ),
        Symbol.create(Futures.Financials.EURO_DOLLAR, SecurityType.FUTURE, Market.CME),
    ]


def get_sector(symbol: Symbol) -> str:
    return SYMBOL_TO_SECTOR.get(symbol.id.symbol, "Unknown")
