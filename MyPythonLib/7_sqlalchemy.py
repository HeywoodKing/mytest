# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey, \
    UniqueConstraint, ForeignKeyConstraint, Index, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func


engine = create_engine('mysql+pymysql://root:123456@192.168.99.100/test?charset=utf8',
                       max_overflow=5)
Base = declarative_base()


# 创建单表:业务线
class Business(Base):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bname = Column(String(32), nullable=False, index=True)


# 多对一:多个服务可以属于一个业务线,多个业务线不能包含同一个服务
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(32), nullable=True, index=True)
    ip = Column(String(15), nullable=False)
    port = Column(Integer, nullable=False)

    business_id = Column(Integer, ForeignKey('business.id'))

    # 在ForeignKey所在的类内添加relationship的字段,注意:
    # 1:Business是类名
    # 2:business字段不会再数据库表中生成字段
    # 3:business用于Service表查询Business表(正向查询),而service用于Business表查询Service表(反向查询)
    business = relationship('Business', backref='service')

    __table_args__ = (
        UniqueConstraint(ip, port, name='uix_ip_port'),
        Index('ix_id_sname', id, sname),
        # ForeignKeyConstraint(['business_id'], ['business.id'])
    )


# 一对一:一种角色只能管理一条业务线,一条业务线只能被一种角色管理
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rname = Column(String(32), nullable=False, index=True)
    priv = Column(String(64), nullable=False)

    business_id = Column(Integer, ForeignKey('business.id'), unique=True)


# 多对多:多个用户可以是同一个role,多个role可以包含同一个用户
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(32), nullable=False, index=True)


class Users2Role(Base):
    __tablename__ = 'users2role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('users.id'))
    rid = Column(Integer, ForeignKey('role.id'))

    __table_args__ = (
        UniqueConstraint(uid, rid, name='uix_uid_rid'),
    )


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def db_session():
    DbSession = sessionmaker(bind=engine)
    session = DbSession()
    return session


def insert():
    session = db_session()
    # row_business = Business(bname='快递')
    # session.add(row_business)
    # session.add_all([
    #     Business(bname='日化'),
    #     Business(bname='家电'),
    #     Business(bname='旅游'),
    #     Business(bname='电影')
    # ])
    session.add_all([
        Service(sname='延保', ip='127.0.0.1', port=1000, business_id=1),
        Service(sname='正常保', ip='127.0.0.1', port=1001, business_id=1),
        Service(sname='加强保', ip='127.0.0.1', port=1002, business_id=2),
        Service(sname='休眠期', ip='127.0.0.1', port=1003, business_id=2)
    ])
    session.commit()


def delete():
    session = db_session()
    session.query(Business).filter(Business.id > 3).delete()
    # user_willdel = session.query(User).filter_by(id='5').first()
    # session.delete(user_willdel)
    session.commit()


def update():
    session = db_session()
    session.query(Business).filter(Business.id>1).update({'bname': '电子商务'})
    session.query(Business).filter(Business.id>1).update({'bname': Business.bname + '_SB'}, synchronize_session=False)
    # session.query(Business).filter(Business.id=1).update({'id': Business.id * 100}, synchronize_session='evaluate')
    # session.query(User).filter_by(id='1').first()
    session.commit()


