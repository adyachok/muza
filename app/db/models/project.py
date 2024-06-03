from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from ..session import Base

project_users = Table(
    'project_users',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('user_id', String, ForeignKey('users.id'), primary_key=True)
)


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    status = Column(String, default="ongoing")
    owner_id = Column(String, ForeignKey('users.id'))  # Assuming user_id is a string (e.g., email or AD username)
    owner = relationship("User", back_populates="projects")
    nominated_users = relationship("User", secondary=project_users, back_populates="nominated_projects")


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)  # Using string ID
    username = Column(String, unique=True, index=True)
    projects = relationship("Project", back_populates="owner")
    nominated_projects = relationship("Project", secondary=project_users, back_populates="nominated_users")
