from django.shortcuts import render

# Create your views here.
def django_page(request):
    context={}
    context['page_title']='Ex01 : Django, framework web.'
    context['style']='style1.css'
    context['text_content']='''Django is a free and open-source web framework,
    written in Python, which follows the model-view-template (MVT) architectural
     pattern. It is maintained by the Django Software Foundation (DSF), an
    independent organization established as a 501(c)(3) non-profit. Django was
    created in the fall of 2003, when the web programmers at the Lawrence
    Journal-World newspaper, Adrian Holovaty and Simon Willison, began using
    Python to build applications. It was released publicly under a BSD license
    in July 2005. The framework was named after guitarist Django Reinhardt. In
    June 2008, it was announced that a newly formed Django Software Foundation
    (DSF) would maintain Django in the future.'''
    return render(request, 'base.html',context)

def affichage_page(request):
    context={}
    context['page_title']='Ex01 : Processus d’affichage d’une page statique.'
    context['style']='style1.css'
    context['text_content']='''Nous venons d\'afficher une belle page statique
    a l\'aide de la fonction return et d\'un template fort bien leche.'''
    return render(request, 'base.html',context)

def templates_page(request):
    context={}
    context['page_title']='Ex01 : Moteur de template.'
    context['style']='style2.css'
    context['text_content']='''For tags: {% for x in list %} {{x-dependent
    variable}} {% endfor %} If tags: {% if x condition %} (if no specified
    condition, "if x exists" will be assumed) action {% elif condition %}
    {% else %} {% endif %} Blocks: in main template, {% block blockname %}
    content (or no content) {% endblock %} creates a block type used in other
    templates thanks to the inheritance functions. A child template would begin
    with {% extends "parenttemplate.html" %} and use the pre-xisting blocks to
    override their content.'''
    return render(request, 'base.html',context)
