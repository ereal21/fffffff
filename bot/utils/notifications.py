import os
from aiogram import Bot

from bot.misc import EnvKeys


async def notify_owner_of_purchase(
    bot: Bot,
    username: str,
    formatted_time: str,
    item_name: str,
    item_price: float,
    parent_cat: str | None,
    category_name: str,
    description: str,
    file_path: str | None,
) -> None:
    """Send purchase details to the bot owner.

    If ``file_path`` is provided and points to an existing file, the file is sent
    as a photo/video with the details in the caption. Otherwise a text message is
    sent.
    """
    text = (
        f"User {username}\n"
        f"Time: {formatted_time} GMT+3\n"
        f"Product: {item_name} ({item_price}€)\n"
        f"Crypto: N/A\n"
        f"Category: {parent_cat or '-'} / {category_name}\n"
        f"Description: {description or '-'}"
    )

    if file_path and os.path.isfile(file_path):
        with open(file_path, "rb") as media:
            if file_path.endswith(".mp4"):
                await bot.send_video(EnvKeys.OWNER_ID, media, caption=text)
            else:
                await bot.send_photo(EnvKeys.OWNER_ID, media, caption=text)
    else:
        await bot.send_message(EnvKeys.OWNER_ID, text)
