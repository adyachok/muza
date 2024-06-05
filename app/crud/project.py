from sqlalchemy.orm import Session
from app.db.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from typing import List, Optional


def create_project(db: Session, project: ProjectCreate) -> ProjectResponse:
    db_project = Project(name=project.name, description=project.description, status=project.status)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return ProjectResponse.from_orm(db_project)


def get_projects(db: Session, skip: int = 0, limit: int = 10) -> List[ProjectResponse]:
    projects = db.query(Project).offset(skip).limit(limit).all()
    return [ProjectResponse.from_orm(project) for project in projects]


def get_project(db: Session, project_id: int) -> Optional[ProjectResponse]:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        return ProjectResponse.from_orm(project)
    return None


def update_project(db: Session, project_id: int, updated_project: ProjectUpdate) -> Optional[ProjectResponse]:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        return None
    project.name = updated_project.name
    project.description = updated_project.description
    project.status = updated_project.status
    db.commit()
    db.refresh(project)
    return ProjectResponse.from_orm(project)


def delete_project(db: Session, project_id: int) -> bool:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        return False
    db.delete(project)
    db.commit()
    return True
