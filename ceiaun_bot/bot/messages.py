# Home
START_COMMAND = """به ربات دانشکده کامپیوتر خوش آمدید🌹

🔻لطفا قبل از استفاده از قابلیت‌های ربات، فایل راهنمای استفاده از آن (تصویر بالا) را مطالعه نمایید."""

HOME_SHORT = "به صفحه اصلی بازگشتید 👇"

# Request course
REQ_COMMAND = """اگر در زمان انتخاب واحد موفق به اخذ درسی نشدید، لطفا درخواست خود را به فرمت گفته شده مانند تصویر بالا ارسال کنید. (در صورتی که ترم آخر هستید به صورت خصوصی به آیدی @mob_gh پیام دهید)

<b>نام و نام خانوادگی + شماره دانشجویی + نام درس + کد ارائه</b>

نکات مهم:
🔹صرفا برای دروسی درخواست ارسال کنید که در زمان ثبت نام، <u>تمامی گروه‌های دیگر آن نیز تکمیل شده باشند</u> و ارائه دهنده آن، گروه کارشناسی مهندسی کامپیوتر باشد. (<b>دروس عمومی و پایه مانند ریاضی و فیزیک ارتباطی به گروه کارشناسی مهندسی کامپیوتر ندارد</b>)

🔹پس از ارسال درخواست، بررسی ظرفیت درس مورد نظر و اخذ آن بر عهده دانشجو است. لطفا در مورد زمان افزایش ظرفیت سوال نفرمایید."""

REQ_ERROR_LENGTH = """❌ لطفا درخواست خود را طبق فرمت گفته شده مجدد ارسال کنید.


<b>نام و نام خانوادگی + شماره دانشجویی + نام درس + کد ارائه
</b>

<tg-spoiler>نمونه: نیما کیانی + 39915042054099 + ساختمان داده + 2323185</tg-spoiler>"""

# Student name
REQ_ERROR_USERNAME = "❗️ لطفا نام و نام خانوادگی خود را به درستی وارد کنید و درخواست خود را مجدد ارسال نمایید "
REQ_ERROR_USERNAME_NONE = "❗️لطفا قسمت نام و نام خانوادگی خود را تکمیل کرده و درخواست خود را مجدد ارسال نمایید"

# Student id
REQ_ERROR_STUDENT_ID = "❗️ لطفا شماره دانشجویی خود را به درستی وارد کنید و درخواست خود را مجدد ارسال نمایید "
REQ_ERROR_STUDENT_ID_CODE_MELLI = "❗️ لطفا شماره دانشجویی خود را وارد کنید و درخواست خود را مجدد ارسال نمایید. کد ملی مورد قبول نمی‌باشد."
REQ_ERROR_STUDENT_ID_NONE = "❗️لطفا قسمت شماره دانشجویی خود تکمیل کرده و درخواست خود را مجدد ارسال نمایید."

# Course name
REQ_ERROR_COURSE = "❗️ لطفا نام درس را به درستی وارد کنید و درخواست خود را مجدد ارسال نمایید "
REQ_ERROR_COURSE_NONE = "❗️لطفا قسمت نام درس را تکمیل کرده و درخواست خود را مجدد ارسال نمایید"
REQ_ERROR_COURSE_DEPARTMENT = """❗️لطفا تنها درخواست خود را برای دروس تخصصی کامپیوتر ارسال کنید.

🔹دروس فیزیک : دکتر دائی
🔹دروس ریاضی : دکتر جعفری (مدیر گروه ریاضی)
🔹دروس معارف : دکتر شریعتی و برای درس انس با قرآن، خانم حاج امینی
🔹دروس ادبیات، زبان، تاریخ تمدن : خانم لسانی
🔹دروس تربیت بدنی و ورزش : دکتر افتخاری

<a href='https://t.me/ceiaun/1011'>دفترچه تلفن دانشگاه</a>"""

