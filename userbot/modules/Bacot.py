from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.babu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EH LU TUH BABU GUA GOBLOK .**")
    sleep(2)
    await typew.edit("**JADI BABU HARUS NURUT SAMA MAJIKANNYA YA ANJING**")


@register(outgoing=True, pattern='^.stress(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**NI YE GUA KASIH TAU SAMA LU YA BEGO LU BAKAL PUNYA ANAK CUCU LU KASIH TAU AJA KETURUNAN LU TUH KALO UDAH HINA YA HINA BEGO.**")
    sleep(6)
    await typew.edit("**GUA SARANIN JUGA LU SURUH ANAK LU NYEKOLAHIN CUCU LU BESOK BIAR PINTER GA KEK LU DONGO GOBLOK IDIOT YEKAN.ANAK LU SURUH KERJA BIAR PUNYA DUIT BIAR BISA MAKAN JANGAN BERGANTUNG SAMA BANSOS MULU.NIH YA KALO KOSA KATA MASIH NYURI DARI ORANG LAINAPA LAGI COPY PASTE GAUSAH BELAGU KONTOL.MAKANYA OTAKNYA DIPAKE TOLOL JANGAN DITARO DI DENGKUL MULU.**")
    sleep(11)
    await typew.edit("**KEBANYAKAN COLI SIH MAKANYA JADI KOPONG TUH DENGKUL ISI OTAK LU AJA CUMA DEBU SAMA SARANG LABA LABA BEGO**")
    sleep(6)
    await typew.edit("**GA USAH SO MANTEP BEGO KALO LEHER MASIH BEDAKI SELANGKANGAN BEJAMUR KONTOL NANAHAN MAKANYA KALO MANDI PAKE AIR BUKAN PAKE PASIR.**")
    sleep(6)
    await typew.edit("**GUA JAGO GA KAYA LU YG SOSOAN JADI JAGOAN KOSA KATA CUMA 1-10 TERUS DIBALIKIN 10-1 SAMA KAYA HIDUP LU MUNDAR MANDIR SANA SINI CARI PINJEMAN BUAT MAKAN SEHARI HARI YEKAN**")
    sleep(6)
    await typew.edit("**MAU SAMPE KAPAN PUN GUA BAKALAN LADENIN LU GOBLOK, LADENIN MANUSIA PURBA JELEK KEK LU GABAKALAN BERENTI GUA TOLOL NI YE GUA SARANIN MENDING LU APUS TELE DAH KONTOL.**")


@register(outgoing=True, pattern='^.ngontol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**HEH LU KONTOL**")
    sleep(2)
    await typew.edit("**LU KENAPA SI NGONTOL BANGET ANJING!**")
    sleep(2)
    await typew.edit("**SUMPAH LU NGONTOL BANGET KONTOLLL!**")
    sleep(2)
    await typew.edit("**DASAR LU KONTOOOOLLLL!!!**")
    sleep(2)
    await typew.edit("**KONTOLLL**")
    sleep(2)
    await typew.edit("**KONTOOOOOLLLLL!!!!**")


@register(outgoing=True, pattern='^.gajelas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**YA AMPUN LU NGOMONG APA? GA NYAMBUNG KONTOL KAYA KEHIDUPAN LU MAKANYA ORG ORG KAYA LU GABAKALN MAJU HIDUPNYA APA LAGI ORG ORG BAWAHAN KAYA LU.**")


@register(outgoing=True, pattern='^.Bacot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**BANYAK BACOT LU NGENTOT**")

CMD_HELP.update({
    "Bacot":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ngontol`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stress`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gajelas`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.babu`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.Bacot`\
\n↳ : Coba Aja Sendiri."
})
