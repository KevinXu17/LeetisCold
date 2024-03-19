"""
ensures that only one object of its kind exists and provides a single point of access
to it for any other code.

"""
import threading


# 2
class SingletonClass(object):
    def __new__(cls): # new before init
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()



# from geeksforgeeks


# Thread Safe
# Medium https://medium.com/analytics-vidhya/how-to-create-a-thread-safe-singleton-class-in-python-822e1170a7f6
class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance



