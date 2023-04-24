import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6140212472"))
    API_HASH = os.environ.get("API_HASH", "f330f029c9824382b9d6db41fcf1e56f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6250233176:AAGwA9v4FXsQ8fieShmTdQmkc448E2lkW1s)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOJ0BuxkrJGTtRsiHlyVGN3NrlPim4CszimEiPqI_m9BlTva2O7xSiqxdr9_bgQMAJ_rSRZP4Q4xHWCUV_jh3IDEwUciDWehC8-_ycvdIM6PWg1dEERcST2SgUsKtz2BZCJIzcHeVHkIPGQqWLy47IQvZJs4Ej0hDhdihVzggM7BTB604L_Yb-m4MuNCqas4Wshaj7mtEt-74JEkQLO7oL2ZcJ2D8WwkbBwIOf129IRR1JsCnTUB39wkGA0FGGttM1KzP1s7t6_16q9t8_wcVl2UPPnZfjRrq6mYmQjIG-QY-TkGzLKZhuPBiICM25sQc-7j8o56SrAZXTApz3VZgymlbOGU=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ZBR_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
