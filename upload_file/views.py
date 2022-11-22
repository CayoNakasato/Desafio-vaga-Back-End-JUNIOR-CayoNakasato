from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

from utils import read_file


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']

        db = FileSystemStorage()

        db.save(uploaded_file.name, uploaded_file)

        transactions = read_file.transaction_list(f"media/{uploaded_file}")
        
        print(transactions)

    return render(request, "upload.html")
