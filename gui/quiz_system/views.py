from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

def question(request):
    return render(request, 'quiz_system/question.html')

def answer(request):
    with connection.cursor() as cursor:
        cursor.execute(request.POST.get('answer',''))
        data = '<table style= "border: 1px solid black;" >'
        for row in cursor.fetchall():
            data +='<tr>'
            for col in row:
                data += '<td>'+str(col)+'</td>'
            data +='</tr>'
        data += '</table>'
    return HttpResponse(data)
