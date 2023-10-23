import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23539681"))
    API_HASH = os.environ.get("API_HASH", "ae1430184ae21aa81b4b030d1bd75885")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6548483719:AAFCxCqSDGI_VE1KEjrzwB605uCfm3MAAcE")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5007135395")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kktbots:A1B2C3abc@cluster0.mtqg1qf.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQFnL-EACl4WdOk861Xelygal05tTbGVXSdp91EwDpc5qPqjoFnOAtB7uR6l-HU4SsEBJcqM5qo7P4g7XOSFlGzI_EptyvBVHrHdaQXa09uI_3NKB5AgJ40rncADT3Z0YI8ZkZvU714EC6LLW_LzxnIZhQ2hWg6ymRMF5Kj2YF8eKeQ22tXkMSKMxx9WY8Y4rLnkDhloRE0nMiiBQwzdZrSIZHPi5oSMNzuybbHjtvsLg3fDhXeSd7mAX9RikaNFLvb4j0lsQB248e95x5WQJC_Da3L_q3lV3EfcrFXIvSvEpEswpMOExpc2ca6sdYcuFJWCE2omdxhWJoR_k9_Z5jhwPkdIrQAAAAEqctKjAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001989728043"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Dhhehdvsj_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
