import asyncio
from telegraph.aio import Telegraph


async def create_news_post(title, body):
    telegraph = Telegraph()
    # print(await telegraph.create_account(short_name='1337'))
    await telegraph.create_account(short_name='1337')
    # await asyncio.sleep(0.5)
    context = f"{body}" if title is None else f"{title} <br> {body}"
    response = await telegraph.create_page(
        "NEWS",
        html_content=f"{title}<br>{body}"
    )
    print(response['url'])
    return response


