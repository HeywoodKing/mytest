from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, CHAR, VARCHAR

Base = declarative_base()


# 创建单表
class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(32), nullable=True, index=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(32), nullable=True, index=True)
    email = Column(VARCHAR(16), unique=True)
    # user_type_id = Column(Integer,ForeignKey("usertype.id"))

    # user_type = relationship("UserType",backref='xxoo')
    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_n_ex','name', 'email',),
    # )
