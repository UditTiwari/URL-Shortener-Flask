
import random
import string


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    print(short_url)
    return short_url

generate_short_url()