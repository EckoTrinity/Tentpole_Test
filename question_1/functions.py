

def handle_uploaded_file(f):  
    """Saves the file to a set location
    """
    with open('./static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  