from mainwindow import MainWindow


if __name__ == "__main__":
    window = MainWindow()

    window.title("Chomem")
    window.geometry("1280x720")
    window.config(bg="white")  

    window.mainloop()
