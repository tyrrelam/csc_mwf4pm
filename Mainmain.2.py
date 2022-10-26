#Python Drawing application
#takes a filename form teh command line, reads file
#and processess the file contents by excuting the
#commands listed in file.
#The commands will be instructions on what to draw
#on the screen

#sprint -  weekly objectives for fixes and new features
import turtle

WELCOME = "Python Drawing Application"

def initialize_turtle():
    return turtle.Turtle()

def main():
    print(WELCOME)
    ryan_turtle=initialize_turtle()
    ryan_turtle.forward(100)
    ryan_turtle.left(90)
    ryan_turtle.forward(100)
    turtle.Screen().exitonclick()

if  __name__=='__main__':
    main()
    
