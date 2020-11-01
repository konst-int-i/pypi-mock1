import pandas as pd


__all__ = [
	"Mock"
	]

class Mock(object): 
	def __init__(self): 
		pass

	def print(self) -> None: 
		print("This is a mock package")



if __name__ ==  "__main__": 

	mock = Mock()
	mock.print()