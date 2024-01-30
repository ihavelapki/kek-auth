from flask import request, Blueprint
from ..data import connect_to_database

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    conn = connect_to_database("metadata.db")
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return {"users": users}, 200
    else:
        return {"error": "Unable to connect to the database"}, 500


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """

    :return:
    """
    request_data = request.data
    print(request_data, type(request_data))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return {'aaa': 'bbb'}

