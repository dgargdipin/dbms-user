from cms import app
print(app.url_map)
if __name__=="__main__":
    app.run(debug=True,port=5001)
