print("- in modelsUsers")
# from .main import Base_users, sess_users
from .main import dict_base, dict_sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# from itsdangerous.serializer import Serializer
from itsdangerous.url_safe import URLSafeTimedSerializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app

Base_users = dict_base['Base_users']
sess_users = dict_sess['sess_users']

def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]



class Users(Base_users, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    # posts = relationship('BlogPosts', backref='author', lazy=True)
    # photo_dir = relationship('PhotoDirectories', backref='photo_directory', lazy=True)

    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    # rincons = relationship("UsersToRincons", back_populates="user")
    directories = relationship("UsersToDirectories", back_populates="user")

    def get_reset_token(self):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:

            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        return sess_users.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email})'


class PhotoDirectories(Base_users):
    __tablename__ = 'photo_directories'
    id = Column(Integer, primary_key = True)
    unique_dir_name = Column(Text,unique=True)
    display_name = Column(Text)
    display_name_no_spaces = Column(Text, nullable = False)
    public = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    users = relationship("UsersToDirectories", back_populates="directory")

    def __repr__(self):
        return f'PhotoDirectories(id: {self.id}, user_id: {self.user_id}, name: {self.name})'

##########
# Associations
##############

class UsersToDirectories(Base_users):
    __tablename__ = 'users_to_directories'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    directory_id = Column(Integer, ForeignKey('photo_directories.id'), primary_key=True)
    permission_view = Column(Boolean, default=True)
    permission_delete = Column(Boolean, default=False)
    permission_add_to_dir = Column(Boolean, default=False)
    permission_admin = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    directory = relationship("PhotoDirectories", back_populates="users")
    user = relationship("Users", back_populates="directories")

    def __repr__(self):
        return f'UsersToDirectories(users_table_id: {self.users_table_id}, directories_table_id: {self.directories_table_id})' 