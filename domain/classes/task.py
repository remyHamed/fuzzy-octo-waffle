import datetime


class Task:
    def __init__(self, title, creation_date, resume, is_done):
        self.__title = title
        self.__creation_date = creation_date
        self.__resume = resume
        self.__is_done = is_done
    
    def _get_title(self):
        return self.__title
    
    def _set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("bar must be set to an string")
        self.__title = title
    title = property(_get_title, _set_title)


    def _get_creation_date(self):
        return self.__creation_date
    
    def _set_creation_date(self, creation_date):
        if not isinstance(creation_date, datetime.UTC):
            raise TypeError("bar must be set to an datetime")
        self.__creation_date = creation_date
    creation_date = property(_get_creation_date, _set_creation_date)

    
    def _get_resume(self):
        return self.__resume
    
    def _set_resume(self, resume):
        if not isinstance(resume, str):
            raise TypeError("bar must be set to an string")
        self.__resume = resume
    resume = property(_get_resume, _set_resume)


    def _get_is_done(self):
        return self.__is_done
    
    def _set_is_done(self, is_done):
        if not isinstance(is_done, bool):
            raise TypeError("bar must be set to an bool")
        self.__is_done = is_done
    is_done = property(_get_is_done, _set_is_done)

    def __str__(self):
        return "Task is : title : " + self._get_title() + ", resume : " + self._get_resume() + ", is done : " + str(self._get_is_done()) 
