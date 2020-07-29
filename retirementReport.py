from tkinter import *
from PIL import Image, ImageTk
# pillow (PIL) library used for jpeg image background compatibility with tkinter


# this is the function called when the "show my results" button is clicked
def resultsButton():
    # results.insert() future use
    print('clicked')


root = Tk()
image = Image.open("Project/images/retirement4.jpg")
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image=photo_image)
label.pack()
# This is the section of code which creates the main window
root.geometry('800x500')
# root.resizable(0, 0)
root.configure(background='#7FFFD4')
root.title('Retirement Report')

# Creates label to give user direction
Label(root, text='Please Answer The Questions Below.', bg='#7FFFD4', font=('courier', 12, 'normal')).place(x=8, y=9)

# Creates current age label
Label(root, text='Current Age:', bg='#7FFFD4', font=('courier', 10, 'normal')).place(x=8, y=39)

# Accepts current age input
currentAgeInput = StringVar()
currentAgeInput = Entry(root, textvariable=currentAgeInput)
currentAgeInput.place(x=118, y=39)

# Creates goal retirement age label
Label(root, text='Goal Retirement Age:', bg='#7FFFD4', font=('courier', 10, 'normal')).place(x=8, y=69)

# Accepts retirement age input
retirementAgeInput = StringVar()
retirementAgeInput = Entry(root, textvariable=retirementAgeInput)
retirementAgeInput.place(x=188, y=69)

# Creates gross income label
Label(root, text='Annual Gross Income:', bg='#7FFFD4', font=('courier', 10, 'normal')).place(x=8, y=99)

# Accepts gross income input
grossIncomeInput = StringVar()
grossIncomeInput = Entry(root, textvariable=grossIncomeInput)
grossIncomeInput.place(x=188, y=99)

# Creates total amount in savings label
Label(root, text='Total Amount In Savings:', bg='#7FFFD4', font=('courier', 10, 'normal')).place(x=8, y=129)

# accepts savings input
savingsInput = StringVar()
savingsInput = Entry(root, textvariable=savingsInput)
savingsInput.place(x=218, y=129)

# creates annual expenses label
Label(root, text='Average Annual Expenses:', bg='#7FFFD4', font=('courier', 10, 'normal')).place(x=8, y=159)

# accepts annual expenses text entry
expensesInput = StringVar()
expensesInput = Entry(root, textvariable=expensesInput)
expensesInput.place(x=218, y=159)

# creates results label
Label(root, text='Results:', bg='#7FFFD4', font=('courier', 12, 'normal')).place(x=8, y=261)

# text box for displaying results
results = Text(root, height=7, width=20)
results.place(x=98, y=269)

# creates results button, calls resultsButton() function
Button(root, text='Display My Results!', bg='#FAEBD7', font=('courier', 12, 'normal'),
       command=resultsButton).place(x=8, y=199)

root.mainloop()
