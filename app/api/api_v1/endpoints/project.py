from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.crud import project as crud_project
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return crud_project.create_project(db, project)


@router.get("/", response_model=List[ProjectResponse])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_project.get_projects(db, skip=skip, limit=limit)


@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud_project.get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, updated_project: ProjectUpdate, db: Session = Depends(get_db)):
    project = crud_project.update_project(db, project_id, updated_project)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    success = crud_project.delete_project(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
