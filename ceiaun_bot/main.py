import logging
import os.path

from telegram import InputMediaDocument, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

import settings
from messages import keyboards, messages
from utils import create_new_sheet

logger = logging.getLogger(__name__)

# States
HOME, REQUEST_COURSE, GET_CHARTS, CONVERT_COURSE = map(chr, range(4))
END = ConversationHandler.END


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(
        quote=True,
        document=settings.FILE_HOME_IMAGE,
        reply_markup=keyboards.HOME_KEYBOARD,
        caption=messages.START_COMMAND,
    )

    return HOME


async def back_home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(
        quote=True,
        document=settings.FILE_HOME_IMAGE,
        reply_markup=keyboards.HOME_KEYBOARD,
        caption=messages.HOME_SHORT,
    )

    return HOME


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    users_id = update.message.from_user.username

    # sending courses_list (done)
    if text == keyboards.HOME_CHART:
        # Send orient help
        await update.message.reply_text(
            quote=True,
            text=messages.CHART_SELECT_ORIENT,
            parse_mode=ParseMode.HTML
        )

        # Send se chart
        await context.bot.send_media_group(
            chat_id=update.effective_chat.id,
            media=[
                InputMediaDocument(settings.FILE_SE_CHARTS[0]),
                InputMediaDocument(
                    settings.FILE_SE_CHARTS[1],
                    caption=messages.CHART_SE_CAPTION,
                    parse_mode=ParseMode.HTML
                )
            ],
        )
        # Send it charts
        await context.bot.send_media_group(
            chat_id=update.effective_chat.id,
            media=[
                InputMediaDocument(settings.FILE_IT_CHARTS[0]),
                InputMediaDocument(
                    settings.FILE_IT_CHARTS[1],
                    caption=messages.CHART_IT_CAPTION,
                    parse_mode=ParseMode.HTML
                )
            ],
        )

        # Send home message
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=messages.HOME_SHORT,
            reply_markup=keyboards.HOME_KEYBOARD
        )

        return None

    # converting courses name (unfinished)
    if text == keyboards.HOME_CONVERT_NAME:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document="BQACAgQAAx0Edz5chAADCmW3440_ebd_3XPYwfxkoCpz8TYnAAIQEAACi4zBUfXtf4Z0LyMsNAQ",
            caption=messages.CONVERT_NAME_COMMAND,
            reply_markup=keyboards.BACK_KEYBOARD,
        )

        return CONVERT_COURSE

    # students requests (unfinished)
    if "درخواست افزایش ظرفیت" in text:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document='BQACAgQAAx0Edz5chAADB2W34uUd86Q7EG8SNB8-jRtiPMZsAAINEAACi4zBURJXGMOkPaRENAQ',
            caption=messages.REQUEST_COMMAND,
        )

    # باید با استیت هندل بشه ############################

    # user_text = text.split("+")
    # if len(user_text) != 4:
    #     return messages.INCORRECT_LENGTH

    # student_name = user_text[0].strip()
    # student_id = str(unidecode(user_text[1].strip()))
    # student_course = user_text[2].strip()
    # student_course_id = str(unidecode(user_text[3].strip()))

    # if student_name.isnumeric():
    #     return messages.INCORRECT_USERNAME

    # if (not student_id.isnumeric()) or (len(student_id) not in [8, 11, 14]):
    #     return messages.INCORRECT_STUDENT_ID

    # if student_course.isnumeric():
    #     return messages.INCORRECT_COURSE

    # if not student_course_id.isnumeric():
    #     return messages.INCORRECT_COURSE_ID

    # #adding data to excel file
    # write_data_to_sheet(
    #     settings.EXCEL_TEMP_FILE,
    #     [student_name, student_id, student_course, student_course_id],
    #     ["A", "B", "C", "D"],
    #     start_row_number=3)

    # return messages.RECEIVED_REQUEST
    ###

    logger.info(f"user id is = {users_id}")
    logger.info(f" user{update.message.chat.id} in {message_type}: {text}")


async def handle_convert_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    REPLACE = (
        (" ", "%"),
        ("ی", "%"),
        ("ک", "%"),
        ("ي", "%"),
        ("ك", "%"),
    )

    text = update.message.text

    converted_name = text
    for r in REPLACE:
        converted_name = converted_name.replace(*r)

    result = ""
    for name in converted_name.split("\n"):
        result += f"<code>%{name}%</code>\n"

    await update.message.reply_text(
        text=messages.CONVERT_NAME_RESULT.format(result=result),
        parse_mode=ParseMode.HTML,
        quote=True,
        reply_markup=keyboards.BACK_KEYBOARD
    )


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f"Error for update {update} caused error {context.error}")


if __name__ == "__main__":
    if not os.path.exists(settings.EXCEL_TEMP_FILE):
        create_new_sheet("temp")

    app = Application.builder().token(settings.BOT_TOKEN).build()

    all_keyboards = (
        f"^({keyboards.HOME_COURSE_REQUEST}|{keyboards.HOME_CONVERT_NAME}|{keyboards.HOME_CHART}|"
        f"{keyboards.BACK})$"
    )
    main_conv = ConversationHandler(
        entry_points=[
            CommandHandler("start", start_command),
            MessageHandler(
                filters.TEXT & filters.Regex(all_keyboards),
                start_command
            )
        ],
        states={
            HOME: [MessageHandler(filters.TEXT, handle_messages)],
            # REQUEST_COURSE: [MessageHandler(filters.TEXT, handle_request_course)],
            CONVERT_COURSE: [
                MessageHandler(filters.TEXT & ~filters.Regex(f"^{keyboards.BACK}$"), handle_convert_course)
            ],
        },
        fallbacks=[
            MessageHandler(filters.TEXT, start_command),
        ],
    )

    app.add_handlers([
        main_conv,
    ])

    # Errors
    app.add_error_handler(error)

    app.run_polling()
