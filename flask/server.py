from hashlib import md5
from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Session, User, Ad
from schema import CreateUser, PatchUser, PatchAd, CreateAd, VALIDATION_CLASS
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: dict | list | str):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def http_error_handler(error: HttpError):
    error_message = {"status": "error", "description": error.message}
    response = jsonify(error_message)
    response.status_code = error.status_code
    return response


def validate_json(json_data: dict, validation_model: VALIDATION_CLASS):
    try:
        model_obj = validation_model(**json_data)
        model_obj_dict = model_obj.dict(exclude_none=True)
    except ValidationError as err:
        raise HttpError(400, message=err.errors())
    return model_obj_dict


def get_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, message="user doesn't exist")
    return user


def hash_password(password: str):
    password = password.encode()
    password_hash = md5(password)
    password_hash_str = password_hash.hexdigest()
    return password_hash_str


class UserView(MethodView):
    def get(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            return jsonify(
                {
                    "id": user.id,
                    "username": user.username,
                    "creation_time": user.creation_time.isoformat(),
                }
            )

    def post(self):
        json_data = validate_json(request.json, CreateUser)
        json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            user = User(**json_data)
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, f'{json_data["username"]} is busy')
            return jsonify({"id": user.id})

    def patch(self, user_id: int):
        json_data = validate_json(request.json, PatchUser)
        if "password" in json_data:
            json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            user = get_user(session, user_id)
            for field, value in json_data.items():
                setattr(user, field, value)
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, f'{json_data["username"]} is busy')
            return jsonify(
                {
                    "id": user.id,
                    "username": user.username,
                    "creation_time": user.creation_time.isoformat(),
                }
            )

    def delete(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            session.delete(user)
            session.commit()
            return jsonify({"status": "success"})


def get_ad(session: Session, ad_id: int):
    ad = session.get(Ad, ad_id)
    if ad is None:
        raise HttpError(404, message="ad doesn't exist")
    return ad


class AdView(MethodView):

    def get(self, ad_id: int):
        with Session() as session:
            ad = get_ad(session, ad_id)
            return jsonify({
                "ad_id": ad.id,
                "user": get_user(session, ad.user_id).username,
                "description": ad.description,
                "heading": ad.heading,
                "creation_time": ad.creation_time
            })

    def post(self):
        json_data = validate_json(request.json, CreateAd)
        with Session() as session:
            ad = Ad(**json_data)
            session.add(ad)
            session.commit()
            return jsonify({"id": ad.id})

    def patch(self, ad_id: int):
        json_data = validate_json(request.json, PatchAd)
        with Session() as session:
            ad = get_ad(session, ad_id)
            for field, value in json_data.items():
                setattr(ad, field, value)
            session.add(ad)
            session.commit()
            return jsonify(
                {
                    "ad_id": ad.id,
                    "user": get_user(session, ad.user_id).username,
                    "description": ad.description,
                    "heading": ad.heading,
                    "creation_time": ad.creation_time
                }
            )

    def delete(self, ad_id: int):
        with Session() as session:
            ad = get_ad(session, ad_id)
            session.delete(ad)
            session.commit()
            return jsonify({"status": "success"})


app.add_url_rule(
    "/user/<int:user_id>",
    view_func=UserView.as_view("with_user_id"),
    methods=["GET", "PATCH", "DELETE"],
)

app.add_url_rule("/user/", view_func=UserView.as_view("create_user"), methods=["POST"])
if __name__ == "__main__":
    app.run()
