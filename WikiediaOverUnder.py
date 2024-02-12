import requests
from bs4 import BeautifulSoup
import random
from tkinter import *

def grab_random_WikiArticle():
    reponse = requests.get( url = "https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(reponse.text, 'html.parser')
    title = soup.find(id="firstHeading").text
    article_text = soup.find('div', {'id': 'mw-content-text'}).text
    article_length = len(article_text.split())

    #Average Wikipedia English article is 668 words 
    random_length = random.randint(500,1200)
    
    return title, article_length, random_length
    

def save_random_Article():
    article_Title, article_Length, random_Length = grab_random_WikiArticle()

    return article_Title, article_Length, random_Length


def OverButton(article_Title, article_Length, random_Length):
    if(article_Length > random_Length):
        print("")
        print(f"### For {article_Title} ###")
        print(f"Over/Under is: {random_Length}")
        print(f"The actual word count is: {article_Length}")
        print("Your guess over is correct!")
        print("")
      
    else:
        print("")
        print(f"### For {article_Title} ###")
        print(f"Over/Under is: {random_Length}")
        print(f"The actual word count is: {article_Length}")
        print("Your guess over is incorrect!")
        print("")
    

def UnderButton(article_Title, article_Length, random_Length):
    if(article_Length < random_Length):
        print("")
        print(f"### For {article_Title} ###")
        print(f"Over/Under is: {random_Length}")
        print(f"The actual word count is: {article_Length}")
        print("Your guess under is correct!")
        print("")
        
    else:
        print("")
        print(f"### For {article_Title} ###")
        print(f"Over/Under is: {random_Length}")
        print(f"The actual word count is: {article_Length}")
        print("Your guess under is incorrect!")
        print("")

def gui_OverUnder():    
    root = Tk()
    root.geometry('550x250')
    
    article_Title, article_Length, random_Length = save_random_Article()

    root.title("Wikipedia Over/Under")

    #TITLE
    title = Label(root, text=f"The Wikipedia article is:",font=('Times New Roman', 15))
    title.pack()


    
    #CONTENT
    wiki_title = Label(root, text=f"{article_Title}",font=('Times New Roman', 15, 'bold'))
    wiki_title.pack()
    

    randomL = Label(root, text=f"Is the article over or under {random_Length} words?",
                    font=('Times New Roman', 15))
    randomL.pack()

    #BUTTONS
    over_Button = Button(root, text="Over!", font=('Times New Roman', 15, ),command= lambda:OverButton(article_Title, article_Length, random_Length))
    over_Button.pack()
    
    under_Button = Button(root, text="Under!", font=('Times New Roman', 15), command= lambda:UnderButton(article_Title, article_Length, random_Length))
    under_Button.pack()

    #REFRESH 
    def refresh_gui():
        root.destroy()  
        gui_OverUnder()

    
    refresh_button = Button(root, text="Refresh", command=refresh_gui,fg='blue')
    refresh_button.pack()
   
    root.mainloop()
    
gui_OverUnder()

