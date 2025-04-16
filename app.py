from flask import Flask, render_template, url_for, flash, redirect
from flask import request
import pandas as pd 
import numpy as np
import os

app= Flask(__name__ , template_folder= "HTML_Templates", static_folder="CSS_Templates",
           static_url_path='/CSS_Templates')
app.config['SECRET_KEY']= '#645gfke@#234'

os.system("python download_sim_file.py")

df= None
similarity= None

def load_once():
    return np.load('sim.npy', mmap_mode= 'r'), pd.read_csv('new_df.csv')

if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    similarity, df = load_once()

@app.route("/")
def home():
    return render_template("home.html")

def recommend_book(book):
    ind= df[df['title'] == book].index
    sorted_sim= sorted(list(enumerate(similarity[ind.item()])), reverse= True, key= lambda x: x[1])[1:16]
    y= []
    for i in sorted_sim:
        y.append([i[0]])
    return y


@app.route("/Recommender_page", methods=["GET", "POST"])
def recommend():
    book= 'Alanna: The First Adventure'        # Default value
    str1= "e.g. Twilight or, Animal Farm"       # Default Value

    if request.method == "POST":
        book = request.form.get("book")
        str1= book

    if book in df['title'].values:
        indexes= recommend_book(book)
        rec= []
        for ind in indexes:     # Sending only the required rows to our html template in a form of dictionary
            rec.append({        # Since sending the entire dataframe and then accessing the values
                'title': df.iloc[ind[0]]['title'],               # there is not working properly.
                'author': df.iloc[ind[0]]['author'],
                'description': df.iloc[ind[0]]['description'],
                'coverImg': df.iloc[ind[0]]['coverImg']
            })
        return render_template("recommend.html", items= df['title'].unique(), books= rec, place= str1)
    else:
        flash(f"OOPS! the book '{book}' is not available here... Try something from the dropdown")
        return redirect(url_for('recommend'))

if __name__ == "__main__":
    app.run(debug= True)
