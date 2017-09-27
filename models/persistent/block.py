from orp.database import Model, PrimaryKey
from orp.relationships import Many

class Block(Model):
	primary_key = PrimaryKey('_name')
	def __init__(
		self,
		name,
	):
		self._name = name
		self.expansions = Many(self, '_block')
	@property
	def name(self):
		return self._name