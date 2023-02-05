# Amazon Gaming Telegram bot

Usage of this software is to be intended to personal and educational uses only.

## Notes

### API format

- **Protocol**: GraphQL
- **Endpoint**: https://gaming.amazon.com/graphql

All requests have a query parameter called `nonce`.

### CSRF token

CSRF token is found as the value of the element with name `csrf-key`, must be included in each GraphQL request.

Header: `csrf-token`

### Authentication

Cookies `session-id`, `session-token` and `x-main` are required.
