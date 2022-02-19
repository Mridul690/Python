class Railway:
    formtype = "RailwayForm"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApp = Railway()
harrysApp.name="Harry"
harrysApp.train= "Grand Trunk Express"
harrysApp.printdata()