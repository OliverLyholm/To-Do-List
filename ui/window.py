import tkinter as tk
from functions.functions import loadTasks, saveTasks




def createWindow():
    
    window = tk.Tk()
    window.title("To do list")
    window.geometry("400x550")
    
    tasks = loadTasks()
    
    scrollFrame = tk.Frame(window)
    scrollFrame.pack(padx=20, pady=20, fill="both", expand=True)
    
    canvas = tk.Canvas(scrollFrame)
    scrollbar = tk.Scrollbar(
        scrollFrame,
        orient="vertical",
        command=canvas.yview
    )
    
    

    listFrame = tk.Frame(canvas)
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvasWindow = canvas.create_window(
        (0, 0),
        window=listFrame,
        anchor="nw"
    )
    
    listFrame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.bind(
        "<Configure>",
        lambda e: canvas.itemconfig(
            canvasWindow,
            width=e.width
        )
    )
        
    

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", pady=20, fill="y")
    
    addFrame = tk.Frame(window)
    addFrame.pack(side="bottom", pady=20)
    
    def scroll(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")
        
    canvas.bind_all(
        "<MouseWheel>", scroll
    )
    
    def deleteTask(task, itemFrame):
        tasks.remove(task)
        saveTasks(tasks)
        itemFrame.destroy()
        
    def toggleDone(task, label, menu):
        task["done"] = not task["done"]
        saveTasks(tasks)

        if task["done"]:
            label.config(fg="gray")
            menu.entryconfig(0, label="Mark as undone")
        else:
            label.config(fg="black")
            menu.entryconfig(0, label="Mark as done")

    def editTask(task, label, itemFrame):
        currentText = task["text"]
        
        label.pack_forget()
        
        editEntry = tk.Entry(
            itemFrame,
            font=("arial", 15)
        )
        
        editEntry.pack(side="left", fill="x", expand=True)
        
        editEntry.insert(0, currentText)
        editEntry.focus()
        
        def saveEdit(event=None):
            newText = editEntry.get().strip()
            
            if newText:
                task["text"] = newText
                saveTasks(tasks)
                
                editEntry.destroy()
                
                
                label.config(text=f"• {task['text']}")
                
                
                if task["done"]:
                    label.config(fg="gray")
                    
                label.pack(side="left", fill="x", expand=True)
                    
        editEntry.bind("<Return>", saveEdit)
        
        
    
    
    
    
    def addItem():
        item = listText.get()
        if item:
            
            task = {
                "text": item,
                "done": False
            }
            tasks.append(task)
            saveTasks(tasks)
            
            createTask(task)
            
            listText.delete(0, tk.END)
            
    def createTask(task):
        itemFrame = tk.Frame(listFrame)
        itemFrame.pack(fill="x", pady=2)
                    
        label = tk.Label(
            itemFrame,
            text=f"• {task['text']}",
            anchor="w",
            font=("arial", 15)
        )
        label.pack(side="left", fill="x", expand=True)
        
        if task["done"]:
            label.config(fg="gray")
                    
        menuButton = tk.Menubutton(
            itemFrame,
            text="⋮",
            font=("arial", 20)
        )
        menuButton.pack(side="right")
        
        reoderButtonsFrame = tk.Frame(itemFrame)
        reoderButtonsFrame.pack()
        
        buttonUp = tk.Button(
            reoderButtonsFrame,
            text="▲",
            font=("arial", 5)
        )
        buttonUp.grid(row=1, column=1)
        
        buttonDown = tk.Button(
            reoderButtonsFrame,
            text="▼",
            font=("arial", 5)
        )
        buttonDown.grid(row=2, column=1)
        
        
                    
        menu = tk.Menu(menuButton, tearoff=0)
        
        menu.add_command(
            label="Mark as done" if not task["done"] else "Mark as undone",
            command=lambda: toggleDone(task, label, menu)
    )

        menu.add_command(
            label="Edit",
            command=lambda: editTask(task, label, itemFrame)
        )
        menu.add_command(
            label="Delete",
            command=lambda: deleteTask(task, itemFrame)
        )
                    
                    
                    
        menuButton.config(menu=menu)
                    
    
    for task in tasks:
        createTask(task)
    
    
    listText = tk.Entry(
        addFrame,
        width=20,
        font=("Arial", 15)
        
        )
    listText.pack(pady=5, ipady=5)
    
    addButton = tk.Button(
        addFrame,
        text="Add",
        width=20,
        font=("Arial", 15),
        command=lambda: addItem()
    )
    addButton.pack(ipady=5)
    
    
    
    
    return window