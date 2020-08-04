from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
# pillow (PIL) library used for jpeg image background compatibility with tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
# matplotlib used for creating the graph and Pandas is used to display it
from subprocess import Popen, PIPE, STDOUT


# this is the function called when the "show my results" button is clicked
def resultsButton():
    displayGraph()


# this is the function to update the graph with the output from the jar file
def displayGraph():
    jar_return_values = Popen(
        ['java', '-jar', 'FinalProject.jar', currentAgeInput.get(), grossIncomeInput.get(), savingsInput.get(),
         expensesInput.get()], stdout=PIPE, stderr=STDOUT)
    amounts = ''
    # amounts = '100 200 300 400 500 600 '
    for line in jar_return_values.stdout:
        amounts = line.decode('utf-8')
    yearlyAmounts = str(amounts).split(' ')
    for amount in yearlyAmounts:
        amount.strip()
    graph = Tk()
    graph.title("Retirement Planner")
    yearlyAmounts.pop()
    years = []
    totalSavings = []
    for i in range(len(yearlyAmounts) - 1):
        years.append(2020 + i)
        totalSavings.append(float(yearlyAmounts[i]))
    results.insert(END, yearlyAmounts[len(yearlyAmounts) - 1])
    data = {'Year': [], 'Total Savings': []}

    # Make the data the actual inputs
    data.get('Year').extend(years)
    data.get('Total Savings').extend(totalSavings)

    df = DataFrame(data, columns=['Year', 'Total Savings'])

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, graph)
    line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df = df[['Year', 'Total Savings']].groupby('Year').sum()
    df.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
    ax1.set_title('Retirement Planner')
    graph.mainloop()


root = Tk()
image = Image.open(
    "retirement4.jpg")
# file directory for image
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image=photo_image)
label.pack()
# This is the section of code which creates the main window
root.geometry('870x550')
root.resizable(0, 0)
root.title('Retirement Report')

# Creates label to give user direction
Label(root, text='Please Answer The Questions Below.', bg='gray90', font=('courier', 12, 'normal')).place(x=8, y=9)

# Creates current age label
Label(root, text='Current Age:', bg='gray90', font=('courier', 10, 'normal')).place(x=8, y=49)

# Accepts current age input
currentAgeInput = StringVar()
currentAgeInput = Entry(root, textvariable=currentAgeInput)
currentAgeInput.place(x=113, y=49)

# Creates gross income label
Label(root, text='Annual Gross Income:', bg='gray90', font=('courier', 10, 'normal')).place(x=8, y=89)

# Accepts gross income input
grossIncomeInput = StringVar()
grossIncomeInput = Entry(root, textvariable=grossIncomeInput)
grossIncomeInput.place(x=180, y=89)

# Creates total amount in savings label
Label(root, text='Total Amount In Savings:', bg='gray90', font=('courier', 10, 'normal')).place(x=8, y=129)

# accepts savings input
savingsInput = StringVar()
savingsInput = Entry(root, textvariable=savingsInput)
savingsInput.place(x=210, y=129)

# creates annual expenses label
Label(root, text='Average Annual Expenses:', bg='gray90', font=('courier', 10, 'normal')).place(x=8, y=169)

# accepts annual expenses text entry
expensesInput = StringVar()
expensesInput = Entry(root, textvariable=expensesInput)
expensesInput.place(x=211, y=169)

# creates results label
Label(root, text='Estimated Retirement Age:', bg='gray90', font=('courier', 10, 'normal')).place(x=8, y=269)

# text box for displaying results
results = Text(root, height=2, width=15)
results.place(x=218, y=269)

# creates results button, calls resultsButton() function
Button(root, text='Display My Results!', bg='wheat2', font=('courier', 12, 'bold'),
       command=resultsButton).place(x=8, y=215)

root.mainloop()
