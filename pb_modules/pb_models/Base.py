print("- in modelsBase")
from sqlalchemy import create_engine, inspect
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship, declarative_base
from .config import config
import os


Base_users = declarative_base()
# Base_cage = declarative_base()
# Base_bls = declarative_base()

dict_base = {}
dict_base["Base_users"]=Base_users
# dict_base["Base_cage"]=Base_cage
# dict_base["Base_bls"]=Base_bls

engine_users = create_engine(config.SQL_URI_USERS)
# engine_cage = create_engine(config.SQL_URI_CAGE)
# engine_bls = create_engine(config.SQL_URI_BLS)
dict_engine = {}
dict_engine["engine_users"]=engine_users
# dict_engine["engine_cage"]=engine_cage
# dict_engine["engine_bls"]=engine_bls

SessionUsers = sessionmaker(bind = engine_users)
# SessionCage = sessionmaker(bind = engine_cage)
# SessionBls = sessionmaker(bind = engine_bls)

sess_users = SessionUsers()
# sess_cage = SessionCage()
# sess_bls = SessionBls()
dict_sess = {}
dict_sess["sess_users"]=sess_users
# dict_sess["sess_cage"]=sess_cage
# dict_sess["sess_bls"]=sess_bls



