from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def resume_view(request):
    resume_data = {
        "name": "Sarath S",
        "title": "Django Fullstack Developer",
        "location": "Kerala, India",
        "email": "sarathpvtmail@gmail.com",
        "links": {
            "linkedin": "LinkedIn",
            "github": "https://github.com/saraths3"
        },
        "summary": "Django full-stack developer with a Computer Science degree. Built projects including a password manager, price comparison app, and Linux automation tool.",
        "skills": [
            "Python", "Django", "HTML", "CSS", "JavaScript", 
            "React", "REST APIs", "SQLite", "PostgreSQL", "Linux"
        ],
        "projects": [
            {
                "title": "GrabMe – Price Comparison Web App",
                "desc": "Developed a price comparison web application using Python and Django.",
                "link": "https://github.com/saraths3/Grabme-python"
            },
            {
                "title": "Portable Password Manager",
                "desc": "Built a secure, portable password manager application using Python.",
                "link": "https://github.com/saraths3/Portable-Password-Manager-in-Python"
            },
            {
                "title": "QuickTasker",
                "desc": "Linux automation toolkit built to work across all major distributions.",
                "link": "https://github.com/saraths3/Quicktasker"
            }
        ],
        "education": {
            "degree": "Bachelor’s Degree in Computer Science",
            "univ": "University of Kerala Thiruvanandapuram",
            "years": "2021 - 2024"
        }
    }
    # Per your tree, resume.html is in myresume/templates/
    return render(request, 'resume.html', {'resume': resume_data})