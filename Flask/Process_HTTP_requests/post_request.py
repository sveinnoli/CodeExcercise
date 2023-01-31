import requests

print(requests.post(
    url="http://127.0.0.1:5000/json_example",
    json={ 
        "language" : "Python",
        "framework" : "Flask",
        "website" : "Scotch",
        "version_info" : { 
                            "python" : "3.9.0", 
                            "flask" : "1.1.2" 
                            }, 
        "examples" : ["query", "form", "json"], 
        "boolean_test" : True }).text
    )