

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    assert friend_name and len(friend_name) != 0
    return f"Hello, {friend_name}!"
