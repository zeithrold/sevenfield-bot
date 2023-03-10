from nonebot import on_message, require
from nonebot.rule import Rule, to_me
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent


async def message_checker(event: GroupMessageEvent):
    return event.get_plaintext() == "ping"

rule = Rule(message_checker, to_me)

matcher = on_message(rule=rule)


@matcher.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    await bot.send_group_msg(group_id=event.group_id, message=f"[CQ:reply,id={event.message_id}]pong")
