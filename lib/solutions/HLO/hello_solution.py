

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    assert friend_name is not None
    return f"Hello, {friend_name}!"
