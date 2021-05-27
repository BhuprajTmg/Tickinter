# Tickinter

To set the title we write
top.title('calculator')

we can set the icon by 
top.iconbitmap('path of the file')

i have provided the entry function under variable display.we can change the variable as your wish, we call here the top , here in this code i have use the justyfy= right
as it makes the entry form the right side of the Entry widgit and i used the font attribute for the style and sizes of the input and here bg determines the real colour of the 
display widgets.

i have made this calculator under grid system so after defining widgets we have to define the row and column where the button is to be placed. here pad x and pad y acts as the 
length and the height of the entry widget .

simillarly in the buton widgets, we define the each button with different numbers and signs, and as in entry widget here we define the different attribures as text, font,bg,etc.

in the same way all the buttons of the window is been placed.

already khow that the program is in grid system so after defining widgets we have to define the row and column again and again for as many buttons is assigned in the program.

after assigning the different numbers to the different buttons. the buttons or the program must perform its functions so it could be said to be fulfiled function.
so for the execution of the operation we as define the button_click. as we need the first input value in every operating function since user can execute any of the function defined in the program so we make the f_num as the global variable().

we need to call the function here command lamda is assigned in tikenter. after we assign the command the command is given a spicific number, lik 1 2 3 to 9 

we also need the clear elements or the numbers in the display entry widgit we have the delete function ie. display.delete(0,END). And thus the screen gets cleared

we also need the equal button as after the execution of the any of the opertion we need to get the result which is here given by click_equal. to get the result after the ual to 
button is been pressed. the condition is checked in this function and particular operation operates.

and this is how cide if the calculator works



![database_soft (4)](https://user-images.githubusercontent.com/78782286/119827031-6801c980-bf18-11eb-93c4-c38b955d8f46.jpg)

