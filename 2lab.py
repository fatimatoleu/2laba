#я использую библиотеку tkinter и функцию tkinter, с помощью которого создаю окно рабочего
#стола
import tkinter as tk 
import sqlite3
from tkinter import ttk, messagebox
#устанавливаю заголовок с помощью данной функции
root = tk.Tk()
root.title("Студенты")
#sq lite позволяет нам подключиться к базе данных, дальше создаем переменную для имени таблицы
connection = sqlite3.connect("students.db")
#дальше по списку запишем все переменные, которые нам понадабиться записать в таблицу базы данных
TABLE_NAME = "students_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COURSE = "student_course"
STUDENT_SPECIALIST = "student_specialist"
STUDENT_EMAIL = "student_email"

connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (" + STUDENT_ID +
            " INTEGER PRIMARY KEY AUTOINCREMENT, " +
            STUDENT_NAME + " TEXT, " + STUDENT_COURSE + " TEXT, " +
            STUDENT_SPECIALIST + " TEXT, " +STUDENT_EMAIL + " INTEGER);" )
#параметры, отправленные в функцию метка, представляют физические свойства обьекта
#устоновила шрифт с помощью функции конфигурация
appLabel = tk.Label(root, text="ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ 7:50-9:45", fg="#800080",width=45)
appLabel.config(font=("Times New Roman", 35))
#положение в окне с помощью функции сетка
appLabel.grid(row=0, columnspan=2, padx=(15,15), pady=(35,0))
#создаем класс для студентов, создаем переменные аналогичнно, 
#и сразу обьявляем переменные в основной функции
class Student:
    studentName = ""
    courseName = ""
    emailnum = 0
    specialist = ""

    def __init__(self, studentName, courseName, emailnum, specialist):
        self.studentName = studentName
        self.courseName = courseName
        self.emailnum = emailnum
        self.specialist = specialist
#создаем метку для студента, используем тот же метод для ярлыка
nameLabel = tk.Label(root, text="Введите имя студента: ", width=45, anchor='w',
                font= ("Times New Roman",12)).grid(row=1, column=0, padx=(15,0),
                pady=(35,0))

courseLabel = tk.Label(root, text="Введите номер курса: ", width=45, anchor='w',
                font= ("Times New Roman",12)).grid(row=2, column=0, padx=(15,0),
                pady=(35,0))

emailnumLabel = tk.Label(root, text="Введите ИИН студента: ", width=45, anchor='w',
                font= ("Times New Roman",12)).grid(row=3, column=0, padx=(15,0),
                pady=(35,0))

specialistLabel = tk.Label(root, text="Введите специальность студента: ", width=45, anchor='w',
                font= ("Times New Roman",12)).grid(row=4, column=0, padx=(15,0),
                pady=(35,0))
#создаем обьекты для входа, определяя с помощью функции сетка
nameEntry = tk.Entry(root, width=35)
nameEntry.grid(row=1, column=1, padx=(0,15), pady=(35,25))

courseEntry = tk.Entry(root, width=35)
courseEntry.grid(row=2, column=1, padx=(0,15), pady=25)

emailEntry = tk.Entry(root, width=35)
emailEntry.grid(row=3, column=1, padx=(0,15), pady= 25)

specialistEntry = tk.Entry(root, width=35)
specialistEntry.grid(row=4, column=1, padx=(0,15), pady=25)
#добавляю глобальные значения
def takeNameInput():
    global nameEntry, courseEntry, emailEntry, specialistEntry
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COURSE,STUDENT_SPECIALIST, STUDENT_EMAIL
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    courseName = courseEntry.get()
    courseEntry.delete(0, tk.END)
    email = int(emailEntry.get())
    emailEntry.delete(0, tk.END)
    specialist = specialistEntry.get()
    specialistEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                    STUDENT_COURSE + ", " + STUDENT_SPECIALIST + ", " +
                    STUDENT_EMAIL + " ) VALUES ( '"
                    + username + "', '" + courseName + "', '" +
                    specialist + "', " + str(email) + " );")
#показываю текст, указывающий, что текст, введеный пользователем, сохранилось в базе данных
    connection.commit()
    messagebox.showinfo("Поздравляем", "Данные успешно загружены.")
#эта функция помогает отображать информацию базы данных на экране 
def destroyRootWindow():
    secondWindow = tk.Tk()
#создаем второе окно
    secondWindow.title("Показать весь список студентов")
#при нажатии кнопки первое окно закроется откроется второе окно
    appLabel = tk.Label(secondWindow, text="ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ 7:50-9:45",
                    fg="#0000ff", width=45)
    appLabel.config(font=("Times New Roman",35))
    appLabel.pack()
#отображать информацию на экране нам поможет функция древовидного представление
    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("bir", "eky", "ush", "tort")

    tree.heading("bir", text="ФИО студента")
    tree.heading("eky", text="Курс студента")
    tree.heading("ush", text="Специальность")
    tree.heading("tort", text="ИИН")
#дальше, вызываем таблицу базы данных
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    i = 0
#создаем переменную, и вставляю информацию в обьект дерево последовательно
    for row in cursor:
        tree.insert('', i, text="Студент " + str(row[0]),
        values=(row[1], row[2],
                row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()
#добавляем кнопки для записи данных, и для списка студентов
button = tk.Button(root, text="Записать данные", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=25)

displayButton = tk.Button(root, text="Показать весь список студентов",
command=lambda : destroyRootWindow())
displayButton.grid(row=10, column=1)
#создаем пустое окно рабочего стола
root.mainloop()