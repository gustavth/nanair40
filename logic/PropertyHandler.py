from baseClasses.Property import Property
from dataControl.PropertyController import PropertyController
from typing import Any


class PropertyHandler:
    def __init__(self) -> None:
        self.propertyControl = PropertyController()
        self.property = Property()

    def addProperty(self, property: 'Property') -> bool:
        propertyJson = self.property.toJSON(property)
        self.propertyControl.appendIntoFile(propertyJson)
        return True


    def editProperty(self, entry: str, entryValue: Any, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.property) for kwarg in kwargs):
            return False
        self.propertyControl.changeOneEntry(entry, entryValue, **kwargs)
        return True


    def listProperties(self, **kwargs) -> list['Property']:
        if any(kwarg not in vars(self.property) for kwarg in kwargs):
            return []

        properties: list['Property'] = self.propertyControl.readFile()
        if not len(kwargs):
            return properties

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(properties)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) not in str(properties[i].__dict__[k]):
                    del properties[i]


        return properties
