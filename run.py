from app import app
from flask import jsonify, request, render_template
from app.utils import get_suggestions


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def render_html():
    return render_template('index.html')


@app.route('/suggest')
def autocomplete():
    query_word = request.args.get("q", "")
    print(query_word)
    results = get_suggestions(query_word)
    resp = jsonify(results=results[:10])
    return resp


if __name__ == '__main__':
    app.run(debug=False)