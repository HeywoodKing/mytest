from setting import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from models import *

engine = create_engine(DB_URI, encoding="utf-8", echo=True, max_overflow=5)
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def delete(id):
    session = Session()
    session.query(Users).filter(Users.id > id).delete()
    session.commit()


def update(id, obj):
    session = Session()
    session.query(Users).filter(Users.id > id).update({"name": "099"})
    session.query(Users).filter(Users.id > id).update({Users.name: Users.name + "099"}, synchronize_session=False)
    session.query(Users).filter(Users.id > id).update({"num": Users.num + 1}, synchronize_session="evaluate")


def query():
    # ###### 查 ######
    session = Session()
    print(session.query(UserType))
    user_type_list = session.query(UserType).all()
    for row in user_type_list:
        print(row.id, row.title)

    # select xxx from UserType where
    user_type_list = session.query(UserType.id, UserType.title).filter(UserType.id > 2)
    for row in user_type_list:
        print(row.id, row.title)


def query2():
    # ###### 查 ######
    session = Session()
    # 　条件
    ret = session.query(Users).filter_by(name='alex').all()
    ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
    ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
    ret = session.query(Users).filter(Users.id.in_([1, 3, 4])).all()
    ret = session.query(Users).filter(~Users.id.in_([1, 3, 4])).all() // 非
    ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()
    from sqlalchemy import and_, or_
    ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
    ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
    ret = session.query(Users).filter(
        or_(
            Users.id < 2,
            and_(Users.name == 'eric', Users.id > 3),
            Users.extra != ""
        )).all()

    # 通配符
    ret = session.query(Users).filter(Users.name.like('e%')).all()
    ret = session.query(Users).filter(~Users.name.like('e%')).all()

    # 限制
    ret = session.query(Users)[1:2]

    # 排序
    ret = session.query(Users).order_by(Users.name.desc()).all()
    ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

    # 分组
    from sqlalchemy.sql import func

    ret = session.query(Users).group_by(Users.extra).all()
    ret = session.query(
        func.max(Users.id),
        func.sum(Users.id),
        func.min(Users.id)).group_by(Users.name).all()

    ret = session.query(
        func.max(Users.id),
        func.sum(Users.id),
        func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) > 2).all()

    # 连表

    ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()

    ret = session.query(Person).join(Favor).all()

    ret = session.query(Person).join(Favor, isouter=True).all()

    # 组合
    q1 = session.query(Users.name).filter(Users.id > 2)
    q2 = session.query(Favor.caption).filter(Favor.nid < 2)
    ret = q1.union(q2).all()

    q1 = session.query(Users.name).filter(Users.id > 2)
    q2 = session.query(Favor.caption).filter(Favor.nid < 2)
    ret = q1.union_all(q2).all()

    # 分组，排序，连表，通配符，子查询，limit，union,where,原生SQL、
    # ret = session.query(Users, UserType)
    # select * from user,usertype;
    #
    # ret = session.query(Users, UserType).filter(Users.usertype_id==UserType.id)
    # select * from user,usertype whre user.usertype_id = usertype.id

    # result = session.query(Users).join(UserType)
    # print(result)

    # result = session.query(Users).join(UserType,isouter=True)
    # print(result)

    # 1.
    # select * from b where id in (select id from tb2)

    # 2 select * from (select * from tb) as B
    # q1 = session.query(UserType).filter(UserType.id > 0).subquery()
    # result = session.query(q1).all()
    # print(result)

    # 3
    # select
    #   id ,
    #   (select * from users where users.user_type_id=usertype.id)
    # from usertype;

    # session.query(UserType,session.query(Users).filter(Users.id == 1).subquery())
    # session.query(UserType,Users)
    # result = session.query(UserType.id,session.query(Users).as_scalar())
    # print(result)
    # result = session.query(UserType.id,session.query(Users).filter(Users.user_type_id==UserType.id).as_scalar())
    # print(result)

    # 问题1. 获取用户信息以及与其关联的用户类型名称(FK,Relationship=>正向操作)
    # user_list = session.query(Users,UserType).join(UserType,isouter=True)
    # print(user_list)
    # for row in user_list:
    #     print(row[0].id,row[0].name,row[0].email,row[0].user_type_id,row[1].title)

    # user_list = session.query(Users.name,UserType.title).join(UserType,isouter=True).all()
    # for row in user_list:
    #     print(row[0],row[1],row.name,row.title)

    # user_list = session.query(Users)
    # for row in user_list:
    #     print(row.name,row.id,row.user_type.title)

    # 问题2. 获取用户类型
    # type_list = session.query(UserType)
    # for row in type_list:
    #     print(row.id,row.title,session.query(Users).filter(Users.user_type_id == row.id).all())

    # type_list = session.query(UserType)
    # for row in type_list:
    #     print(row.id,row.title,row.xxoo)

    # ###### 删除 ######
    # session.query(UserType.id,UserType.title).filter(UserType.id > 2).delete()

    # ###### 修改 ######
    # session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({"title" : "黑金"})
    # session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({UserType.title: UserType.title + "x"}, synchronize_session=False)
    # session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({"num": Users.num + 1}, synchronize_session="evaluate")

    session.commit()
    session.close()

    # 注：设置外检的另一种方式 ForeignKeyConstraint(['other_id'], ['othertable.other_id'])
