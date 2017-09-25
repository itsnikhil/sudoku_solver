Sudoku Solver!

Objective: A script to solve sudoku from just an image!

Update: It is now working, Final working scripts are inside Solution folder (https://github.com/itsnikhil/sudoku_solver/tree/master/Solution)

How to run?
1) Install required libraries -<br />
  a) OpenCV (http://docs.opencv.org/3.2.0/d5/de5/tutorial_py_setup_in_windows.html)<br />
  b) pip install Pillow<br />
  c) Numpy http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
2) Clone this repo (https://github.com/itsnikhil/sudoku_solver.git)
3) Look for Solution folder
4) Run 'TrainAndTest.py' in terminal/cmd

How it works?
1) First 'sudoku.png' is converted to binary colors (Black and White) #'opencv.py' does this thersholding
2) That binary image is chopped into 9x9 pieces #'slice_img.py' does this slicing
3) Each digit is individually read using KNN character recogination algo #<mark>'TranAndTest.py'</mark> does this and below
4) All the character read is stored in 'data.txt'
5) Characters from 'data.txt' is then read to create Sudoku board which is then solved using Sudoku solving algo #'suduko_solver.py' does all this
6) All the files created get removed in the end!
