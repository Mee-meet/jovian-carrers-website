from flask import Flask
app=Flask(__name__)
@app.route("/")
def helloworld():
  return "hello worldd"

print(__name__)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)