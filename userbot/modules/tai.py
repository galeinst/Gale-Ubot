from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.yesus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**ANDA TAU SEBERAPA BAIKNYA YESUS?**")
    sleep(2)
    await typew.edit("**YESUS TERAMAT TULUS SAMPAI JADI TUKANG PIJIT PLUS PLUS YANG MELAYANI UMATNYA.**")



CMD_HELP.update({
    "nyindir1":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.yesus`\
\n↳ : Coba Aja Sendiri."
})
