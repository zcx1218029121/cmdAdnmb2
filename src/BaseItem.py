class BaseItem:
    def __init__(self, item, index=0):
        self.item = item
        self.ext = self.item["ext"]
        self.img = self.item["img"]
        self.now = self.item["now"]
        self.email = self.item["email"]
        self.admin = self.item["admin"]
        self.content = self.item["content"]
        self.userid = self.item["userid"]
        self.id = self.item["id"]
        self.index = index
        # 回复串 为芦苇娘的不存在当前用户
        if "sage" in self.item:
            self.sage = self.item["sage"]
        if "name" in self.item:
            self.name = self.item["name"]
        if "status" in self.item:
            self.status = self.item["status"]
