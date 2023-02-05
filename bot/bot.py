from bot.api import get_games, get_user_info
from bot.config import load_config
from bot.csrf import get_csrf


def run():
    # Load configuration
    config = load_config()

    # First get the page HTML
    csrf_token = get_csrf()
    print(f"CSRF: {csrf_token}")

    # Retrieve and validate user info
    user = get_user_info(config, csrf_token)
    user_id = user["id"]
    print(f"User ID: {user_id}")

    # Retrieve all available games
    games = get_games(config, csrf_token)
    print(f"Available games: {len(games)}")
