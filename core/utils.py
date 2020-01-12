from django.utils.text import slugify

from .constants import SLUG_MAX_LENGTH


def generate_slug(name: str, pk: int) -> str:
    slug = f"{name}-{pk}"
    slug_prototype = slugify(slug)
    if len(slug_prototype) >= SLUG_MAX_LENGTH:
        slug = slug_prototype[0:SLUG_MAX_LENGTH]
    else:
        slug = slug_prototype
    return slug
