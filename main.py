
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
import random

TOKEN = os.getenv("BOT_TOKEN")

messages = [
    "burada yazdığın her şey, aceleye getirilmeyen bir sessizlikte saklanıyor, sanki dünya biraz yavaşlamış gibi",
    "bazen insan sadece anlatmak ister, çözülmesini değil, duyulmasını bekler",
    "burada söylediklerin hiçbir yere gitmiyor, sadece olduğu gibi kalıyor ve bu bile yeterli olabilir",
    "ne hissedersen hisset, burada ona yer var, sıkışmadan, taşmadan",
    "bu alan seni düzeltmeye çalışmaz, sadece yanında durur",
    "bazen bir duygunun anlam kazanması gerekmez, sadece hissedilmesi yeterlidir",
    "burada zaman biraz daha yumuşak akar, hiçbir şey seni aceleye zorlamaz",
    "içinden geçenleri toparlaman gerekmez, dağınık haliyle de kabul ediliyor",
    "bazı şeyler anlatıldıkça hafifler, burada o hafifliğe izin var",
    "ve ne olursa olsun, burada yalnız değilsin"
]

WELCOME_TEXT = (
    "seni çok seviyorum sevgilim 🤍\n\n"
    "buraya içini dökebilirsin\n"
    "yıldızlarını saç ⭐"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # 🤍 teşekkür / sağ ol cevabı
    if any(word in text for word in [
        "teşekkür ederim",
        "tesekkür ederim",
        "sag ol",
        "sağ ol",
        "sagol",
        "sağol"
    ]):
        await update.message.reply_text(
            "bunu tek başına taşımak zorunda olmadığın için ben teşekkür ederim\n\n"
            "bazen bir duyguyu çözmekten önce ona yer açmak gerekir"
        )
        return

    # ❤️‍🔥 aşk cevabı
    if "aşk ne demek" in text or "ask ne demek" in text:
        await update.message.reply_text(
            "aşkkktannnn yanmakkk ne demekkk ❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥"
        )
        return

    msg = random.choice(messages)

    await update.message.reply_text(
        f"⭐ yıldızın bırakıldı\n\n{msg}"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
