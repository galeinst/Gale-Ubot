from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb.`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb.`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumssalam wr. wb.`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumssalam wr. wb.`")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAHAHA WAGYU**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("MENGONTOL BANGET KAMU")


@register(outgoing=True, pattern='^.pamer(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GOSAH PAMER BOT MULU KONTOL, KEK BARU MAEN BOT AJA ANJG**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ORANG SUSAH KAYA ELU GAPANTES IDUP BEGO , LU IDUP CUMA NYUSAHIN ORANG DOANG NGENTOT**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BANYAK BACOT BABI SATU INI**")

CMD_HELP.update({
    "salam":
    "πΎπ€π’π’ππ£π: `.P` | `.p`\
\nβ³ : Untuk Memberi salam.\
\n\nπΎπ€π’π’ππ£π: `.L` `.l`\
\nβ³ : Untuk Menjawab Salam.\
\n\nπΎπ€π’π’ππ£π: `B`\
\nβ³ : Liat aja sendiri Tot.\
\n\nπΎπ€π’π’ππ£π: `.pamer`\
\nβ³ : Buat Yang Suka Pamer Bot.\
\n\nπΎπ€π’π’ππ£π: `O` | `M` | `Y`\
\nβ³ : Awas Galak."
})
