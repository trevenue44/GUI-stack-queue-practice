import sys
from PyQt5.QtGui import QCursor
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

# Stack class
class Stack():
    def __init__(self):
        self.__stack_array = [] # private list to store values
    
    def push(self, value):
        self.__stack_array.append(value)

    def pop(self):
        if not self.is_empty():
            return self.__stack_array.pop()
        else:
            print("*Stack is empty*")

    def peek(self):
        return self.__stack_array[-1]

    def is_empty(self):
        if len(self.__stack_array) > 0:
            return False
        else:
            return True


# Queue Class
class Queue():
    def __init__(self):
        self.__queue_array = [] # private list to store values
    
    def insert(self, value):
        self.__queue_array.append(value)

    def remove(self):
        if not self.is_empty():
            return self.__queue_array.pop(0)
        else:
            print("*Queue is empty*")

    def peekFront(self):
        return self.__queue_array[0]

    def is_empty(self):
        if len(self.__queue_array) > 0:
            return False
        else:
            return True


# creating a class that inherits the features of the QMainWindow
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        # Setting initial window properties
        self.setGeometry(100, 100, 1000, 350)
        self.setWindowTitle("Stacks and Queues")
        self.setStyleSheet("background: rgba(8, 20, 25, 0.8);")
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.widgets = {"logo": [], "button": [], "text_boxes": []} # creating a way to store all widgets
        self.initUI()

    def initUI(self):
        # PART I: STACKS
        text_box = QLineEdit(self)
        text_box.resize(300, 80)
        text_box.setStyleSheet("background-color: rgba(150, 150, 150); color: rgba(25, 30, 80); font-size: 70px")
        self.widgets["text_boxes"].append(text_box)
        self.grid.addWidget(self.widgets["text_boxes"][-1], 0, 0)
        
        # creating a button for reversiing all
        reverse_button = self.create_button("Reverse All")
        # putting the reverse button into the widget dictionay
        self.widgets["button"].append(reverse_button)
        # putting the button onto the grid (displaying it)
        self.grid.addWidget(self.widgets["button"][-1], 1, 0)

        self.widgets["button"][-1].clicked.connect(self.reverse_clicked)


        # creating a button for reversing caps
        reverse_caps = self.create_button("Reverse CAPS")
        # putting the reverse caps button into the widget dictionay
        self.widgets["button"].append(reverse_caps)
        # putting the button onto the grid (displaying it)
        self.grid.addWidget(self.widgets["button"][-1], 2, 0)

        self.widgets["button"][-1].clicked.connect(self.reverse_caps_clicked)


        # PART II: QUEUES
        text_box = QLineEdit(self)
        text_box.resize(300, 80)
        text_box.setStyleSheet("background-color: rgba(150, 150, 150); color: rgba(25, 30, 80); font-size: 70px")
        self.widgets["text_boxes"].append(text_box)
        self.grid.addWidget(self.widgets["text_boxes"][-1], 0, 1)

        # creating a button for storing input
        take_input_button = self.create_button("Take Input")
        # putting the bring button into the widget dictionay
        self.widgets["button"].append(take_input_button)
        # putting the button onto the grid (displaying it)
        self.grid.addWidget(self.widgets["button"][-1], 0, 2)

        self.widgets["button"][-1].clicked.connect(self.take_input)

    def take_input(self):
        # taking what the user inputs
        text = self.widgets["text_boxes"][-1].text()
        
        my_queue = Queue()

        if " " in text.strip():
            iterable = text.strip().split(" ")
        else:
            iterable = text.strip()

        # adding each element to the stack using a for loop
        if isinstance(iterable, list):
            for letter in iterable:
                my_queue.insert(letter+" ")
        else:
            for letter in iterable:
                my_queue.insert(letter)
        
        self.do_with_queue(my_queue)
        self.widgets["text_boxes"][-1].setText("")
    
    def do_with_queue(self, queue): 
        # creating a button for bringing one
        bring_one_button = self.create_button("Bring One")
        # putting the bring button into the widget dictionay
        self.widgets["button"].append(bring_one_button)
        # putting the button onto the grid (displaying it)
        self.grid.addWidget(self.widgets["button"][-1], 1, 1)

        self.widgets["button"][-1].clicked.connect(lambda: self.bring_one_clicked(queue))


        # creating a button for bringing only caps
        bring_caps_button = self.create_button("Bring CAPS")
        # putting the bring caps button into the widget dictionay
        self.widgets["button"].append(bring_caps_button)
        # putting the button onto the grid (displaying it)
        self.grid.addWidget(self.widgets["button"][-1], 2, 1)

        self.widgets["button"][-1].clicked.connect(lambda: self.bring_caps_clicked(queue))

    def bring_one_clicked(self, q):
        if not q.is_empty():
            result = self.widgets["text_boxes"][-1].text()
            result += q.remove()
            self.widgets["text_boxes"][-1].setText(result)


    def bring_caps_clicked(self, q):
        if not q.is_empty():
            result = self.widgets["text_boxes"][-1].text()
            result += ''.join(x for x in q.remove() if x.isupper())
            self.widgets["text_boxes"][-1].setText(result)

    def reverse_clicked(self):
        # taking what the user inputs
        text = self.widgets["text_boxes"][-2].text()
        
        my_stack = Stack()

        if " " in text.strip():
            iterable = text.strip().split(" ")
        else:
            iterable = text.strip()

        # adding each element to the stack using a for loop
        if isinstance(iterable, list):
            for letter in iterable:
                my_stack.push(letter+" ")
        else:
            for letter in iterable:
                my_stack.push(letter)            

        # popping out all the elements of the stack
        reversed = ''
        while not my_stack.is_empty():
            reversed += my_stack.pop()
        self.widgets["text_boxes"][-2].setText(reversed.strip())        
        

    def reverse_caps_clicked(self):
        # taking what the user inputs
        text = self.widgets["text_boxes"][-2].text()
        
        my_stack = Stack()

        if " " in text.strip():
            iterable = text.strip().split(" ")
        else:
            iterable = text.strip()

        # adding each element to the stack using a for loop
        if isinstance(iterable, list):
            for letter in iterable:
                my_stack.push(letter+" ")
        else:
            for letter in iterable:
                my_stack.push(letter)            

        # popping out all the elements of the stack
        reversed = ''
        while not my_stack.is_empty():
            reversed += ''.join(x for x in my_stack.pop() if x.isupper())
        self.widgets["text_boxes"][-2].setText(reversed.strip())        
        

    def create_button(self, text):
        # button
        button = QtWidgets.QPushButton(text)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("*{border: 1px solid rgba(0, 200, 240, 0.8);" +
                        "border-radius: 20px;" + 
                        "font-size: 35px;" + 
                        "color: white;" + 
                        "padding: 12px 0;" + 
                        "margin: 8px 10px}" +
                        "*:hover{background: rgba(0, 200, 240, 0.8);}" + 
                        "*:pressed{background: rgba(200, 200, 240);}")
        return button


# a function that create windows
def window():
    app = QApplication(sys.argv)
    # creating an instance of the MyWindow class
    win = MyWindow()
    # showing the window
    win.show()
    sys.exit(app.exec())

window()
