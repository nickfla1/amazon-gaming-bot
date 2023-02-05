import yaml

from bot.constants import CONFIG_FILE


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)
