from django.shortcuts import render
from django.http import JsonResponse
import pickle

def loan_client(request):
    return render(request,'loan_client.html')

def loan_status_check(request):
    # read parameters
    amount = float(request.GET["amount"])
    income = float(request.GET["income"])
    cincome = float(request.GET["cincome"])
    term = float(request.GET["term"])

    # load model and make prediction
    f = open(r"e:\classroom\ds\jan21\loan_model.pkl","rb")
    model = pickle.load(f)
    f.close()

    X_test = [[income,cincome, amount, term]]
    status = model.predict(X_test)[0]

    return JsonResponse({"status" : status})


