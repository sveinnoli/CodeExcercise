from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    query_data = request.args.get("query_data")
    return f"Query string: {query_data}"

@app.route('/form_example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
            <h1>The language value is: {}</h1>
            <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

@app.route("/json_example", methods=["POST"])
def json_example():
    if request.method == 'POST':
        request_data = request.get_json()
        print(request_data)

        language = None
        framework = None
        python_version = None
        example = None
        boolean_test = None
        if request_data:
            if 'language' in request_data:
                language = request_data['language']

            if 'framework' in request_data:
                framework = request_data['framework']

            if 'version_info' in request_data:
                if 'python' in request_data['version_info']:
                    python_version = request_data['version_info']['python']

            if 'examples' in request_data:
                if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                    example = request_data['examples'][0]

            if 'boolean_test' in request_data:
                boolean_test = request_data['boolean_test']

    return '''
            The language value is: {}
            The framework value is: {}
            The Python version is: {}
            The item at index 0 in the example list is: {}
            The boolean value is: {}
            {}'''.format(language, framework, python_version, example, boolean_test, request_data)

@app.errorhandler(405)
def err(e):
    return "Does not support GET"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')