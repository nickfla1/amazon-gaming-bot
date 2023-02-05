from bot.api import get_games
from bot.config import load_config
from bot.csrf import get_csrf


def run():
    # Load configuration
    config = load_config()

    # First get the page HTML
    csrf_token = get_csrf()
    print(f"CSRF: {csrf_token}")

    # Retrieve all available games
    games = get_games(config, csrf_token)
    print(f"Available games: {len(games)}")
