import random
from datetime import timedelta
from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv
from . import wenda
first = True

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
async def say_sorry(session):
    await session.send('ごめんなさい！〒︿〒')

@sv.on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=True)
async def chat_waifu(session):
    # if not sv.check_priv(session.ctx, Priv.SUPERUSER):
    #     await session.send(R.img('laopo.jpg').cqcode)
    await session.send('mua~')


@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('我不是！我没有！别瞎说啊！', at_sender=True)

@sv.on_command('mua', only_to_me=True)
async def chat_mua(session):
    await session.send('笨蛋~', at_sender=True)

@sv.on_command('晚安', only_to_me=True)
async def chat_goodnight(session):
    await session.send('晚安，骑士君~', at_sender=True)

@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=False)
async def ddhaole(session):
    await session.send('那个朋友是不是你弟弟？')
    # await util.silence(session.ctx, 30)

@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    # await util.silence(session.ctx, 30)
    
@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.5:
        await bot.send(ctx, '嗯嗯，没错')


@sv.on_message('group')
async def group_wenda(bot, ctx):
    msg_ask = ctx['message'].extract_plain_text()
    global first
    if first:
        wenda.readdir()
        print('\n词库启动，记忆装载完毕\n')
        first = False
    if '删除词条' in msg_ask:
        await bot.send(ctx, wenda.delet(msg_ask))
    elif msg_ast == '打印所有词条':
        await bot.send(ctx, wenda.keys())
    elif msg_ask == '重新读取记忆':
        await bot.send(ctx, wenda.readdir())
    elif '问' in msg_ask and '答' in msg_ask and '问答' not in msg_ask:
        await bot.send(ctx, wenda.add(msg_ask))
    elif (msg := wenda.reply(msg_ask)):
        await bot.send(ctx, msg)


