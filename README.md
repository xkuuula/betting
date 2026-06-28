# Polymarket CS2 Large Bet Alerts

Realtime Python service that watches Polymarket trade streams for Counter-Strike 2 markets and sends Telegram alerts for large USD-notional bets.

## Why this data path

Polymarket exposes two useful realtime surfaces:

- RTDS WebSocket `wss://ws-live-data.polymarket.com`, topic `activity`, type `trades`. This is the best public enriched stream because it includes trade size, price, market slug/title, outcome, proxy wallet, timestamp, and transaction hash.
- CLOB market WebSocket `wss://ws-subscriptions-clob.polymarket.com/ws/market`, event `last_trade_price`. This is closest to the matching engine for known token IDs, but it is lower-level and does not include all enriched user/market metadata.

The service uses RTDS as the primary source for all new trades and optionally keeps a CLOB subscription for discovered CS2 token IDs. RTDS is enough to identify and alert full enriched large bets; the CLOB channel provides an earlier low-level signal for active markets discovered through Gamma API.

## Quick Start

Install [uv](https://docs.astral.sh/uv/) first, then run:

```powershell
uv sync
Copy-Item .env.example .env
# edit .env with Telegram token/chat id
uv run polymarket-cs2-alerts
```

On Windows you can also edit `.env` and run `run_bot.bat`.

## Development

```powershell
uv sync --dev
uv run pytest -q
uv run ruff check .
```

## Configuration

All settings are read from `.env`.

- `TELEGRAM_BOT_TOKEN`: Telegram bot token.
- `TELEGRAM_CHAT_ID`: target chat/channel id.
- `MINIMUM_BET_SIZE_USD`: alert threshold, default `5000`.
- `MAX_TRADE_PRICE`: only alert trades with price below this value, default `0.5`.
- `DATA_API_URL`: Polymarket Data API used to check whether `proxyWallet` has earlier trades on Polymarket.
- `ALLOWED_TOURNAMENTS`: optional comma-separated tournament names or substrings.
- `EXCLUDED_TOURNAMENTS`: optional comma-separated tournament names or substrings.
- `ENABLE_CLOB_MARKET_WS`: enable/disable the low-level CLOB listener.
- `DISCOVERY_INTERVAL_SECONDS`: active-market rediscovery interval.

## Notes

Polymarket CS2/esports metadata is not guaranteed to expose a normalized tournament tier. The classifier still displays a best-effort Tier 1/2/3/Unknown label, but tier no longer blocks alerts. Use `ALLOWED_TOURNAMENTS` and `EXCLUDED_TOURNAMENTS` in `.env` when you want to narrow the watched matches.

Never commit `.env` with real Telegram credentials.
