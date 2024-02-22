from database import DB
from generator import Generator

DB.insert(account='linkedin',pwd=Generator.generatePwd())
print(DB.get())