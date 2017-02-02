class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
         items = self.items
         items.append(item)

    def getClassiness(self):
        classiness_score = 0
        items = self.items
        scores = {
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5
        }
        for item in items:
            if item in scores:
                classiness_score += scores[item]
        return classiness_score



me = Classy()

me.addItem('tophat')
print me.getClassiness()

me.addItem('bowtie')
me.addItem("jacket")
me.addItem("monocle")
print me.getClassiness()

me.addItem("bowtie")
print me.getClassiness()
