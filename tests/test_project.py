from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal
from app.db.project import Project

client = TestClient(app)


def test_create_project():
    response = client.post("/api/v1/projects/",
                           json={"name": "Test Project", "description": "Test Description", "status": "ongoing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Project"

    # Clean up
    db = SessionLocal()
    db.query(Project).delete()
    db.commit()
    db.close()
