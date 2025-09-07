from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Pacil Store',
        'name': 'Jovian Felix Rustan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)