class Flipkart:
    products={'laptop':80000,
              'phone':50000,
              'earphones':900,
              'bags':300}
    @classmethod
    def showProducts(cls):
        print(cls.products)

    def register(self,name,phno):
        self.username = name
        self.phonenumber = phno
        print(f'Welcome to flipkart {self.username},shop now!!!')


    @staticmethod
    def discount():
        print("Hey all,10% discount is going on ,show now!!!!!")

saniya=Flipkart()
saniya.register('saniya','987654321')
saniya.discount()
saniya.showProducts()




rina=Flipkart()
rina.register('rina','987654321')

tina=Flipkart()
tina.register('tina','987654321')
