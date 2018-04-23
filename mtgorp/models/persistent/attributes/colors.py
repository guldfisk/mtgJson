import typing as t
from enum import Enum


class Color(Enum):
	WHITE = 'W', 0
	BLUE = 'U', 1
	BLACK = 'B', 2
	RED = 'R', 3
	GREEN = 'G', 4
	
	@property
	def code(self):
		return '{{{}}}'.format(self.value)
	
	def __lt__(self, other):
		return self.position < other.position
	
	def __new__(cls, code, position):
		obj = object.__new__(cls)
		obj._value_ = code
		obj.position = position
		return obj


def color_set_sort_value(color_set: t.AbstractSet[Color]):
	return (
		sum(1<<c.position for c in color_set)
	)


def test():
	print(isinstance(Color.WHITE, Color))


if __name__ == '__main__':
	test()