# Course id
REQ_ERROR_COURSE_ID = "❗️ لطفا کد ارائه درس را به درستی وارد کنید و درخواست خود را مجدد ارسال نمایید "
REQ_ERROR_COURSE_ID_NONE = "❗️لطفا قسمت کد ارائه درس را تکمیل کرده و درخواست خود را مجدد ارسال نمایید"
REQ_ERROR_COURSE_ID_INSTEAD = """❗️لطفا کد ارائه درس را به درستی وارد کنید و درخواست خود را مجدد ارسال نمایید.

💡کد درس با کد ارائه درس متفاوت است، لطفا کد ارائه درس را ارسال نمایید."""

REQ_RECEIVED_REQ = """درخواست شما دریافت شد ✅

📌پس از ارسال درخواست خود، بررسی ظرفیت درس مورد نظر و اخذ آن بر عهده دانشجو است. لطفا در مورد زمان افزایش ظرفیت سوال نفرمایید.

🔻درخواست بعدی خود را ارسال نمایید در غیر این صورت از گزینه «برگشت 🔙» استفاده کنید:"""

# Convert name
CONVERT_NAME_COMMAND = """🔻جهت تبدیل نام دروس کافیست نام درس مورد نظر خود را وارد کنید. (نمونه در تصویر بالا)"""
CONVERT_NAME_RESULT = """نام درس با موفقیت تبدیل شد ✅

نام درس تغییر یافته :
{result}

در صورتی که قصد تغییر نام درس دیگری رو دارید، نام درس مورد نظر خود را وارد کنید در غیر این صورت از گزینه «برگشت 🔙» استفاده کنید."""

# Chart
CHART_SELECT_ORIENT = """💠 نحوه تعیین #گرایش رشته مهندسی کامپیوتر

🔹گرایش دانشجویان ورودی 95 به بعد در زمان ثبت نام مشخص نمی‌باشد، لذا تعیین گرایش دانشجو با توجه به اولین درس تخصصی انجام خواهد شد. در صورت عدم رعایت این مورد، دانشجو در زمان فارغ التحصیلی با مشکل مواجه خواهد شد.

🔹دو #گرایش نرم افزار و فناوری اطلاعات در 7 درس سه واحدی تفاوت دارند که این دروس را از فایل لیست دروس گرایش مورد نظر قابل مشاهده می‌باشد. (جدول دروس تخصصی)

📌 تاکید می‌گردد که اخذ درس سه واحدی از گرایش مخالف به عنوان واحد #اختیاری، تنها پس از مشخص شدن گرایش دانشجو و اخذ اولین درس تخصصی از آن گرایش امکان پذیر خواهد بود.

<a href="https://t.me/ceiaun">کانال دانشجویان مقطع کارشناسی کامپیوتر</a>
@ceiaun"""

CHART_SE_CAPTION = """📌 لیست دروس و چارت پیشنهادی رشته مهندسی کامیپوتر - گرایش نرم افزار

پیش نیاز دروس از هر دو فایل بررسی شود.

<a href="https://t.me/ceiaun">کانال دانشجویان مقطع کارشناسی کامپیوتر</a>
@ceiaun"""

CHART_IT_CAPTION = """📌 لیست دروس و #چارت پیشنهادی رشته مهندسی کامیپوتر - #گرایش فناوری اطلاعات (IT)

پیش نیاز دروس از هر دو فایل بررسی شود.

<a href="https://t.me/ceiaun">کانال دانشجویان مقطع کارشناسی کامپیوتر</a>
@ceiaun"""

# Admin
ADMIN_HOME = "پنل ادمین:"
ADMIN_STAT = """تعداد درخواست ها: {request_count}
تعداد کاربران: {users_count}"""
ADMIN_GET_FILE_TITLE = "عنوان فایل را ارسال کنید:"
ADMIN_GET_FILE_NONE = "هیچ درخواستی وجود ندارد!"
ADMIN_GET_FILE_ID = "فایل را ارسال کنید:"
ADMIN_CLEAN_REQ_LIST = "عنوان فایل نهایی را وارد کنید:"