def query():
    session = db_session()
    # res = session.query(Business).all()

    # 一、条件
    # res = session.query(Business).filter(Business.id>0)
    # res = session.query(User).filter(User.id == '5').one()
    # res = session.query(Business.bname).order_by(Business.id).all()
    # res = session.query(Business.id,Business.bname).first()
    # res = session.query(Business).filter(Business.id>0, Business.id<3)
    # res = session.query(Business).filter_by(bname='lili').all()
    # res = session.query(Business).filter(Business.id.between(1, 3), Business.bname=='zhangsan').all()
    # res = session.query(Business).filter(Business.id.in_([1, 3, 5]), Business.bname=='lisi').all()
    # res = session.query(Business).filter(~Business.id.in_([1, 3, 5], Business.bname=='liuliu')).all()
    # res = session.query(Business).filter(and_(Business.id > 2, Business.bname=='liuliu')).all()
    # res = session.query(Business).filter(or_(Business.id > 2, Business.bname=='六三')).all()
    # res = session.query(Business).filter(
    #     or_(Business.id == 2, and_(Business.id > 3, Business.bname=='lisi'), Business.bname!='')
    # ).all()

    # 二、通配符
    # res = session.query(Business).filter(Business.bname.like('%海%')).all()
    # res = session.query(Business).filter(Business.bname.like('%海_%')).all()

    # 三、limit
    # res = session.query(Business)[0:5:2]

    # 四、排序
    # res = session.query(Business).order_by(Business.id.desc()).all()
    # res = session.query(Business).order_by(Business.id.desc(), Business.bname.asc()).all()

    # 五、分组
    # res = session.query(Business.bname).group_by(Business.bname).all()

    # res = session.query(
    #     func.max(Business.id),
    #     func.min(Business.bname),
    #     func.sum(Business.bname),
    #     func.avg(Business.bname),
    #     func.count(Business.bname),
    # ).group_by(Business.id).all()
    # res = session.query(
    #     Business.bname,
    #     func.count(1),
    # ).group_by(Business.bname).having(func.count(1) > 2).all()

    # 六、连表
    # 笛卡尔积
    # res = session.query(Business, Service).all()

    # where条件
    # res = session.query(Business, Service).filter(Business.id == Service.business_id).all()

    # 内连接
    # join默认为内连接,SQLAlchemy会自动帮我们通过foreign key字段去找关联关系
    # res = session.query(Business).join(Service)
    # res = session.query(Business.id, Business.bname, Service.id, Service.sname).join(Service).all()

    # 左连接:isouter=True #右连接:同左连接,只是把两个表的位置换一下
    # res = session.query(Business.id, Business.bname, Service.id, Service.sname).join(Service, isouter=True).all()

    # 七、组合
    # q1 = session.query(Business.id, Business.bname).filter(Business.id > 0, Business.id < 5)
    # q2 = session.query(Business.id, Business.bname).filter(
    #     or_(
    #         Business.bname.like('%林%'),
    #         Business.bname.like('%海%'),
    #     )
    # )

    # 组合+去重
    # res1 = q1.union(q2)
    # 组合,不去重
    # res2 = q1.union_all(q2)
    # print([i.ename for i in q1.all()])  # ['林海峰', '李杰', '武配齐', '元昊']
    # print([i.ename for i in q2.all()])  # ['林海峰', '元昊']
    # print([i.ename for i in res1.all()])  # ['林海峰', '李杰', '武配齐', '元昊']
    # print([i.ename for i in res2.all()])  # ['林海峰', '李杰', '武配齐', '元昊', '元昊', '林海峰']

    # 示例:查出id大于2的员工,当做子查询的表使用

    # 原生SQL:
    # select * from (select * from emp where id > 2);
    # res = session.query(session.query(Business).filter(Business.id > 2).subquery()).all()

    # 示例:#查出销售部门的员工姓名

    # 原生SQL:
    # select ename from emp where dep_id in (select id from dep where dname='销售');
    # res = session.query(Service.sname).filter(Service.business_id.in_(
    #     session.query(Business.id).filter_by(bname='销售'),  # 传的是参数
    #     # session.query(Business.id).filter(Business.bname=='销售') # 传的是表达式
    # )).all()

    # 示例:查询所有的员工姓名与部门名

    # 原生SQL:
    # select ename as 员工姓名,(select dname from dep where id = emp.dep_id) as 部门名 from emp;
    # sub_sql = session.query(Business.bname).filter(Business.id==Service.business_id)
    # sub_sql.as_scalar()  # as_scalar的功能就是把上面的sub_sql加上了括号
    # res = session.query(Users.uname, sub_sql.as_scalar()).all()

    # 五 正查、反查
    # 一 标准连表查询
    # res = session.query(Business.bname, Service.sname).join(Service)

    # 三 基于relationship的正查、反查
    # 查询员工名与其部门名(正向查)
    # res = session.query(Service)
    # for row in res:
    #     print(row.sname, row.id, row.business.bname)

    # 查询部门名以及该部门下的员工(反向查)
    res = session.query(Business).order_by(Business.id)
    for row in res:
        if row.service:
            for item in row.service:
                print(row.id, row.bname, item.sname)
        else:
            print(row.id, row.bname)

    # for row in res:
    #     print(row.id, row.bname, id(row))


if __name__ == "__main__":
    # drop_db()
    # init_db()
    # insert()
    query()





# # cursor = engine.execute('select version()')
# cursor = engine.execute('select * from region where pid=%s', [3])
#
# # res = cursor.fetchone()
# # res = cursor.fetchmany(3)
# res = cursor.fetchall()
# print(res)

