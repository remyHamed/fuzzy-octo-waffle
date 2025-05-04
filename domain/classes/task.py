import datetime


class Task:
    def __init__(self,id :int = None, title:str = "", creation_date :datetime = datetime.datetime.now(), resume:str = "", is_done :bool = False):
        self._id = id
        self.__title = title
        self.__creation_date = creation_date
        self.__resume = resume
        self.__is_done = is_done

    def _get_id(self) -> int:
        return self._id
    
    def _set_id(self, id :int) -> None:
        if not isinstance(id, int):
            raise TypeError("bar must be set to an string")
        self._id = id
    id = property(_get_id, _set_id)

    
    def _get_title(self) -> str:
        return self.__title
    
    def _set_title(self, title) -> None:
        if not isinstance(title, str):
            raise TypeError("bar must be set to an string")
        self.__title = title
    title = property(_get_title, _set_title)


    def _get_creation_date(self) -> datetime:
        return self.__creation_date
    
    def _set_creation_date(self, creation_date: datetime) ->  None:
        if not isinstance(creation_date, datetime):
            raise TypeError("bar must be set to an datetime")
        self.__creation_date = creation_date
    creation_date = property(_get_creation_date, _set_creation_date)

    
    def _get_resume(self) -> str:
        return self.__resume
    
    def _set_resume(self, resume : str) -> str:
        if not isinstance(resume, str):
            raise TypeError("bar must be set to an string")
        self.__resume = resume
    resume = property(_get_resume, _set_resume)


    def _get_is_done(self) -> bool:
        return self.__is_done
    
    def _set_is_done(self, is_done : bool) -> None:
        if not isinstance(is_done, bool):
            raise TypeError("bar must be set to an bool")
        self.__is_done = is_done
    is_done = property(_get_is_done, _set_is_done)

    def __str__(self):
        return "Task -> id: " + str(self._get_id()) + " title : " + self._get_title() + ", resume : " + self._get_resume() + ", is done : " + str(self._get_is_done()) 


