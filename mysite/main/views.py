from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"main/home.html")

portfolio_data =[
    {"title":"Project 1",
    "description":"Some quick example text to build on the card title and make up the bulk of the card's content.",
    "image_url":'main/images/portfolio/pic2.jpg',
    },
    {"title":"Project 1",
    "description":"Some quick example text to build on the card title and make up the bulk of the card's content.",
    "image_url":'main/images/portfolio/pic2.jpg',
    },
    
]

def portfolio(request):
    return render(request,"main/portfolio.html",{
        "portfolio_data":portfolio_data,
    })

programming_languages=[
    "C/C++","Python","JAVA","Javascript"
]

web_skills=[
    "HTML","CSS","BOOTSTRAP","DJANGO"
]

databases=[
    "MYSQL","MongoDB","SQLite","POSGRESQL"
]

data_science=[
    "Numpy","Pandas","Matplotlib","Seaborn","Keras",
    "Tensorflow","OpenCV","Machine learning","Deep learning","Natural language processing"
]

def skills(request):
    return render(request,"main/skills.html",{
        "programming_languages":programming_languages,
        "web_skills":web_skills,
        "databases":databases,
        "data_science":data_science,

    })

def about(request):
    return render(request,"main/about.html")

def contact(request):
    return render(request,"main/contact.html")