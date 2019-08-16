from flask import Flask, render_template,url_for
app=Flask(__name__) #basic name of the module is __name__.
# flask looks for templates and file in it
#decoraters are used to add functionalities to the site

"""for creating multiple posts in the website we can use a list 
of dictionaries in ewhich we will specify the author and the data
 which we wanted to be displayed on the webpage"""
posts=[
    {
        'author':'corey schafer',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'april 20,2019'
    },
    {
        'author':'harsh',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'april 21,2019'
    }

]

@app.route("/")
#it handles all the complicated stuff backhand
#it is used for the first page
@app.route("/home")
#it was to provide anothe page as home page
# '/ is the address of the webpage we have developed'
def home():
    return render_template('new.html',posts=posts)
#we have used the posts function in the above line
# because this function will tell the html file what
# to tke and print from the python dictionary.
@app.route("/about")
#it handles all the complicated stuff backhand
# '/ is the address of the webpage we have developed'
def about():
    return render_template('about.html',title='ABOUT PAGE')


if __name__=='__main__':
    app.run(debug=True)