def copy(event):
    event.widget.event_generate("<<Copy>>")

def paste(event):
    event.widget.event_generate("<<Paste>>")



# Designate Height and Width of our app
app_width = 550
app_height = 520

# global variables
cmpt = 1
entries = []