from django.shortcuts import render

# Create your views here.
def bics(request):

    colors=[[]]
    colors[0]=['rgb(0,0,0)','rgb(255,0,0)','rgb(0,0,255)','rgb(0,255,0)']
    former_shade=255
    new_shade=250
    for i in range(1,50):
        colors.append(['','','',''])
        colors[i][0]=colors[i-1][0].replace(str(255-int(former_shade)),str(255-int(new_shade)))
        for j in range(1,4):
            colors[i][j]=colors[i-1][j].replace(str(former_shade),str(new_shade))
        former_shade-=5
        new_shade-=5
    context={'colors':colors}


    return render(request,'template_bics.html',context)
