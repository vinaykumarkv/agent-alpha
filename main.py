from services.pipeline import run_pipeline
from db.db_init import initialize_db

def test_pipeline():
    initialize_db()

    image_path = "data/images/sample.png"

    result = run_pipeline(image_path)

    print("\n✅ Pipeline Output:")
    print(result)


if __name__ == "__main__":
    test_pipeline()