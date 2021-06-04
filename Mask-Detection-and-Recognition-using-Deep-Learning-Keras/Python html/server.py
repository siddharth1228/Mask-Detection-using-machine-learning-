from flask import Flask, render_template,request
from subprocess import call
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/C:/Users/siddh/Mask-Detection-and-Recognition-using-Deep-Learning-Keras/Python html/templates/Mask Testing using images (1).py', methods=['POST'])
def my_link1():
  print ('I got clicked!')
  
  call(["python", "C:/Users/siddh/Mask-Detection-and-Recognition-using-Deep-Learning-Keras/Python html/Mask Testing using images (1).py"])
  return render_template('index.html') 
@app.route('/C:/Users/siddh/Mask-Detection-and-Recognition-using-Deep-Learning-Keras/Mask Testing using Video (1).py', methods=['POST'])
def my_link2():
  print ('I got clicked!')
  call(["python", "C:/Users/siddh/Mask-Detection-and-Recognition-using-Deep-Learning-Keras/Mask Testing using Video (1).py"])
  return render_template('index.html')  

if __name__ == '__main__':
  app.run(debug=True)