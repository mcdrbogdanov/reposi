from vkbottle import Bot, Message

from vkbottle.api.keyboard import Keyboard, Text

from vkbottle.branch import Branch, ExitBranch

bot=Bot('vk1.a.zpd_3zF1mV2ppzCW_JhLcTVKadIY8h9Ksi-AfsbP3XCxkGvZqF3c6nfL_bRW9Tzdprqd22d9vlwah73X1Dp9N3Y7KpwFWSCAAmhKb6LjeQLHHSWXHhjpi0WEnV0nN5s4FwnNYjlieM-pTQ4vxdCacpUVb3_Y2cSSTekjlM234f9jDnHDuXPT1Xv85pHiiXVv9c2e25qfbwQBMe6B3BCVMA')

dialogs = {}

wait = []

emoji = ':)' # Спасибо моему IDLE :)

start_keyboard = Keyboard(one_time=False)

start_keyboard.add_row()

start_keyboard.add_button(Text(label="Поиск собеседника"), color="negative")

wait_keyboard = Keyboard(one_time=True)

wait_keyboard.add_row()

wait_keyboard.add_button(Text(label="Отменить поиск"), color="positive")

stop_keyboard = Keyboard(one_time=False)

stop_keyboard.add_row()

stop_keyboard.add_button(Text(label="Отключиться от диалога"), color="primary")

@bot.on.message(text='Поиск собеседника', lower = True)

async def start(ans: Message):

    if ans.from_id not in wait and ans.from_id not in dialogs:

        if len(wait) == 0:

            await ans(f'{emoji} Вы добавлены в очередь поиска собеседника.', keyboard=wait_keyboard)

            wait.append(ans.from_id)

            await bot.branch.add(ans.peer_id, "wait")

        else:

            dialogs[ans.from_id] = wait[0]

            dialogs[wait[0]] = ans.from_id

            await bot.api.messages.send(peer_id=ans.from_id, random_id=0, message=f'{emoji} Мы нашли вам собеседника!', keyboard=stop_keyboard)

            await bot.api.messages.send(peer_id=wait[0], random_id=0, message=f'{emoji} Мы нашли вам собеседника!', keyboard=stop_keyboard)

            await bot.branch.add(ans.from_id, "dialog")

            await bot.branch.add(wait[0], "dialog")

            del wait[0]

@bot.branch.simple_branch("wait")

async def branch(ans: Message):

    if ans.text == "Отменить поиск":

        await ans(f"{emoji} Поиск собеседника остановлен.", keyboard=start_keyboard)

        await bot.branch.exit(ans.peer_id)

        del wait[0]

    else:

        await ans(f'{emoji} Вы находитесь в поиске собеседника.', keyboard=wait_keyboard)

@bot.branch.simple_branch("dialog")

async def branch(ans: Message):

    if ans.text == "Отключиться от диалога":

        await bot.api.messages.send(peer_id=ans.from_id, random_id=0, message=f'{emoji} Диалог был остановлен.', keyboard=start_keyboard)

        await bot.api.messages.send(peer_id=dialogs[ans.from_id], random_id=0, message=f'{emoji} Собеседник остановил диалог.', keyboard=start_keyboard)

        await bot.branch.exit(dialogs[ans.from_id])

        await bot.branch.exit(ans.from_id)

        del dialogs[dialogs[ans.from_id]]

        del dialogs[ans.from_id]

    else:

        await bot.api.messages.send(peer_id=dialogs[ans.from_id], random_id=0, message='Собеседник: ' + ans.text)

@bot.on.message()

async def all(ans: Message):

    await ans('Привет! Я анонимный чат-бот. Чтобы начать поиск собеседника, воспользуйтесь кнопками.', keyboard=start_keyboard)

bot.run_polling()
