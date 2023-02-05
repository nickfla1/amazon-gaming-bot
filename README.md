# Amazon Gaming Telegram bot

> Work in progress.

## Notes

### API format

Protocol: GraphQL
Endpoint: https://gaming.amazon.com/graphql

All requests have a query parameter called `nonce`, being an uuid v4.

### CSRF token

CSRF token is found as the value of the element with name `csrf-key`, must be included in each GraphQL request.

Header: `csrf-token`

### Authentication

Cookies maybe?