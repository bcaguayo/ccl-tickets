from flask import Blueprint, make_response, jsonify, render_template
from .controller import MainController


main_bp = Blueprint('main', __name__)
main_controller = MainController()

@main_bp.route('/', )
def home():
    return render_template('index.html')

@main_bp.route('/test', methods=['GET'])
def test():
    """ Example endpoint with simple greeting.
    ---
    tags:
      - Example API
    responses:
      200:
        description: A simple greeting
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello World!"
    """
    result=main_controller.test()
    return make_response(jsonify(data=result))
      