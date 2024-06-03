from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal
from app.db.models.persona import Persona

client = TestClient(app)

def test_create_persona():
    response = client.post("/api/v1/personas/", json={"name": "John Doe", "age": 30})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert "id" in response.json()

    # Clean up
    db = SessionLocal()
    db.query(Persona).delete()
    db.commit()
    db.close()

def test_read_persona():
    db = SessionLocal()
    # Create a test persona
    persona = Persona(name="Alice", age=25)
    db.add(persona)
    db.commit()

    # Test reading the persona
    response = client.get(f"/api/v1/personas/{persona.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["age"] == 25

    db.query(Persona).delete()
    db.commit()
    db.close()

def test_update_persona():
    db = SessionLocal()
    # Create a test persona
    persona = Persona(name="Bob", age=40)
    db.add(persona)
    db.commit()

    # Update the persona
    updated_data = {"name": "Bob Updated", "age": 45}
    response = client.put(f"/api/v1/personas/{persona.id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Bob Updated"
    assert response.json()["age"] == 45

    db.query(Persona).delete()
    db.commit()
    db.close()

def test_delete_persona():
    db = SessionLocal()
    # Create a test persona
    persona = Persona(name="Charlie", age=35)
    db.add(persona)
    db.commit()

    # Delete the persona
    response = client.delete(f"/api/v1/personas/{persona.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Persona deleted successfully"}

    db.close()
