
class Array3D:
    
    def __init__(self,rows,cols,depth):
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        self.__data = []
        for d in range(self.__depth):
            aux=[]
            for r in range(self.__rows):
                aux2=[]
                for c in range(self.__cols):
                    aux2.append(None)
                aux.append(aux2)
            self.__data.append(aux)
            
    def get_num_rows(self):
        return self.__rows
    
    def get_num_cols(self):
        return self.__cols
    
    def get_num_depth(self):
        return self.__depth
    
    def set_item(self,row,col,depth,value):
        self.__data[depth][row][col] = value
        
    def get_item(self,row,col,depth):
        return self.__data[depth][row][col]
    
    def clearing(self,value):
        for d in range(self.__depth):
            for r in range(self.__rows):
                for c in range(self.__cols):
                    self.set_item(r,c,d,value)
        
                
    def to_string(self):
        print(self.__data)
        
