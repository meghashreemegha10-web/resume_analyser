import hashlib
import json
import os
from typing import Optional

USERS_FILE = "data/users.json"


def _load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def _save_users(users: dict) -> None:
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username: str, password: str) -> tuple[bool, str]:
    """Register a new user. Returns (success, message)."""
    username = username.strip().lower()
    if not username or not password:
        return False, "Username and password are required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    users = _load_users()
    if username in users:
        return False, "Username already exists. Please choose another."
    users[username] = {
        "password_hash": _hash_password(password),
        "display_name": username.capitalize()
    }
    _save_users(users)
    return True, "Account created successfully! Please log in."


def verify_user(username: str, password: str) -> tuple[bool, Optional[str]]:
    """Verify credentials. Returns (success, display_name or None)."""
    username = username.strip().lower()
    users = _load_users()
    user = users.get(username)
    if not user:
        return False, None
    if user["password_hash"] == _hash_password(password):
        return True, user.get("display_name", username.capitalize())
    return False, None
