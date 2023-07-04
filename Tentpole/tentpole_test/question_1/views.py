from django.shortcuts import render
from django.http import HttpResponse  
from question_1 import forms
from question_1.functions import handle_uploaded_file  
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Create your views here.

def form_name_view(request):
    """This Function Processes the form POST

    Returns:
        HttpResponse : returns a response for processing the form content
    """
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST, request.FILES)

        if form.is_valid():
           handle_uploaded_file(request.FILES['statement_file'])  
           return generate_graph(request)  
           
        else:
            form = form = forms.FormName()
            

    return render(request, 'question_1/form.html',  {'form': form})

def generate_graph(request):
    """This Function generates and saves the graph

    Returns:
        HttpResponse: returns a reponse for generating the graph and redirects to a visual representation of the graph
    """
    file_name = request.FILES['statement_file']
    print(file_name)
    # Read the spreadsheet file
    data = pd.read_excel('./static/upload/' + str(file_name), engine='openpyxl')
    
    # Extract necessary data columns from the spreadsheet
    dates = data['Month']
    incomes = data['Income']
    expenses = data['Expenses']
    
    # Generate the graph
    plt.plot(dates, incomes, label='Income')
    plt.plot(dates, expenses, label='Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Income and Expenses Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Save the graph to a file and render it directly in the browser
    plt.savefig('./static/graph/graph.png')
    plt.show()

    return render(request, 'question_1/graph.html')
    