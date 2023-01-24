from vkbottle import Bot, Message 

from vkbottle import Keyboard, KeyboardButtonColor, Text

bp = Bot('vk1.a.zpd_3zF1mV2ppzCW_JhLcTVKadIY8h9Ksi-AfsbP3XCxkGvZqF3c6nfL_bRW9Tzdprqd22d9vlwah73X1Dp9N3Y7KpwFWSCAAmhKb6LjeQLHHSWXHhjpi0WEnV0nN5s4FwnNYjlieM-pTQ4vxdCacpUVb3_Y2cSSTekjlM234f9jDnHDuXPT1Xv85pHiiXVv9c2e25qfbwQBMe6B3BCVMA') 

@bp.on.private_message()

async def hello(m: Message):

   kb: dict = Keyboard(inline=True).add(Text("porno"))

   await m.reply(m.text, keyboard=kb)

bot.run_forever()
