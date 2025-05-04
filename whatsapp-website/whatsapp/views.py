from django.shortcuts import render
import json
from django.conf import settings

def get_group_contacts(group_name):
    with open(settings.GROUPS_JSON_PATH, 'r') as file:
        data = json.load(file)
    return data["groups"].get(group_name, {}).get("contacts", [])

def base_view(request):
    return render(request, 'whatsapp/base.html')

def group1_view(request):
    return render(request, 'whatsapp/group1.html')

def group2_view(request):
    return render(request, 'whatsapp/group2.html')

def group3_view(request):
    contacts = get_group_contacts("Group 3")
    return render(request, 'whatsapp/group3.html',{'contacts': contacts})