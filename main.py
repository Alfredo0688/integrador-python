import tkinter as tk
from vista.vista import Frame
#from include.menu import barrita_menu

def  main():  
    ventana = tk.Tk()
    ventana.title('Paseador de michis')  
    ventana.iconbitmap('img/cat.ico')
    ventana.resizable(0,0)

    #barrita_menu(ventana)
    app = Frame(root= ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()