from sklearn.model_selection import train_test_split 

def train_data(x,y,size):
     if size == '':
          x_train, x_test, y_train, y_test = train_test_split(x, y,test_size= 0.2, random_state=5)
     x_train, x_test, y_train, y_test = train_test_split(x, y,test_size= size, random_state=5)
     
     return x_train, x_test, y_train, y_test