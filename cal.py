import tkinter as tk

def calculate():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    operator = entry_operator.get()
    result = 0
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    
    entry_result.delete(0, tk.END)
    entry_result.insert(0, str(result))

root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")

label_num1 = tk.Label(root, text="Number 1")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_operator = tk.Label(root, text="Operator")
label_operator.grid(row=1, column=0)

entry_operator = tk.Entry(root)
entry_operator.grid(row=1, column=1)

label_num2 = tk.Label(root, text="Number 2")
label_num2.grid(row=2, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1)

label_result = tk.Label(root, text="Result")
label_result.grid(row=3, column=0)

entry_result = tk.Entry(root)
entry_result.grid(row=3, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2)

root.mainloop()
