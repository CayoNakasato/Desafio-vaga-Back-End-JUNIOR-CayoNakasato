from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage

from utils import read_file

from upload_file.models import Transaction

def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']

        db = FileSystemStorage()

        db.save(uploaded_file.name, uploaded_file)

        transactions = read_file.transaction_list(f"media/{uploaded_file}")

        for transaction in transactions:
            Transaction.objects.create(**transaction)
        return redirect("/transactions/")

    return render(request, "upload.html")

def render_cards(req):
    card_transaction = Transaction.objects.values(
        "type",
        "date",
        "value",
        "cpf",
        "card",
        "hour",
        "owner",
        "shop_name"
    )

    total_value = read_file.sum_values(card_transaction)

    return render(req, "render_cards.html", context={"card_transaction": card_transaction, "total_value": total_value})

