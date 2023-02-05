from uuid import uuid4
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from bot.constants import GRAPHQL_ENDPOINT


def get_games(config, csrf_token):
    cookies = _get_cookies(config)

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "CarboniteApp",
        "csrf-token": csrf_token,
    }

    transport = AIOHTTPTransport(
        url=GRAPHQL_ENDPOINT, cookies=cookies, headers=headers)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query OffersContext_Offers_And_Items_And_FeaturedContent(
  $dateOverride: Time
  $pageSize: Int
) {
  games: items(
    collectionType: FREE_GAMES
    dateOverride: $dateOverride
    pageSize: $pageSize
  ) {
    items {
      ...Item
      __typename
    }
    __typename
  }
}

fragment Item on Item {
  id
  isFGWP
  isRetailLinkItem
  grantsCode
  priority
  assets {
    title
    externalClaimLink
    platforms
    cardMedia {
      defaultMedia {
        src1x
        src2x
        type
        __typename
      }
      __typename
    }
    externalClaimLink
    __typename
  }
  journey {
    id
    offers {
      ...LinkedJourneyOffer
      __typename
    }
    __typename
  }
  offers {
    id
    startTime
    endTime
    offerSelfConnection {
      eligibility {
        offerState
        isClaimed
        conflictingClaimAccount {
          obfuscatedEmail
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
  game {
    assets {
      title
      __typename
    }
    __typename
  }
  __typename
}

fragment LinkedJourneyOffer on JourneyOffer {
  catalogId
  grantsCode
  self {
    eligibility(getOnlyActiveOffers: true) {
      canClaim
      isClaimed
      conflictingClaimAccount {
        ...ConflictingClaimAccount
        __typename
      }
      __typename
    }
    __typename
  }
  __typename
}

fragment ConflictingClaimAccount on ConflictingClaimUser {
  fullName
  obfuscatedEmail
  __typename
}
        """
    )

    res = client.execute(query, variable_values={
        "pageSize": 100}, parse_result=True)
    return res["games"]["items"]


def _get_cookies(config):
    return {
        "x-main": config["auth"]["mainToken"],
        "session-id": config["auth"]["sessionId"],
        "session-token": config["auth"]["sessionToken"],
    }
