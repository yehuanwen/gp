from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, INTEGER
from sqlalchemy.orm import relationship
from gp.connections import Base


class Product(Base):
    # 表的名字:
    __tablename__ = 'product'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, autoincrement=True)  # ID
    updated_at = Column(INTEGER)  # 最后一次更新时间

    gp_icon = Column(TEXT)   # 图标
    gp_name = Column(TEXT)  # GP名称
    gp_tag = Column(TEXT)  # GP标签
    gp_url = Column(TEXT)  # GP链接
    gp_intro = Column(TEXT)  # GP介绍
    gp_developer = Column(TEXT)  # GP开发者
    gp_rating = Column(TEXT)  # GP评级
    gp_package = Column(TEXT)  # GP包名
    gp_picture = Column(TEXT)  # GP图片，英文逗号分割
    gp_version = Column(TEXT)  # GP最新版本
    gp_update = Column(TEXT)  # GP更新时间
    gp_news = Column(TEXT)  # GP更新内容
    gp_video_image = Column(TEXT)  # GP视频图片
    gp_video_url = Column(TEXT)  # GP视频链接
    gp_review = relationship("GPReview")# GP评论
    gp_downloads = Column(TEXT)  # GP下载人数


class GPReview(Base):
    # 表的名字:
    __tablename__ = 'gp_review'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, autoincrement=True)  # ID
    product_id = Column(INTEGER, ForeignKey(Product.id))
    avatar_url = Column(TEXT)   # 头像链接
    user_name = Column(TEXT)  # 用户名称
    review_text = Column(TEXT)  # 评论
    rating_star = Column(INTEGER)  # 评星个数，1~5
