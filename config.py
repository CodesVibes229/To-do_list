class Config:
    SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://root:ghost229@localhost/todo_list'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_secret_key'
