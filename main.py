import datetime
import PySide6.QtCore
import sys
from domain.classes.app import App
from domain.classes.db_handler import DbHandler
from domain.classes.task import Task
from domain.classes.my_widget import MyWidget

if __name__ == "__main__":
   application = App()
   application.run()