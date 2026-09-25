import tkinter as tk



def createWindow():
    
    window = tk.Tk()
    window.title("To do list")
    window.geometry("400x550")
    
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
        "Configure",
        lambda e: canvas.itemconfig(canvasWindow, width=e.width)
    )
    
    

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", pady=20, fill="y")
    
    addFrame = tk.Frame(window)
    addFrame.pack(side="bottom", pady=20)
    
    def scroll(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")
        
    canvas.bind(
        "<MouseWheel>", scroll
    )
    
    def addItem():
        item = listText.get()
        if item:
            
            # itemFrame = tk.Frame(listFrame)
            # itemFrame.pack(fill="x", pady=2)
            
            tk.Label(
                listFrame,
                text=f"• {item}",
                anchor="w",
                font=("arial", 15)
            ).pack(fill="x")
            
            # menuButton = tk.Menubutton(
            #     itemFrame,
            #     text="⋮",
            #     font=("arial", 15)
            # )
            # menuButton.pack(side="right")
            
            listText.delete(0, tk.END)
    
    
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