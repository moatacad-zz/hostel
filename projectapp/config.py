class AppConfig:
    SECRET_KEY='O7hPqKchcAdlmbo'

class LiveConfig(AppConfig):
    SECRET_KEY='Hz_Vq0XyJUJ6rbo'
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root@localhost/hostel'
    SQLALCHEMY_TRACK_MODIFICATIONS=True