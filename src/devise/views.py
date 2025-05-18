from django.http import HttpResponse
from django.shortcuts import render
import api

# Create your views here.
def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personalisé")
    return render(request, "devise/index.html", context={"data":rates,
                                                                      "days_labels":days,
                                                                      "page_label":page_label})