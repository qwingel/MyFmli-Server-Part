import waitress

from app import create_app


if __name__ == "__main__":
    waitress.serve(app=create_app(), port=80)