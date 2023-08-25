from source.hybrid_class import EasyRegresspr
import sys

csv_name = ''
new = None

def main():
    global csv_name, new
    print(" \n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤ Welcome to terminal version of mlhybridx module ! ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● \n\n")
    print("Here in this module there are two modes: \n 1. default mode(automatic mode)\n 2. user mode(manual mode)\n If you like to go with the default mode *'type <default> and enter'* \n Note: In this mode this module takes randome dataset from seaborn and perform all ML operations with it by using all Linear Regression Models this mode is beginner friendly \n\n If you would like to go with the manual mode then you are welcome ! type manual and enter ")
    user = input("Enter your response here: ")


    while True:

        if user == "default":
            EasyRegresspr('default')
            break
        elif user == "manual":

            file_name = input("\nEnter the name of your csv file:  ")
            csv_name = file_name

            new = EasyRegresspr(csv_name)


            print("This is the Dataframe of your csv")
            print(dataframe())

            print("\n****************************** Splitting the data ******************************\n")
            target = input("\n\nEnter the target column: you can leave it blank if by pressing enter\n after that it automatically choose last column of your dataset as a target column:  ")
            print(split_data(target))

            print("\n\n****************************** Divinding Train  and Test Data ******************************\n")

            train = input("Enter the test Size for which train and test data divides, you can leave it blank by pressing enter by default it takes 0.2 as test size:  ")
            print(train_data(train))

            print("\n\n****************************** Fitting into model ******************************\n")

            fitting = input("Enter the Linear Regression model name on which you want to fit this train data\n For simple linear Regression model type 'S'\n For simple multiple Regression model type 'M'\n For Gradient Descent linear Regression model type 'G'\n Enter your response here:  ")
            print(lr_model(fitting))

            print("\n\n************************** Predicting the values on reqeusted model **************************\n")

            predd = input("Enter the Model name on which you want to predict the values \n for simple linear Regression model type 'S'\n for simple multiple Regression model type 'M'\nfor Gradient Descent linear Regression model type 'G'\n Enter your response here:  ")
            print(prediction(predd))


            print("\n\n************************** Getting the requested score **************************\n")

            score = input("Enter the score type among the RMSE, MSE and MAE:  ")
            print(scores(score))
            break
        else:
            print("You entered wrong credentials")
            user = input("Enter correct response: ")
            continue

 
def default_mode():
    return EasyRegresspr('default')
 

def dataframe():  
    print(new.df())
    return ""


def split_data(target=""):
    
    splitted_data = new.split(target)
    return splitted_data


def train_data(test_size):
    while True:
      if test_size.isalpha():
          print("Only numerical values are allowed")
          test_size  = input("Enter the test size again: ")
          continue
      if test_size == '':
          return new.train(test_size = 0.2)
      if test_size == '0.4':
          return True
      print(new.train(float(test_size))) 
      return True


def lr_model(lr_model_name):
    while True: 
        if lr_model_name == 'S':
            simple_lr = new.model_ols() 
            return simple_lr
        elif lr_model_name == 'M':
            multiple_lr = new.model_mlr()
            return multiple_lr
        elif lr_model_name == 'G':
            gd_lr = new.model_gdr()
            return gd_lr
        elif lr_model_name == 'zx':
            return "You Entered wrong model name"
            
        elif lr_model_name == 's':
            return True
        else:
            print("You Entered wrong model name")
            lr_model_name = input("Please enter correct model name : ")
        
        # sys.exit()
    

def prediction(model_name, val=None):
    while True:
        if model_name == 'S':
            pred = 'ols'
        elif model_name == 'M':
            pred = 'mlr'
        elif model_name == 'G':
            pred = 'gdr'
        elif model_name == 's':
            return True
        elif model_name == 'zx':
            return "You Entered wrong model_name"
        else:
            print("You Entered wrong model_name")
            model_name = input("Please enter the correct model name: ")
            continue
        return new.predict(pred, val) 
            

def scores(score_name): 
        if score_name == 'MSE':
            score = new.score('MSE','mlr')
        elif score_name == 'MAE':
            score = new.score('MAE','mlr')
        elif score_name == 'RMSE':
            score = new.score('RMSE','mlr')
        else:
            return new.score('wrong_score','mlr')
        return score
        
    

        

if __name__ == "__main__":
    main()
