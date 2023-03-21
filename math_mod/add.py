class Addition:
    def __init__(self,*args):
        self.num = args

    def addition(self):
        res = self.num[0]
        for i in self.num[1:]:
            res += i
        return res
