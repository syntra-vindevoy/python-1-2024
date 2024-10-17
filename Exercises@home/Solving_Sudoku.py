# URL of sudoku: https://www.google.com/search?sca_esv=d5db76981dc197ce&sxsrf=ADLYWILPW2DT6F968ogZ4YZDHMo-vCLqkQ:1729073607646&q=sudoku+online&udm=2&fbs=AEQNm0A6bwEop21ehxKWq5cj-cHaxUZOSO72WoU7KkLyB7O1BLPwnsqUQoH7cGimAlpV3w1-yBjpg35HpX2ySbUvN7X4Ep2f6m0UUZhJIG1kvg_E7jUVBlzicWBMuvNcPdpKn0LwYc7dDHjUFQu2OkeWKh6V3IK2nmA_nELC2Nh2AeXxi2C2VGw&sa=X&sqi=2&ved=2ahUKEwi6lbKR1ZKJAxU9dqQEHU4GMQwQtKgLegQIGBAB&biw=1536&bih=730&dpr=1.25#vhid=YMRf9mZysi7qbM&vssid=mosaic
import numpy as np
SUDOKU_PUZZLE = [
    [1, 2, 0, 2, 2, 0, 0, 2, 1],
    [0, 0, 3, 0, 3, 4, 4, 0, 0],
    [1, 0, 0, 4, 0, 3, 0, 4, 0],
    [2, 4, 0, 0, 2, 0, 0, 0, 1],
    [0, 0, 3, 0, 3, 3, 3, 0, 2],
    [2, 0, 0, 3, 0, 0, 2, 0, 0],
    [1, 0, 1, 2, 0, 0, 3, 4, 0],
    [3, 0, 0, 2, 0, 2, 2, 0, 0],
    [0, 0, 3, 0, 1, 0, 1, 2, 2]
]

#print(np.matrix(SUDOKU_PUZZLE))

def sudoku_solver():

print(SUDOKU_PUZZLE[1:5])