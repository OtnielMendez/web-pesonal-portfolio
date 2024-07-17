from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")



def contact(request):
    return render(request, "core/contact.html")

# html_base = '''
# "<h1>Mi web personal</h1>

# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about">Acerca de</a></li>
#     <li><a href="/portfolio">Portafolio</a></li>
#     <li><a href="/contact">Contacto</a></li>
    
# </ul>


# '''

# # Create your views here.
# #def home(request):
#     #return render(request, "core/home.html")

# def home(request):
#     return render(request, "core/home.html")

# def about(request):
#     return render(request, "core/about.html")

# def portfolio(request):
#     return render(request, "core/portfolio.html")

# def contact(request):
#     return render(request, "core/contact.html")

# def about(request):
#     return HttpResponse( """
#         <h2>Acerca de</h2>
#         <p>Me llamo Otniel y me encanta Django!</p>
#     """)

# def portfolio(request):
#     return HttpResponse("""
#         <h2>Portfolio</h2>
#         <p>Me llamo Otniel y me encanta Django!</p>
#     """)


# def contact(request):
#     return HttpResponse(html_base + """
#         <h2>Contact</h2>
#         <p>Aquí less dejo mi email y mis redes sociales:</p>

#     """)

