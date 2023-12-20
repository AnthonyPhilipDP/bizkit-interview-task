from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    filtered_users = []

    # Changing the declaration value based on search condition

    if 'id' in args:
        user_with_id = next((user for user in USERS if user.get('id') == args['id']), None)
        if user_with_id:
            filtered_users.append(user_with_id)

    if 'name' in args:
        name_query = args['name']
        filtered_users += [user for user in USERS if name_query in user.get('name', '')]

    if 'age' in args:
        age_query = int(args['age'])
        filtered_users += [user for user in USERS if age_query - 1 <= int(user.get('age', 0)) <= age_query + 1]

    if 'occupation' in args:
        occupation_query = args['occupation']
        filtered_users += [user for user in USERS if occupation_query in user.get('occupation', '')]

    #To avoid repetition of user results
    unique_user_result = []
    for user in filtered_users:
        if user not in unique_user_result:
            unique_user_result.append(user)

    return unique_user_result