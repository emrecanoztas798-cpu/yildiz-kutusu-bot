from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
import random

TOKEN = os.getenv("BOT_TOKEN")

# ⭐ Huzurlu mesajlar
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
    "ben burada, sadece okuyan ve yanında duran bir sessizlik gibiyim",
    "ve ne olursa olsun, burada yalnız değilsin"
]

# ⭐ Karşılama mesajı
WELCOME_TEXT = (
    "seni çok seviyorum sevgilim 🤍\n\n"
    "buraya içini dökebilirsin\n"
    "yıldızlarını saç ⭐"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(messages)

    await update.message.reply_text(
        f"⭐ yıldızın bırakıldı\n\n{msg}"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
