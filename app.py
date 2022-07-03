from flask import Flask, render_template

app = Flask(__name__)

RECIPE=[
  {
    'item':1,
    'dish':'mix-veg curry',
    'spicy-level':'Normal',
    'members': 5
  },
  {
    'item':2,
    'dish':'chicken pulusu',
    'spicy-level':'medium',
    'members': 8
  },
  {
    'item':3,
    'dish':'Mutton pulusu',
    'spicy-level':'medium',
    'members': 10
  },
  {
    'item':4,
    'dish':'Mutton-Kheema-balls',
    'spicy-level':'Spicy',
    'members': 12
  }
]

ORISSA=[
{
    'item':1,
    'dish':'Dhalma',
    'spicy-level':'Normal',
    'members': 5
  },
{
    'item':2,
    'dish':'Chenna-poda',
    'members': 8
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',recipes=RECIPE,states=ORISSA)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)