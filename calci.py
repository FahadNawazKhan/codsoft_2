import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

font_style = ("Helvetica Neue", 18)

entry_num1 = tk.Entry(root, width=15, font=font_style)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=15, font=font_style)
entry_num2.grid(row=0, column=1, padx=10, pady=10)


label_operation = tk.Label(root, text="Operation:", font=font_style)
label_operation.grid(row=1, column=0, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
dropdown_operation = tk.OptionMenu(root, operation_var, *operation_choices)
dropdown_operation.config(font=font_style)
dropdown_operation.grid(row=1, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate", command=calculate, font=font_style)
button_calculate.grid(row=2, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ", font=font_style)
label_result.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
