class Board():
    def __init__(self,x,y):
        self.hamleler=[]
        self.lenx=x
        self.leny=y
        self.board=self.make_board(self.lenx,self.leny)
        self.renkBoard=[[" " for a in range(x)] for b in range(y)]
        self.sira="A"
        

    def change_sira(self):
        if self.sira=="A":
            self.sira="B"
        else:
            self.sira="A"


    def update_renk(self):
        for b,line in enumerate(self.board):
            for a,cell in enumerate(line):
                if cell==0 and self.renkBoard[b][a]!=" ":
                    self.renkBoard[b][a]=" "


    def check_win(self):
        cells=[]
        for line in self.renkBoard:
            for cell in line:cells.append(cell)

        a=cells.count("A")
        b=cells.count("B")
        if a==0:
            return "B"
        elif b==0:
            return "A"
        else:
            return "Continue"
                

                
        



    def start(self):
        devam=True
        while devam:
            qes=True
            while qes:
                xy=input("x,y :").split(",")
                x,y=int(xy[0]),int(xy[1])
                if self.ispossible(x,y):
                    myboard.make_move(x,y)
                    
                    
                else:
                    print("yanlis")
                    continue
                if len(self.hamleler)>2:
                    wstate=self.check_win()
                    if wstate!="Continue":
                        #print(wstate)
                        qes=devam=False
                #myboard.printboard()

        #print(f"{wstate} kazandi")
                

    def ispossible(self,x,y):
        return self.renkBoard[y][x]==" " or self.renkBoard[y][x]==self.sira
            
        
        

    def make_board(self,x,y):
        return [[0 for a in range(x)] for b in range(y)]

    def printboard(self):
        print(f"\nIt is {self.sira} turn")
        for i,x in enumerate(self.board):
            print(x+self.renkBoard[i])


    def find_neighbor(self,x,y):
        neighbors=[]
        if x>0:
            neighbors.append((x-1,y))
        if x<self.lenx-1:
            neighbors.append((x+1,y))
        if y>0:
            neighbors.append((x,y-1))
        if y<self.leny-1:
            neighbors.append((x,y+1))
        return neighbors
            
    def find_cap(self,x,y):
        return len(self.find_neighbor(x,y))

    def ismore(self,x,y):
        nl=self.find_cap(x,y)
        if self.board[y][x]>=nl:
            return True
        else:
            return False

    def bloom(self,x,y):  
        neighbors=self.find_neighbor(x,y)
        nl=len(neighbors)
        print(nl)
        self.board[y][x]=self.board[y][x]%nl
        print(self.board[y][x])
        for a in neighbors:
            x,y=a[0],a[1]
            self.board[y][x]+=1
            self.renkBoard[y][x]=self.sira
        #self.update_board()
        
        
        
    def update_board(self):
        if self.check_win()!="Continue":
            print(self.check_win(),"won")
        else:
            mores=[]
            for i,line in enumerate(self.board):
                for j,cell in enumerate(line):
                    if self.ismore(j,i):
                        mores.append((j,i))

            for x in mores:
                self.bloom(x[0],x[1])
            if mores:
                self.update_board()
        
    
        
    
                
        
        
    def make_move(self,x,y):
        self.board[y][x]+=1
        self.renkBoard[y][x]=self.sira
        self.update_board()
        self.change_sira()
        self.update_renk()
        self.hamleler.append((x,y,self.sira))
        
            
        
        
        
if __name__=="__main__":             
    myboard=Board(7,8)
    #myboard.start()
