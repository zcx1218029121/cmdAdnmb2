from BaseItem import *


class StringInfo(BaseItem):
    def __init__(self, item, index=0):
        super().__init__(item, index=index)
        self.replys = []
        for temp in self.item["replys"]:
            self.replys.append(BaseItem(temp))
