\ Model Sudoku
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 
Subject To
 R0: Numero[0,0,0] + Numero[1,0,0] + Numero[2,0,0] + Numero[3,0,0]
   + Numero[4,0,0] + Numero[5,0,0] + Numero[6,0,0] + Numero[7,0,0]
   + Numero[8,0,0] = 1
 R1: Numero[0,0,1] + Numero[1,0,1] + Numero[2,0,1] + Numero[3,0,1]
   + Numero[4,0,1] + Numero[5,0,1] + Numero[6,0,1] + Numero[7,0,1]
   + Numero[8,0,1] = 1
 R2: Numero[0,0,2] + Numero[1,0,2] + Numero[2,0,2] + Numero[3,0,2]
   + Numero[4,0,2] + Numero[5,0,2] + Numero[6,0,2] + Numero[7,0,2]
   + Numero[8,0,2] = 1
 R3: Numero[0,0,3] + Numero[1,0,3] + Numero[2,0,3] + Numero[3,0,3]
   + Numero[4,0,3] + Numero[5,0,3] + Numero[6,0,3] + Numero[7,0,3]
   + Numero[8,0,3] = 1
 R4: Numero[0,0,4] + Numero[1,0,4] + Numero[2,0,4] + Numero[3,0,4]
   + Numero[4,0,4] + Numero[5,0,4] + Numero[6,0,4] + Numero[7,0,4]
   + Numero[8,0,4] = 1
 R5: Numero[0,0,5] + Numero[1,0,5] + Numero[2,0,5] + Numero[3,0,5]
   + Numero[4,0,5] + Numero[5,0,5] + Numero[6,0,5] + Numero[7,0,5]
   + Numero[8,0,5] = 1
 R6: Numero[0,0,6] + Numero[1,0,6] + Numero[2,0,6] + Numero[3,0,6]
   + Numero[4,0,6] + Numero[5,0,6] + Numero[6,0,6] + Numero[7,0,6]
   + Numero[8,0,6] = 1
 R7: Numero[0,0,7] + Numero[1,0,7] + Numero[2,0,7] + Numero[3,0,7]
   + Numero[4,0,7] + Numero[5,0,7] + Numero[6,0,7] + Numero[7,0,7]
   + Numero[8,0,7] = 1
 R8: Numero[0,0,8] + Numero[1,0,8] + Numero[2,0,8] + Numero[3,0,8]
   + Numero[4,0,8] + Numero[5,0,8] + Numero[6,0,8] + Numero[7,0,8]
   + Numero[8,0,8] = 1
 R9: Numero[0,1,0] + Numero[1,1,0] + Numero[2,1,0] + Numero[3,1,0]
   + Numero[4,1,0] + Numero[5,1,0] + Numero[6,1,0] + Numero[7,1,0]
   + Numero[8,1,0] = 1
 R10: Numero[0,1,1] + Numero[1,1,1] + Numero[2,1,1] + Numero[3,1,1]
   + Numero[4,1,1] + Numero[5,1,1] + Numero[6,1,1] + Numero[7,1,1]
   + Numero[8,1,1] = 1
 R11: Numero[0,1,2] + Numero[1,1,2] + Numero[2,1,2] + Numero[3,1,2]
   + Numero[4,1,2] + Numero[5,1,2] + Numero[6,1,2] + Numero[7,1,2]
   + Numero[8,1,2] = 1
 R12: Numero[0,1,3] + Numero[1,1,3] + Numero[2,1,3] + Numero[3,1,3]
   + Numero[4,1,3] + Numero[5,1,3] + Numero[6,1,3] + Numero[7,1,3]
   + Numero[8,1,3] = 1
 R13: Numero[0,1,4] + Numero[1,1,4] + Numero[2,1,4] + Numero[3,1,4]
   + Numero[4,1,4] + Numero[5,1,4] + Numero[6,1,4] + Numero[7,1,4]
   + Numero[8,1,4] = 1
 R14: Numero[0,1,5] + Numero[1,1,5] + Numero[2,1,5] + Numero[3,1,5]
   + Numero[4,1,5] + Numero[5,1,5] + Numero[6,1,5] + Numero[7,1,5]
   + Numero[8,1,5] = 1
 R15: Numero[0,1,6] + Numero[1,1,6] + Numero[2,1,6] + Numero[3,1,6]
   + Numero[4,1,6] + Numero[5,1,6] + Numero[6,1,6] + Numero[7,1,6]
   + Numero[8,1,6] = 1
 R16: Numero[0,1,7] + Numero[1,1,7] + Numero[2,1,7] + Numero[3,1,7]
   + Numero[4,1,7] + Numero[5,1,7] + Numero[6,1,7] + Numero[7,1,7]
   + Numero[8,1,7] = 1
 R17: Numero[0,1,8] + Numero[1,1,8] + Numero[2,1,8] + Numero[3,1,8]
   + Numero[4,1,8] + Numero[5,1,8] + Numero[6,1,8] + Numero[7,1,8]
   + Numero[8,1,8] = 1
 R18: Numero[0,2,0] + Numero[1,2,0] + Numero[2,2,0] + Numero[3,2,0]
   + Numero[4,2,0] + Numero[5,2,0] + Numero[6,2,0] + Numero[7,2,0]
   + Numero[8,2,0] = 1
 R19: Numero[0,2,1] + Numero[1,2,1] + Numero[2,2,1] + Numero[3,2,1]
   + Numero[4,2,1] + Numero[5,2,1] + Numero[6,2,1] + Numero[7,2,1]
   + Numero[8,2,1] = 1
 R20: Numero[0,2,2] + Numero[1,2,2] + Numero[2,2,2] + Numero[3,2,2]
   + Numero[4,2,2] + Numero[5,2,2] + Numero[6,2,2] + Numero[7,2,2]
   + Numero[8,2,2] = 1
 R21: Numero[0,2,3] + Numero[1,2,3] + Numero[2,2,3] + Numero[3,2,3]
   + Numero[4,2,3] + Numero[5,2,3] + Numero[6,2,3] + Numero[7,2,3]
   + Numero[8,2,3] = 1
 R22: Numero[0,2,4] + Numero[1,2,4] + Numero[2,2,4] + Numero[3,2,4]
   + Numero[4,2,4] + Numero[5,2,4] + Numero[6,2,4] + Numero[7,2,4]
   + Numero[8,2,4] = 1
 R23: Numero[0,2,5] + Numero[1,2,5] + Numero[2,2,5] + Numero[3,2,5]
   + Numero[4,2,5] + Numero[5,2,5] + Numero[6,2,5] + Numero[7,2,5]
   + Numero[8,2,5] = 1
 R24: Numero[0,2,6] + Numero[1,2,6] + Numero[2,2,6] + Numero[3,2,6]
   + Numero[4,2,6] + Numero[5,2,6] + Numero[6,2,6] + Numero[7,2,6]
   + Numero[8,2,6] = 1
 R25: Numero[0,2,7] + Numero[1,2,7] + Numero[2,2,7] + Numero[3,2,7]
   + Numero[4,2,7] + Numero[5,2,7] + Numero[6,2,7] + Numero[7,2,7]
   + Numero[8,2,7] = 1
 R26: Numero[0,2,8] + Numero[1,2,8] + Numero[2,2,8] + Numero[3,2,8]
   + Numero[4,2,8] + Numero[5,2,8] + Numero[6,2,8] + Numero[7,2,8]
   + Numero[8,2,8] = 1
 R27: Numero[0,3,0] + Numero[1,3,0] + Numero[2,3,0] + Numero[3,3,0]
   + Numero[4,3,0] + Numero[5,3,0] + Numero[6,3,0] + Numero[7,3,0]
   + Numero[8,3,0] = 1
 R28: Numero[0,3,1] + Numero[1,3,1] + Numero[2,3,1] + Numero[3,3,1]
   + Numero[4,3,1] + Numero[5,3,1] + Numero[6,3,1] + Numero[7,3,1]
   + Numero[8,3,1] = 1
 R29: Numero[0,3,2] + Numero[1,3,2] + Numero[2,3,2] + Numero[3,3,2]
   + Numero[4,3,2] + Numero[5,3,2] + Numero[6,3,2] + Numero[7,3,2]
   + Numero[8,3,2] = 1
 R30: Numero[0,3,3] + Numero[1,3,3] + Numero[2,3,3] + Numero[3,3,3]
   + Numero[4,3,3] + Numero[5,3,3] + Numero[6,3,3] + Numero[7,3,3]
   + Numero[8,3,3] = 1
 R31: Numero[0,3,4] + Numero[1,3,4] + Numero[2,3,4] + Numero[3,3,4]
   + Numero[4,3,4] + Numero[5,3,4] + Numero[6,3,4] + Numero[7,3,4]
   + Numero[8,3,4] = 1
 R32: Numero[0,3,5] + Numero[1,3,5] + Numero[2,3,5] + Numero[3,3,5]
   + Numero[4,3,5] + Numero[5,3,5] + Numero[6,3,5] + Numero[7,3,5]
   + Numero[8,3,5] = 1
 R33: Numero[0,3,6] + Numero[1,3,6] + Numero[2,3,6] + Numero[3,3,6]
   + Numero[4,3,6] + Numero[5,3,6] + Numero[6,3,6] + Numero[7,3,6]
   + Numero[8,3,6] = 1
 R34: Numero[0,3,7] + Numero[1,3,7] + Numero[2,3,7] + Numero[3,3,7]
   + Numero[4,3,7] + Numero[5,3,7] + Numero[6,3,7] + Numero[7,3,7]
   + Numero[8,3,7] = 1
 R35: Numero[0,3,8] + Numero[1,3,8] + Numero[2,3,8] + Numero[3,3,8]
   + Numero[4,3,8] + Numero[5,3,8] + Numero[6,3,8] + Numero[7,3,8]
   + Numero[8,3,8] = 1
 R36: Numero[0,4,0] + Numero[1,4,0] + Numero[2,4,0] + Numero[3,4,0]
   + Numero[4,4,0] + Numero[5,4,0] + Numero[6,4,0] + Numero[7,4,0]
   + Numero[8,4,0] = 1
 R37: Numero[0,4,1] + Numero[1,4,1] + Numero[2,4,1] + Numero[3,4,1]
   + Numero[4,4,1] + Numero[5,4,1] + Numero[6,4,1] + Numero[7,4,1]
   + Numero[8,4,1] = 1
 R38: Numero[0,4,2] + Numero[1,4,2] + Numero[2,4,2] + Numero[3,4,2]
   + Numero[4,4,2] + Numero[5,4,2] + Numero[6,4,2] + Numero[7,4,2]
   + Numero[8,4,2] = 1
 R39: Numero[0,4,3] + Numero[1,4,3] + Numero[2,4,3] + Numero[3,4,3]
   + Numero[4,4,3] + Numero[5,4,3] + Numero[6,4,3] + Numero[7,4,3]
   + Numero[8,4,3] = 1
 R40: Numero[0,4,4] + Numero[1,4,4] + Numero[2,4,4] + Numero[3,4,4]
   + Numero[4,4,4] + Numero[5,4,4] + Numero[6,4,4] + Numero[7,4,4]
   + Numero[8,4,4] = 1
 R41: Numero[0,4,5] + Numero[1,4,5] + Numero[2,4,5] + Numero[3,4,5]
   + Numero[4,4,5] + Numero[5,4,5] + Numero[6,4,5] + Numero[7,4,5]
   + Numero[8,4,5] = 1
 R42: Numero[0,4,6] + Numero[1,4,6] + Numero[2,4,6] + Numero[3,4,6]
   + Numero[4,4,6] + Numero[5,4,6] + Numero[6,4,6] + Numero[7,4,6]
   + Numero[8,4,6] = 1
 R43: Numero[0,4,7] + Numero[1,4,7] + Numero[2,4,7] + Numero[3,4,7]
   + Numero[4,4,7] + Numero[5,4,7] + Numero[6,4,7] + Numero[7,4,7]
   + Numero[8,4,7] = 1
 R44: Numero[0,4,8] + Numero[1,4,8] + Numero[2,4,8] + Numero[3,4,8]
   + Numero[4,4,8] + Numero[5,4,8] + Numero[6,4,8] + Numero[7,4,8]
   + Numero[8,4,8] = 1
 R45: Numero[0,5,0] + Numero[1,5,0] + Numero[2,5,0] + Numero[3,5,0]
   + Numero[4,5,0] + Numero[5,5,0] + Numero[6,5,0] + Numero[7,5,0]
   + Numero[8,5,0] = 1
 R46: Numero[0,5,1] + Numero[1,5,1] + Numero[2,5,1] + Numero[3,5,1]
   + Numero[4,5,1] + Numero[5,5,1] + Numero[6,5,1] + Numero[7,5,1]
   + Numero[8,5,1] = 1
 R47: Numero[0,5,2] + Numero[1,5,2] + Numero[2,5,2] + Numero[3,5,2]
   + Numero[4,5,2] + Numero[5,5,2] + Numero[6,5,2] + Numero[7,5,2]
   + Numero[8,5,2] = 1
 R48: Numero[0,5,3] + Numero[1,5,3] + Numero[2,5,3] + Numero[3,5,3]
   + Numero[4,5,3] + Numero[5,5,3] + Numero[6,5,3] + Numero[7,5,3]
   + Numero[8,5,3] = 1
 R49: Numero[0,5,4] + Numero[1,5,4] + Numero[2,5,4] + Numero[3,5,4]
   + Numero[4,5,4] + Numero[5,5,4] + Numero[6,5,4] + Numero[7,5,4]
   + Numero[8,5,4] = 1
 R50: Numero[0,5,5] + Numero[1,5,5] + Numero[2,5,5] + Numero[3,5,5]
   + Numero[4,5,5] + Numero[5,5,5] + Numero[6,5,5] + Numero[7,5,5]
   + Numero[8,5,5] = 1
 R51: Numero[0,5,6] + Numero[1,5,6] + Numero[2,5,6] + Numero[3,5,6]
   + Numero[4,5,6] + Numero[5,5,6] + Numero[6,5,6] + Numero[7,5,6]
   + Numero[8,5,6] = 1
 R52: Numero[0,5,7] + Numero[1,5,7] + Numero[2,5,7] + Numero[3,5,7]
   + Numero[4,5,7] + Numero[5,5,7] + Numero[6,5,7] + Numero[7,5,7]
   + Numero[8,5,7] = 1
 R53: Numero[0,5,8] + Numero[1,5,8] + Numero[2,5,8] + Numero[3,5,8]
   + Numero[4,5,8] + Numero[5,5,8] + Numero[6,5,8] + Numero[7,5,8]
   + Numero[8,5,8] = 1
 R54: Numero[0,6,0] + Numero[1,6,0] + Numero[2,6,0] + Numero[3,6,0]
   + Numero[4,6,0] + Numero[5,6,0] + Numero[6,6,0] + Numero[7,6,0]
   + Numero[8,6,0] = 1
 R55: Numero[0,6,1] + Numero[1,6,1] + Numero[2,6,1] + Numero[3,6,1]
   + Numero[4,6,1] + Numero[5,6,1] + Numero[6,6,1] + Numero[7,6,1]
   + Numero[8,6,1] = 1
 R56: Numero[0,6,2] + Numero[1,6,2] + Numero[2,6,2] + Numero[3,6,2]
   + Numero[4,6,2] + Numero[5,6,2] + Numero[6,6,2] + Numero[7,6,2]
   + Numero[8,6,2] = 1
 R57: Numero[0,6,3] + Numero[1,6,3] + Numero[2,6,3] + Numero[3,6,3]
   + Numero[4,6,3] + Numero[5,6,3] + Numero[6,6,3] + Numero[7,6,3]
   + Numero[8,6,3] = 1
 R58: Numero[0,6,4] + Numero[1,6,4] + Numero[2,6,4] + Numero[3,6,4]
   + Numero[4,6,4] + Numero[5,6,4] + Numero[6,6,4] + Numero[7,6,4]
   + Numero[8,6,4] = 1
 R59: Numero[0,6,5] + Numero[1,6,5] + Numero[2,6,5] + Numero[3,6,5]
   + Numero[4,6,5] + Numero[5,6,5] + Numero[6,6,5] + Numero[7,6,5]
   + Numero[8,6,5] = 1
 R60: Numero[0,6,6] + Numero[1,6,6] + Numero[2,6,6] + Numero[3,6,6]
   + Numero[4,6,6] + Numero[5,6,6] + Numero[6,6,6] + Numero[7,6,6]
   + Numero[8,6,6] = 1
 R61: Numero[0,6,7] + Numero[1,6,7] + Numero[2,6,7] + Numero[3,6,7]
   + Numero[4,6,7] + Numero[5,6,7] + Numero[6,6,7] + Numero[7,6,7]
   + Numero[8,6,7] = 1
 R62: Numero[0,6,8] + Numero[1,6,8] + Numero[2,6,8] + Numero[3,6,8]
   + Numero[4,6,8] + Numero[5,6,8] + Numero[6,6,8] + Numero[7,6,8]
   + Numero[8,6,8] = 1
 R63: Numero[0,7,0] + Numero[1,7,0] + Numero[2,7,0] + Numero[3,7,0]
   + Numero[4,7,0] + Numero[5,7,0] + Numero[6,7,0] + Numero[7,7,0]
   + Numero[8,7,0] = 1
 R64: Numero[0,7,1] + Numero[1,7,1] + Numero[2,7,1] + Numero[3,7,1]
   + Numero[4,7,1] + Numero[5,7,1] + Numero[6,7,1] + Numero[7,7,1]
   + Numero[8,7,1] = 1
 R65: Numero[0,7,2] + Numero[1,7,2] + Numero[2,7,2] + Numero[3,7,2]
   + Numero[4,7,2] + Numero[5,7,2] + Numero[6,7,2] + Numero[7,7,2]
   + Numero[8,7,2] = 1
 R66: Numero[0,7,3] + Numero[1,7,3] + Numero[2,7,3] + Numero[3,7,3]
   + Numero[4,7,3] + Numero[5,7,3] + Numero[6,7,3] + Numero[7,7,3]
   + Numero[8,7,3] = 1
 R67: Numero[0,7,4] + Numero[1,7,4] + Numero[2,7,4] + Numero[3,7,4]
   + Numero[4,7,4] + Numero[5,7,4] + Numero[6,7,4] + Numero[7,7,4]
   + Numero[8,7,4] = 1
 R68: Numero[0,7,5] + Numero[1,7,5] + Numero[2,7,5] + Numero[3,7,5]
   + Numero[4,7,5] + Numero[5,7,5] + Numero[6,7,5] + Numero[7,7,5]
   + Numero[8,7,5] = 1
 R69: Numero[0,7,6] + Numero[1,7,6] + Numero[2,7,6] + Numero[3,7,6]
   + Numero[4,7,6] + Numero[5,7,6] + Numero[6,7,6] + Numero[7,7,6]
   + Numero[8,7,6] = 1
 R70: Numero[0,7,7] + Numero[1,7,7] + Numero[2,7,7] + Numero[3,7,7]
   + Numero[4,7,7] + Numero[5,7,7] + Numero[6,7,7] + Numero[7,7,7]
   + Numero[8,7,7] = 1
 R71: Numero[0,7,8] + Numero[1,7,8] + Numero[2,7,8] + Numero[3,7,8]
   + Numero[4,7,8] + Numero[5,7,8] + Numero[6,7,8] + Numero[7,7,8]
   + Numero[8,7,8] = 1
 R72: Numero[0,8,0] + Numero[1,8,0] + Numero[2,8,0] + Numero[3,8,0]
   + Numero[4,8,0] + Numero[5,8,0] + Numero[6,8,0] + Numero[7,8,0]
   + Numero[8,8,0] = 1
 R73: Numero[0,8,1] + Numero[1,8,1] + Numero[2,8,1] + Numero[3,8,1]
   + Numero[4,8,1] + Numero[5,8,1] + Numero[6,8,1] + Numero[7,8,1]
   + Numero[8,8,1] = 1
 R74: Numero[0,8,2] + Numero[1,8,2] + Numero[2,8,2] + Numero[3,8,2]
   + Numero[4,8,2] + Numero[5,8,2] + Numero[6,8,2] + Numero[7,8,2]
   + Numero[8,8,2] = 1
 R75: Numero[0,8,3] + Numero[1,8,3] + Numero[2,8,3] + Numero[3,8,3]
   + Numero[4,8,3] + Numero[5,8,3] + Numero[6,8,3] + Numero[7,8,3]
   + Numero[8,8,3] = 1
 R76: Numero[0,8,4] + Numero[1,8,4] + Numero[2,8,4] + Numero[3,8,4]
   + Numero[4,8,4] + Numero[5,8,4] + Numero[6,8,4] + Numero[7,8,4]
   + Numero[8,8,4] = 1
 R77: Numero[0,8,5] + Numero[1,8,5] + Numero[2,8,5] + Numero[3,8,5]
   + Numero[4,8,5] + Numero[5,8,5] + Numero[6,8,5] + Numero[7,8,5]
   + Numero[8,8,5] = 1
 R78: Numero[0,8,6] + Numero[1,8,6] + Numero[2,8,6] + Numero[3,8,6]
   + Numero[4,8,6] + Numero[5,8,6] + Numero[6,8,6] + Numero[7,8,6]
   + Numero[8,8,6] = 1
 R79: Numero[0,8,7] + Numero[1,8,7] + Numero[2,8,7] + Numero[3,8,7]
   + Numero[4,8,7] + Numero[5,8,7] + Numero[6,8,7] + Numero[7,8,7]
   + Numero[8,8,7] = 1
 R80: Numero[0,8,8] + Numero[1,8,8] + Numero[2,8,8] + Numero[3,8,8]
   + Numero[4,8,8] + Numero[5,8,8] + Numero[6,8,8] + Numero[7,8,8]
   + Numero[8,8,8] = 1
 R81: Numero[0,0,0] + Numero[0,1,0] + Numero[0,2,0] + Numero[0,3,0]
   + Numero[0,4,0] + Numero[0,5,0] + Numero[0,6,0] + Numero[0,7,0]
   + Numero[0,8,0] = 1
 R82: Numero[1,0,0] + Numero[1,1,0] + Numero[1,2,0] + Numero[1,3,0]
   + Numero[1,4,0] + Numero[1,5,0] + Numero[1,6,0] + Numero[1,7,0]
   + Numero[1,8,0] = 1
 R83: Numero[2,0,0] + Numero[2,1,0] + Numero[2,2,0] + Numero[2,3,0]
   + Numero[2,4,0] + Numero[2,5,0] + Numero[2,6,0] + Numero[2,7,0]
   + Numero[2,8,0] = 1
 R84: Numero[3,0,0] + Numero[3,1,0] + Numero[3,2,0] + Numero[3,3,0]
   + Numero[3,4,0] + Numero[3,5,0] + Numero[3,6,0] + Numero[3,7,0]
   + Numero[3,8,0] = 1
 R85: Numero[4,0,0] + Numero[4,1,0] + Numero[4,2,0] + Numero[4,3,0]
   + Numero[4,4,0] + Numero[4,5,0] + Numero[4,6,0] + Numero[4,7,0]
   + Numero[4,8,0] = 1
 R86: Numero[5,0,0] + Numero[5,1,0] + Numero[5,2,0] + Numero[5,3,0]
   + Numero[5,4,0] + Numero[5,5,0] + Numero[5,6,0] + Numero[5,7,0]
   + Numero[5,8,0] = 1
 R87: Numero[6,0,0] + Numero[6,1,0] + Numero[6,2,0] + Numero[6,3,0]
   + Numero[6,4,0] + Numero[6,5,0] + Numero[6,6,0] + Numero[6,7,0]
   + Numero[6,8,0] = 1
 R88: Numero[7,0,0] + Numero[7,1,0] + Numero[7,2,0] + Numero[7,3,0]
   + Numero[7,4,0] + Numero[7,5,0] + Numero[7,6,0] + Numero[7,7,0]
   + Numero[7,8,0] = 1
 R89: Numero[8,0,0] + Numero[8,1,0] + Numero[8,2,0] + Numero[8,3,0]
   + Numero[8,4,0] + Numero[8,5,0] + Numero[8,6,0] + Numero[8,7,0]
   + Numero[8,8,0] = 1
 R90: Numero[0,0,1] + Numero[0,1,1] + Numero[0,2,1] + Numero[0,3,1]
   + Numero[0,4,1] + Numero[0,5,1] + Numero[0,6,1] + Numero[0,7,1]
   + Numero[0,8,1] = 1
 R91: Numero[1,0,1] + Numero[1,1,1] + Numero[1,2,1] + Numero[1,3,1]
   + Numero[1,4,1] + Numero[1,5,1] + Numero[1,6,1] + Numero[1,7,1]
   + Numero[1,8,1] = 1
 R92: Numero[2,0,1] + Numero[2,1,1] + Numero[2,2,1] + Numero[2,3,1]
   + Numero[2,4,1] + Numero[2,5,1] + Numero[2,6,1] + Numero[2,7,1]
   + Numero[2,8,1] = 1
 R93: Numero[3,0,1] + Numero[3,1,1] + Numero[3,2,1] + Numero[3,3,1]
   + Numero[3,4,1] + Numero[3,5,1] + Numero[3,6,1] + Numero[3,7,1]
   + Numero[3,8,1] = 1
 R94: Numero[4,0,1] + Numero[4,1,1] + Numero[4,2,1] + Numero[4,3,1]
   + Numero[4,4,1] + Numero[4,5,1] + Numero[4,6,1] + Numero[4,7,1]
   + Numero[4,8,1] = 1
 R95: Numero[5,0,1] + Numero[5,1,1] + Numero[5,2,1] + Numero[5,3,1]
   + Numero[5,4,1] + Numero[5,5,1] + Numero[5,6,1] + Numero[5,7,1]
   + Numero[5,8,1] = 1
 R96: Numero[6,0,1] + Numero[6,1,1] + Numero[6,2,1] + Numero[6,3,1]
   + Numero[6,4,1] + Numero[6,5,1] + Numero[6,6,1] + Numero[6,7,1]
   + Numero[6,8,1] = 1
 R97: Numero[7,0,1] + Numero[7,1,1] + Numero[7,2,1] + Numero[7,3,1]
   + Numero[7,4,1] + Numero[7,5,1] + Numero[7,6,1] + Numero[7,7,1]
   + Numero[7,8,1] = 1
 R98: Numero[8,0,1] + Numero[8,1,1] + Numero[8,2,1] + Numero[8,3,1]
   + Numero[8,4,1] + Numero[8,5,1] + Numero[8,6,1] + Numero[8,7,1]
   + Numero[8,8,1] = 1
 R99: Numero[0,0,2] + Numero[0,1,2] + Numero[0,2,2] + Numero[0,3,2]
   + Numero[0,4,2] + Numero[0,5,2] + Numero[0,6,2] + Numero[0,7,2]
   + Numero[0,8,2] = 1
 R100: Numero[1,0,2] + Numero[1,1,2] + Numero[1,2,2] + Numero[1,3,2]
   + Numero[1,4,2] + Numero[1,5,2] + Numero[1,6,2] + Numero[1,7,2]
   + Numero[1,8,2] = 1
 R101: Numero[2,0,2] + Numero[2,1,2] + Numero[2,2,2] + Numero[2,3,2]
   + Numero[2,4,2] + Numero[2,5,2] + Numero[2,6,2] + Numero[2,7,2]
   + Numero[2,8,2] = 1
 R102: Numero[3,0,2] + Numero[3,1,2] + Numero[3,2,2] + Numero[3,3,2]
   + Numero[3,4,2] + Numero[3,5,2] + Numero[3,6,2] + Numero[3,7,2]
   + Numero[3,8,2] = 1
 R103: Numero[4,0,2] + Numero[4,1,2] + Numero[4,2,2] + Numero[4,3,2]
   + Numero[4,4,2] + Numero[4,5,2] + Numero[4,6,2] + Numero[4,7,2]
   + Numero[4,8,2] = 1
 R104: Numero[5,0,2] + Numero[5,1,2] + Numero[5,2,2] + Numero[5,3,2]
   + Numero[5,4,2] + Numero[5,5,2] + Numero[5,6,2] + Numero[5,7,2]
   + Numero[5,8,2] = 1
 R105: Numero[6,0,2] + Numero[6,1,2] + Numero[6,2,2] + Numero[6,3,2]
   + Numero[6,4,2] + Numero[6,5,2] + Numero[6,6,2] + Numero[6,7,2]
   + Numero[6,8,2] = 1
 R106: Numero[7,0,2] + Numero[7,1,2] + Numero[7,2,2] + Numero[7,3,2]
   + Numero[7,4,2] + Numero[7,5,2] + Numero[7,6,2] + Numero[7,7,2]
   + Numero[7,8,2] = 1
 R107: Numero[8,0,2] + Numero[8,1,2] + Numero[8,2,2] + Numero[8,3,2]
   + Numero[8,4,2] + Numero[8,5,2] + Numero[8,6,2] + Numero[8,7,2]
   + Numero[8,8,2] = 1
 R108: Numero[0,0,3] + Numero[0,1,3] + Numero[0,2,3] + Numero[0,3,3]
   + Numero[0,4,3] + Numero[0,5,3] + Numero[0,6,3] + Numero[0,7,3]
   + Numero[0,8,3] = 1
 R109: Numero[1,0,3] + Numero[1,1,3] + Numero[1,2,3] + Numero[1,3,3]
   + Numero[1,4,3] + Numero[1,5,3] + Numero[1,6,3] + Numero[1,7,3]
   + Numero[1,8,3] = 1
 R110: Numero[2,0,3] + Numero[2,1,3] + Numero[2,2,3] + Numero[2,3,3]
   + Numero[2,4,3] + Numero[2,5,3] + Numero[2,6,3] + Numero[2,7,3]
   + Numero[2,8,3] = 1
 R111: Numero[3,0,3] + Numero[3,1,3] + Numero[3,2,3] + Numero[3,3,3]
   + Numero[3,4,3] + Numero[3,5,3] + Numero[3,6,3] + Numero[3,7,3]
   + Numero[3,8,3] = 1
 R112: Numero[4,0,3] + Numero[4,1,3] + Numero[4,2,3] + Numero[4,3,3]
   + Numero[4,4,3] + Numero[4,5,3] + Numero[4,6,3] + Numero[4,7,3]
   + Numero[4,8,3] = 1
 R113: Numero[5,0,3] + Numero[5,1,3] + Numero[5,2,3] + Numero[5,3,3]
   + Numero[5,4,3] + Numero[5,5,3] + Numero[5,6,3] + Numero[5,7,3]
   + Numero[5,8,3] = 1
 R114: Numero[6,0,3] + Numero[6,1,3] + Numero[6,2,3] + Numero[6,3,3]
   + Numero[6,4,3] + Numero[6,5,3] + Numero[6,6,3] + Numero[6,7,3]
   + Numero[6,8,3] = 1
 R115: Numero[7,0,3] + Numero[7,1,3] + Numero[7,2,3] + Numero[7,3,3]
   + Numero[7,4,3] + Numero[7,5,3] + Numero[7,6,3] + Numero[7,7,3]
   + Numero[7,8,3] = 1
 R116: Numero[8,0,3] + Numero[8,1,3] + Numero[8,2,3] + Numero[8,3,3]
   + Numero[8,4,3] + Numero[8,5,3] + Numero[8,6,3] + Numero[8,7,3]
   + Numero[8,8,3] = 1
 R117: Numero[0,0,4] + Numero[0,1,4] + Numero[0,2,4] + Numero[0,3,4]
   + Numero[0,4,4] + Numero[0,5,4] + Numero[0,6,4] + Numero[0,7,4]
   + Numero[0,8,4] = 1
 R118: Numero[1,0,4] + Numero[1,1,4] + Numero[1,2,4] + Numero[1,3,4]
   + Numero[1,4,4] + Numero[1,5,4] + Numero[1,6,4] + Numero[1,7,4]
   + Numero[1,8,4] = 1
 R119: Numero[2,0,4] + Numero[2,1,4] + Numero[2,2,4] + Numero[2,3,4]
   + Numero[2,4,4] + Numero[2,5,4] + Numero[2,6,4] + Numero[2,7,4]
   + Numero[2,8,4] = 1
 R120: Numero[3,0,4] + Numero[3,1,4] + Numero[3,2,4] + Numero[3,3,4]
   + Numero[3,4,4] + Numero[3,5,4] + Numero[3,6,4] + Numero[3,7,4]
   + Numero[3,8,4] = 1
 R121: Numero[4,0,4] + Numero[4,1,4] + Numero[4,2,4] + Numero[4,3,4]
   + Numero[4,4,4] + Numero[4,5,4] + Numero[4,6,4] + Numero[4,7,4]
   + Numero[4,8,4] = 1
 R122: Numero[5,0,4] + Numero[5,1,4] + Numero[5,2,4] + Numero[5,3,4]
   + Numero[5,4,4] + Numero[5,5,4] + Numero[5,6,4] + Numero[5,7,4]
   + Numero[5,8,4] = 1
 R123: Numero[6,0,4] + Numero[6,1,4] + Numero[6,2,4] + Numero[6,3,4]
   + Numero[6,4,4] + Numero[6,5,4] + Numero[6,6,4] + Numero[6,7,4]
   + Numero[6,8,4] = 1
 R124: Numero[7,0,4] + Numero[7,1,4] + Numero[7,2,4] + Numero[7,3,4]
   + Numero[7,4,4] + Numero[7,5,4] + Numero[7,6,4] + Numero[7,7,4]
   + Numero[7,8,4] = 1
 R125: Numero[8,0,4] + Numero[8,1,4] + Numero[8,2,4] + Numero[8,3,4]
   + Numero[8,4,4] + Numero[8,5,4] + Numero[8,6,4] + Numero[8,7,4]
   + Numero[8,8,4] = 1
 R126: Numero[0,0,5] + Numero[0,1,5] + Numero[0,2,5] + Numero[0,3,5]
   + Numero[0,4,5] + Numero[0,5,5] + Numero[0,6,5] + Numero[0,7,5]
   + Numero[0,8,5] = 1
 R127: Numero[1,0,5] + Numero[1,1,5] + Numero[1,2,5] + Numero[1,3,5]
   + Numero[1,4,5] + Numero[1,5,5] + Numero[1,6,5] + Numero[1,7,5]
   + Numero[1,8,5] = 1
 R128: Numero[2,0,5] + Numero[2,1,5] + Numero[2,2,5] + Numero[2,3,5]
   + Numero[2,4,5] + Numero[2,5,5] + Numero[2,6,5] + Numero[2,7,5]
   + Numero[2,8,5] = 1
 R129: Numero[3,0,5] + Numero[3,1,5] + Numero[3,2,5] + Numero[3,3,5]
   + Numero[3,4,5] + Numero[3,5,5] + Numero[3,6,5] + Numero[3,7,5]
   + Numero[3,8,5] = 1
 R130: Numero[4,0,5] + Numero[4,1,5] + Numero[4,2,5] + Numero[4,3,5]
   + Numero[4,4,5] + Numero[4,5,5] + Numero[4,6,5] + Numero[4,7,5]
   + Numero[4,8,5] = 1
 R131: Numero[5,0,5] + Numero[5,1,5] + Numero[5,2,5] + Numero[5,3,5]
   + Numero[5,4,5] + Numero[5,5,5] + Numero[5,6,5] + Numero[5,7,5]
   + Numero[5,8,5] = 1
 R132: Numero[6,0,5] + Numero[6,1,5] + Numero[6,2,5] + Numero[6,3,5]
   + Numero[6,4,5] + Numero[6,5,5] + Numero[6,6,5] + Numero[6,7,5]
   + Numero[6,8,5] = 1
 R133: Numero[7,0,5] + Numero[7,1,5] + Numero[7,2,5] + Numero[7,3,5]
   + Numero[7,4,5] + Numero[7,5,5] + Numero[7,6,5] + Numero[7,7,5]
   + Numero[7,8,5] = 1
 R134: Numero[8,0,5] + Numero[8,1,5] + Numero[8,2,5] + Numero[8,3,5]
   + Numero[8,4,5] + Numero[8,5,5] + Numero[8,6,5] + Numero[8,7,5]
   + Numero[8,8,5] = 1
 R135: Numero[0,0,6] + Numero[0,1,6] + Numero[0,2,6] + Numero[0,3,6]
   + Numero[0,4,6] + Numero[0,5,6] + Numero[0,6,6] + Numero[0,7,6]
   + Numero[0,8,6] = 1
 R136: Numero[1,0,6] + Numero[1,1,6] + Numero[1,2,6] + Numero[1,3,6]
   + Numero[1,4,6] + Numero[1,5,6] + Numero[1,6,6] + Numero[1,7,6]
   + Numero[1,8,6] = 1
 R137: Numero[2,0,6] + Numero[2,1,6] + Numero[2,2,6] + Numero[2,3,6]
   + Numero[2,4,6] + Numero[2,5,6] + Numero[2,6,6] + Numero[2,7,6]
   + Numero[2,8,6] = 1
 R138: Numero[3,0,6] + Numero[3,1,6] + Numero[3,2,6] + Numero[3,3,6]
   + Numero[3,4,6] + Numero[3,5,6] + Numero[3,6,6] + Numero[3,7,6]
   + Numero[3,8,6] = 1
 R139: Numero[4,0,6] + Numero[4,1,6] + Numero[4,2,6] + Numero[4,3,6]
   + Numero[4,4,6] + Numero[4,5,6] + Numero[4,6,6] + Numero[4,7,6]
   + Numero[4,8,6] = 1
 R140: Numero[5,0,6] + Numero[5,1,6] + Numero[5,2,6] + Numero[5,3,6]
   + Numero[5,4,6] + Numero[5,5,6] + Numero[5,6,6] + Numero[5,7,6]
   + Numero[5,8,6] = 1
 R141: Numero[6,0,6] + Numero[6,1,6] + Numero[6,2,6] + Numero[6,3,6]
   + Numero[6,4,6] + Numero[6,5,6] + Numero[6,6,6] + Numero[6,7,6]
   + Numero[6,8,6] = 1
 R142: Numero[7,0,6] + Numero[7,1,6] + Numero[7,2,6] + Numero[7,3,6]
   + Numero[7,4,6] + Numero[7,5,6] + Numero[7,6,6] + Numero[7,7,6]
   + Numero[7,8,6] = 1
 R143: Numero[8,0,6] + Numero[8,1,6] + Numero[8,2,6] + Numero[8,3,6]
   + Numero[8,4,6] + Numero[8,5,6] + Numero[8,6,6] + Numero[8,7,6]
   + Numero[8,8,6] = 1
 R144: Numero[0,0,7] + Numero[0,1,7] + Numero[0,2,7] + Numero[0,3,7]
   + Numero[0,4,7] + Numero[0,5,7] + Numero[0,6,7] + Numero[0,7,7]
   + Numero[0,8,7] = 1
 R145: Numero[1,0,7] + Numero[1,1,7] + Numero[1,2,7] + Numero[1,3,7]
   + Numero[1,4,7] + Numero[1,5,7] + Numero[1,6,7] + Numero[1,7,7]
   + Numero[1,8,7] = 1
 R146: Numero[2,0,7] + Numero[2,1,7] + Numero[2,2,7] + Numero[2,3,7]
   + Numero[2,4,7] + Numero[2,5,7] + Numero[2,6,7] + Numero[2,7,7]
   + Numero[2,8,7] = 1
 R147: Numero[3,0,7] + Numero[3,1,7] + Numero[3,2,7] + Numero[3,3,7]
   + Numero[3,4,7] + Numero[3,5,7] + Numero[3,6,7] + Numero[3,7,7]
   + Numero[3,8,7] = 1
 R148: Numero[4,0,7] + Numero[4,1,7] + Numero[4,2,7] + Numero[4,3,7]
   + Numero[4,4,7] + Numero[4,5,7] + Numero[4,6,7] + Numero[4,7,7]
   + Numero[4,8,7] = 1
 R149: Numero[5,0,7] + Numero[5,1,7] + Numero[5,2,7] + Numero[5,3,7]
   + Numero[5,4,7] + Numero[5,5,7] + Numero[5,6,7] + Numero[5,7,7]
   + Numero[5,8,7] = 1
 R150: Numero[6,0,7] + Numero[6,1,7] + Numero[6,2,7] + Numero[6,3,7]
   + Numero[6,4,7] + Numero[6,5,7] + Numero[6,6,7] + Numero[6,7,7]
   + Numero[6,8,7] = 1
 R151: Numero[7,0,7] + Numero[7,1,7] + Numero[7,2,7] + Numero[7,3,7]
   + Numero[7,4,7] + Numero[7,5,7] + Numero[7,6,7] + Numero[7,7,7]
   + Numero[7,8,7] = 1
 R152: Numero[8,0,7] + Numero[8,1,7] + Numero[8,2,7] + Numero[8,3,7]
   + Numero[8,4,7] + Numero[8,5,7] + Numero[8,6,7] + Numero[8,7,7]
   + Numero[8,8,7] = 1
 R153: Numero[0,0,8] + Numero[0,1,8] + Numero[0,2,8] + Numero[0,3,8]
   + Numero[0,4,8] + Numero[0,5,8] + Numero[0,6,8] + Numero[0,7,8]
   + Numero[0,8,8] = 1
 R154: Numero[1,0,8] + Numero[1,1,8] + Numero[1,2,8] + Numero[1,3,8]
   + Numero[1,4,8] + Numero[1,5,8] + Numero[1,6,8] + Numero[1,7,8]
   + Numero[1,8,8] = 1
 R155: Numero[2,0,8] + Numero[2,1,8] + Numero[2,2,8] + Numero[2,3,8]
   + Numero[2,4,8] + Numero[2,5,8] + Numero[2,6,8] + Numero[2,7,8]
   + Numero[2,8,8] = 1
 R156: Numero[3,0,8] + Numero[3,1,8] + Numero[3,2,8] + Numero[3,3,8]
   + Numero[3,4,8] + Numero[3,5,8] + Numero[3,6,8] + Numero[3,7,8]
   + Numero[3,8,8] = 1
 R157: Numero[4,0,8] + Numero[4,1,8] + Numero[4,2,8] + Numero[4,3,8]
   + Numero[4,4,8] + Numero[4,5,8] + Numero[4,6,8] + Numero[4,7,8]
   + Numero[4,8,8] = 1
 R158: Numero[5,0,8] + Numero[5,1,8] + Numero[5,2,8] + Numero[5,3,8]
   + Numero[5,4,8] + Numero[5,5,8] + Numero[5,6,8] + Numero[5,7,8]
   + Numero[5,8,8] = 1
 R159: Numero[6,0,8] + Numero[6,1,8] + Numero[6,2,8] + Numero[6,3,8]
   + Numero[6,4,8] + Numero[6,5,8] + Numero[6,6,8] + Numero[6,7,8]
   + Numero[6,8,8] = 1
 R160: Numero[7,0,8] + Numero[7,1,8] + Numero[7,2,8] + Numero[7,3,8]
   + Numero[7,4,8] + Numero[7,5,8] + Numero[7,6,8] + Numero[7,7,8]
   + Numero[7,8,8] = 1
 R161: Numero[8,0,8] + Numero[8,1,8] + Numero[8,2,8] + Numero[8,3,8]
   + Numero[8,4,8] + Numero[8,5,8] + Numero[8,6,8] + Numero[8,7,8]
   + Numero[8,8,8] = 1
 R162: Numero[0,0,0] + Numero[0,0,1] + Numero[0,0,2] + Numero[0,0,3]
   + Numero[0,0,4] + Numero[0,0,5] + Numero[0,0,6] + Numero[0,0,7]
   + Numero[0,0,8] = 1
 R163: Numero[1,0,0] + Numero[1,0,1] + Numero[1,0,2] + Numero[1,0,3]
   + Numero[1,0,4] + Numero[1,0,5] + Numero[1,0,6] + Numero[1,0,7]
   + Numero[1,0,8] = 1
 R164: Numero[2,0,0] + Numero[2,0,1] + Numero[2,0,2] + Numero[2,0,3]
   + Numero[2,0,4] + Numero[2,0,5] + Numero[2,0,6] + Numero[2,0,7]
   + Numero[2,0,8] = 1
 R165: Numero[3,0,0] + Numero[3,0,1] + Numero[3,0,2] + Numero[3,0,3]
   + Numero[3,0,4] + Numero[3,0,5] + Numero[3,0,6] + Numero[3,0,7]
   + Numero[3,0,8] = 1
 R166: Numero[4,0,0] + Numero[4,0,1] + Numero[4,0,2] + Numero[4,0,3]
   + Numero[4,0,4] + Numero[4,0,5] + Numero[4,0,6] + Numero[4,0,7]
   + Numero[4,0,8] = 1
 R167: Numero[5,0,0] + Numero[5,0,1] + Numero[5,0,2] + Numero[5,0,3]
   + Numero[5,0,4] + Numero[5,0,5] + Numero[5,0,6] + Numero[5,0,7]
   + Numero[5,0,8] = 1
 R168: Numero[6,0,0] + Numero[6,0,1] + Numero[6,0,2] + Numero[6,0,3]
   + Numero[6,0,4] + Numero[6,0,5] + Numero[6,0,6] + Numero[6,0,7]
   + Numero[6,0,8] = 1
 R169: Numero[7,0,0] + Numero[7,0,1] + Numero[7,0,2] + Numero[7,0,3]
   + Numero[7,0,4] + Numero[7,0,5] + Numero[7,0,6] + Numero[7,0,7]
   + Numero[7,0,8] = 1
 R170: Numero[8,0,0] + Numero[8,0,1] + Numero[8,0,2] + Numero[8,0,3]
   + Numero[8,0,4] + Numero[8,0,5] + Numero[8,0,6] + Numero[8,0,7]
   + Numero[8,0,8] = 1
 R171: Numero[0,1,0] + Numero[0,1,1] + Numero[0,1,2] + Numero[0,1,3]
   + Numero[0,1,4] + Numero[0,1,5] + Numero[0,1,6] + Numero[0,1,7]
   + Numero[0,1,8] = 1
 R172: Numero[1,1,0] + Numero[1,1,1] + Numero[1,1,2] + Numero[1,1,3]
   + Numero[1,1,4] + Numero[1,1,5] + Numero[1,1,6] + Numero[1,1,7]
   + Numero[1,1,8] = 1
 R173: Numero[2,1,0] + Numero[2,1,1] + Numero[2,1,2] + Numero[2,1,3]
   + Numero[2,1,4] + Numero[2,1,5] + Numero[2,1,6] + Numero[2,1,7]
   + Numero[2,1,8] = 1
 R174: Numero[3,1,0] + Numero[3,1,1] + Numero[3,1,2] + Numero[3,1,3]
   + Numero[3,1,4] + Numero[3,1,5] + Numero[3,1,6] + Numero[3,1,7]
   + Numero[3,1,8] = 1
 R175: Numero[4,1,0] + Numero[4,1,1] + Numero[4,1,2] + Numero[4,1,3]
   + Numero[4,1,4] + Numero[4,1,5] + Numero[4,1,6] + Numero[4,1,7]
   + Numero[4,1,8] = 1
 R176: Numero[5,1,0] + Numero[5,1,1] + Numero[5,1,2] + Numero[5,1,3]
   + Numero[5,1,4] + Numero[5,1,5] + Numero[5,1,6] + Numero[5,1,7]
   + Numero[5,1,8] = 1
 R177: Numero[6,1,0] + Numero[6,1,1] + Numero[6,1,2] + Numero[6,1,3]
   + Numero[6,1,4] + Numero[6,1,5] + Numero[6,1,6] + Numero[6,1,7]
   + Numero[6,1,8] = 1
 R178: Numero[7,1,0] + Numero[7,1,1] + Numero[7,1,2] + Numero[7,1,3]
   + Numero[7,1,4] + Numero[7,1,5] + Numero[7,1,6] + Numero[7,1,7]
   + Numero[7,1,8] = 1
 R179: Numero[8,1,0] + Numero[8,1,1] + Numero[8,1,2] + Numero[8,1,3]
   + Numero[8,1,4] + Numero[8,1,5] + Numero[8,1,6] + Numero[8,1,7]
   + Numero[8,1,8] = 1
 R180: Numero[0,2,0] + Numero[0,2,1] + Numero[0,2,2] + Numero[0,2,3]
   + Numero[0,2,4] + Numero[0,2,5] + Numero[0,2,6] + Numero[0,2,7]
   + Numero[0,2,8] = 1
 R181: Numero[1,2,0] + Numero[1,2,1] + Numero[1,2,2] + Numero[1,2,3]
   + Numero[1,2,4] + Numero[1,2,5] + Numero[1,2,6] + Numero[1,2,7]
   + Numero[1,2,8] = 1
 R182: Numero[2,2,0] + Numero[2,2,1] + Numero[2,2,2] + Numero[2,2,3]
   + Numero[2,2,4] + Numero[2,2,5] + Numero[2,2,6] + Numero[2,2,7]
   + Numero[2,2,8] = 1
 R183: Numero[3,2,0] + Numero[3,2,1] + Numero[3,2,2] + Numero[3,2,3]
   + Numero[3,2,4] + Numero[3,2,5] + Numero[3,2,6] + Numero[3,2,7]
   + Numero[3,2,8] = 1
 R184: Numero[4,2,0] + Numero[4,2,1] + Numero[4,2,2] + Numero[4,2,3]
   + Numero[4,2,4] + Numero[4,2,5] + Numero[4,2,6] + Numero[4,2,7]
   + Numero[4,2,8] = 1
 R185: Numero[5,2,0] + Numero[5,2,1] + Numero[5,2,2] + Numero[5,2,3]
   + Numero[5,2,4] + Numero[5,2,5] + Numero[5,2,6] + Numero[5,2,7]
   + Numero[5,2,8] = 1
 R186: Numero[6,2,0] + Numero[6,2,1] + Numero[6,2,2] + Numero[6,2,3]
   + Numero[6,2,4] + Numero[6,2,5] + Numero[6,2,6] + Numero[6,2,7]
   + Numero[6,2,8] = 1
 R187: Numero[7,2,0] + Numero[7,2,1] + Numero[7,2,2] + Numero[7,2,3]
   + Numero[7,2,4] + Numero[7,2,5] + Numero[7,2,6] + Numero[7,2,7]
   + Numero[7,2,8] = 1
 R188: Numero[8,2,0] + Numero[8,2,1] + Numero[8,2,2] + Numero[8,2,3]
   + Numero[8,2,4] + Numero[8,2,5] + Numero[8,2,6] + Numero[8,2,7]
   + Numero[8,2,8] = 1
 R189: Numero[0,3,0] + Numero[0,3,1] + Numero[0,3,2] + Numero[0,3,3]
   + Numero[0,3,4] + Numero[0,3,5] + Numero[0,3,6] + Numero[0,3,7]
   + Numero[0,3,8] = 1
 R190: Numero[1,3,0] + Numero[1,3,1] + Numero[1,3,2] + Numero[1,3,3]
   + Numero[1,3,4] + Numero[1,3,5] + Numero[1,3,6] + Numero[1,3,7]
   + Numero[1,3,8] = 1
 R191: Numero[2,3,0] + Numero[2,3,1] + Numero[2,3,2] + Numero[2,3,3]
   + Numero[2,3,4] + Numero[2,3,5] + Numero[2,3,6] + Numero[2,3,7]
   + Numero[2,3,8] = 1
 R192: Numero[3,3,0] + Numero[3,3,1] + Numero[3,3,2] + Numero[3,3,3]
   + Numero[3,3,4] + Numero[3,3,5] + Numero[3,3,6] + Numero[3,3,7]
   + Numero[3,3,8] = 1
 R193: Numero[4,3,0] + Numero[4,3,1] + Numero[4,3,2] + Numero[4,3,3]
   + Numero[4,3,4] + Numero[4,3,5] + Numero[4,3,6] + Numero[4,3,7]
   + Numero[4,3,8] = 1
 R194: Numero[5,3,0] + Numero[5,3,1] + Numero[5,3,2] + Numero[5,3,3]
   + Numero[5,3,4] + Numero[5,3,5] + Numero[5,3,6] + Numero[5,3,7]
   + Numero[5,3,8] = 1
 R195: Numero[6,3,0] + Numero[6,3,1] + Numero[6,3,2] + Numero[6,3,3]
   + Numero[6,3,4] + Numero[6,3,5] + Numero[6,3,6] + Numero[6,3,7]
   + Numero[6,3,8] = 1
 R196: Numero[7,3,0] + Numero[7,3,1] + Numero[7,3,2] + Numero[7,3,3]
   + Numero[7,3,4] + Numero[7,3,5] + Numero[7,3,6] + Numero[7,3,7]
   + Numero[7,3,8] = 1
 R197: Numero[8,3,0] + Numero[8,3,1] + Numero[8,3,2] + Numero[8,3,3]
   + Numero[8,3,4] + Numero[8,3,5] + Numero[8,3,6] + Numero[8,3,7]
   + Numero[8,3,8] = 1
 R198: Numero[0,4,0] + Numero[0,4,1] + Numero[0,4,2] + Numero[0,4,3]
   + Numero[0,4,4] + Numero[0,4,5] + Numero[0,4,6] + Numero[0,4,7]
   + Numero[0,4,8] = 1
 R199: Numero[1,4,0] + Numero[1,4,1] + Numero[1,4,2] + Numero[1,4,3]
   + Numero[1,4,4] + Numero[1,4,5] + Numero[1,4,6] + Numero[1,4,7]
   + Numero[1,4,8] = 1
 R200: Numero[2,4,0] + Numero[2,4,1] + Numero[2,4,2] + Numero[2,4,3]
   + Numero[2,4,4] + Numero[2,4,5] + Numero[2,4,6] + Numero[2,4,7]
   + Numero[2,4,8] = 1
 R201: Numero[3,4,0] + Numero[3,4,1] + Numero[3,4,2] + Numero[3,4,3]
   + Numero[3,4,4] + Numero[3,4,5] + Numero[3,4,6] + Numero[3,4,7]
   + Numero[3,4,8] = 1
 R202: Numero[4,4,0] + Numero[4,4,1] + Numero[4,4,2] + Numero[4,4,3]
   + Numero[4,4,4] + Numero[4,4,5] + Numero[4,4,6] + Numero[4,4,7]
   + Numero[4,4,8] = 1
 R203: Numero[5,4,0] + Numero[5,4,1] + Numero[5,4,2] + Numero[5,4,3]
   + Numero[5,4,4] + Numero[5,4,5] + Numero[5,4,6] + Numero[5,4,7]
   + Numero[5,4,8] = 1
 R204: Numero[6,4,0] + Numero[6,4,1] + Numero[6,4,2] + Numero[6,4,3]
   + Numero[6,4,4] + Numero[6,4,5] + Numero[6,4,6] + Numero[6,4,7]
   + Numero[6,4,8] = 1
 R205: Numero[7,4,0] + Numero[7,4,1] + Numero[7,4,2] + Numero[7,4,3]
   + Numero[7,4,4] + Numero[7,4,5] + Numero[7,4,6] + Numero[7,4,7]
   + Numero[7,4,8] = 1
 R206: Numero[8,4,0] + Numero[8,4,1] + Numero[8,4,2] + Numero[8,4,3]
   + Numero[8,4,4] + Numero[8,4,5] + Numero[8,4,6] + Numero[8,4,7]
   + Numero[8,4,8] = 1
 R207: Numero[0,5,0] + Numero[0,5,1] + Numero[0,5,2] + Numero[0,5,3]
   + Numero[0,5,4] + Numero[0,5,5] + Numero[0,5,6] + Numero[0,5,7]
   + Numero[0,5,8] = 1
 R208: Numero[1,5,0] + Numero[1,5,1] + Numero[1,5,2] + Numero[1,5,3]
   + Numero[1,5,4] + Numero[1,5,5] + Numero[1,5,6] + Numero[1,5,7]
   + Numero[1,5,8] = 1
 R209: Numero[2,5,0] + Numero[2,5,1] + Numero[2,5,2] + Numero[2,5,3]
   + Numero[2,5,4] + Numero[2,5,5] + Numero[2,5,6] + Numero[2,5,7]
   + Numero[2,5,8] = 1
 R210: Numero[3,5,0] + Numero[3,5,1] + Numero[3,5,2] + Numero[3,5,3]
   + Numero[3,5,4] + Numero[3,5,5] + Numero[3,5,6] + Numero[3,5,7]
   + Numero[3,5,8] = 1
 R211: Numero[4,5,0] + Numero[4,5,1] + Numero[4,5,2] + Numero[4,5,3]
   + Numero[4,5,4] + Numero[4,5,5] + Numero[4,5,6] + Numero[4,5,7]
   + Numero[4,5,8] = 1
 R212: Numero[5,5,0] + Numero[5,5,1] + Numero[5,5,2] + Numero[5,5,3]
   + Numero[5,5,4] + Numero[5,5,5] + Numero[5,5,6] + Numero[5,5,7]
   + Numero[5,5,8] = 1
 R213: Numero[6,5,0] + Numero[6,5,1] + Numero[6,5,2] + Numero[6,5,3]
   + Numero[6,5,4] + Numero[6,5,5] + Numero[6,5,6] + Numero[6,5,7]
   + Numero[6,5,8] = 1
 R214: Numero[7,5,0] + Numero[7,5,1] + Numero[7,5,2] + Numero[7,5,3]
   + Numero[7,5,4] + Numero[7,5,5] + Numero[7,5,6] + Numero[7,5,7]
   + Numero[7,5,8] = 1
 R215: Numero[8,5,0] + Numero[8,5,1] + Numero[8,5,2] + Numero[8,5,3]
   + Numero[8,5,4] + Numero[8,5,5] + Numero[8,5,6] + Numero[8,5,7]
   + Numero[8,5,8] = 1
 R216: Numero[0,6,0] + Numero[0,6,1] + Numero[0,6,2] + Numero[0,6,3]
   + Numero[0,6,4] + Numero[0,6,5] + Numero[0,6,6] + Numero[0,6,7]
   + Numero[0,6,8] = 1
 R217: Numero[1,6,0] + Numero[1,6,1] + Numero[1,6,2] + Numero[1,6,3]
   + Numero[1,6,4] + Numero[1,6,5] + Numero[1,6,6] + Numero[1,6,7]
   + Numero[1,6,8] = 1
 R218: Numero[2,6,0] + Numero[2,6,1] + Numero[2,6,2] + Numero[2,6,3]
   + Numero[2,6,4] + Numero[2,6,5] + Numero[2,6,6] + Numero[2,6,7]
   + Numero[2,6,8] = 1
 R219: Numero[3,6,0] + Numero[3,6,1] + Numero[3,6,2] + Numero[3,6,3]
   + Numero[3,6,4] + Numero[3,6,5] + Numero[3,6,6] + Numero[3,6,7]
   + Numero[3,6,8] = 1
 R220: Numero[4,6,0] + Numero[4,6,1] + Numero[4,6,2] + Numero[4,6,3]
   + Numero[4,6,4] + Numero[4,6,5] + Numero[4,6,6] + Numero[4,6,7]
   + Numero[4,6,8] = 1
 R221: Numero[5,6,0] + Numero[5,6,1] + Numero[5,6,2] + Numero[5,6,3]
   + Numero[5,6,4] + Numero[5,6,5] + Numero[5,6,6] + Numero[5,6,7]
   + Numero[5,6,8] = 1
 R222: Numero[6,6,0] + Numero[6,6,1] + Numero[6,6,2] + Numero[6,6,3]
   + Numero[6,6,4] + Numero[6,6,5] + Numero[6,6,6] + Numero[6,6,7]
   + Numero[6,6,8] = 1
 R223: Numero[7,6,0] + Numero[7,6,1] + Numero[7,6,2] + Numero[7,6,3]
   + Numero[7,6,4] + Numero[7,6,5] + Numero[7,6,6] + Numero[7,6,7]
   + Numero[7,6,8] = 1
 R224: Numero[8,6,0] + Numero[8,6,1] + Numero[8,6,2] + Numero[8,6,3]
   + Numero[8,6,4] + Numero[8,6,5] + Numero[8,6,6] + Numero[8,6,7]
   + Numero[8,6,8] = 1
 R225: Numero[0,7,0] + Numero[0,7,1] + Numero[0,7,2] + Numero[0,7,3]
   + Numero[0,7,4] + Numero[0,7,5] + Numero[0,7,6] + Numero[0,7,7]
   + Numero[0,7,8] = 1
 R226: Numero[1,7,0] + Numero[1,7,1] + Numero[1,7,2] + Numero[1,7,3]
   + Numero[1,7,4] + Numero[1,7,5] + Numero[1,7,6] + Numero[1,7,7]
   + Numero[1,7,8] = 1
 R227: Numero[2,7,0] + Numero[2,7,1] + Numero[2,7,2] + Numero[2,7,3]
   + Numero[2,7,4] + Numero[2,7,5] + Numero[2,7,6] + Numero[2,7,7]
   + Numero[2,7,8] = 1
 R228: Numero[3,7,0] + Numero[3,7,1] + Numero[3,7,2] + Numero[3,7,3]
   + Numero[3,7,4] + Numero[3,7,5] + Numero[3,7,6] + Numero[3,7,7]
   + Numero[3,7,8] = 1
 R229: Numero[4,7,0] + Numero[4,7,1] + Numero[4,7,2] + Numero[4,7,3]
   + Numero[4,7,4] + Numero[4,7,5] + Numero[4,7,6] + Numero[4,7,7]
   + Numero[4,7,8] = 1
 R230: Numero[5,7,0] + Numero[5,7,1] + Numero[5,7,2] + Numero[5,7,3]
   + Numero[5,7,4] + Numero[5,7,5] + Numero[5,7,6] + Numero[5,7,7]
   + Numero[5,7,8] = 1
 R231: Numero[6,7,0] + Numero[6,7,1] + Numero[6,7,2] + Numero[6,7,3]
   + Numero[6,7,4] + Numero[6,7,5] + Numero[6,7,6] + Numero[6,7,7]
   + Numero[6,7,8] = 1
 R232: Numero[7,7,0] + Numero[7,7,1] + Numero[7,7,2] + Numero[7,7,3]
   + Numero[7,7,4] + Numero[7,7,5] + Numero[7,7,6] + Numero[7,7,7]
   + Numero[7,7,8] = 1
 R233: Numero[8,7,0] + Numero[8,7,1] + Numero[8,7,2] + Numero[8,7,3]
   + Numero[8,7,4] + Numero[8,7,5] + Numero[8,7,6] + Numero[8,7,7]
   + Numero[8,7,8] = 1
 R234: Numero[0,8,0] + Numero[0,8,1] + Numero[0,8,2] + Numero[0,8,3]
   + Numero[0,8,4] + Numero[0,8,5] + Numero[0,8,6] + Numero[0,8,7]
   + Numero[0,8,8] = 1
 R235: Numero[1,8,0] + Numero[1,8,1] + Numero[1,8,2] + Numero[1,8,3]
   + Numero[1,8,4] + Numero[1,8,5] + Numero[1,8,6] + Numero[1,8,7]
   + Numero[1,8,8] = 1
 R236: Numero[2,8,0] + Numero[2,8,1] + Numero[2,8,2] + Numero[2,8,3]
   + Numero[2,8,4] + Numero[2,8,5] + Numero[2,8,6] + Numero[2,8,7]
   + Numero[2,8,8] = 1
 R237: Numero[3,8,0] + Numero[3,8,1] + Numero[3,8,2] + Numero[3,8,3]
   + Numero[3,8,4] + Numero[3,8,5] + Numero[3,8,6] + Numero[3,8,7]
   + Numero[3,8,8] = 1
 R238: Numero[4,8,0] + Numero[4,8,1] + Numero[4,8,2] + Numero[4,8,3]
   + Numero[4,8,4] + Numero[4,8,5] + Numero[4,8,6] + Numero[4,8,7]
   + Numero[4,8,8] = 1
 R239: Numero[5,8,0] + Numero[5,8,1] + Numero[5,8,2] + Numero[5,8,3]
   + Numero[5,8,4] + Numero[5,8,5] + Numero[5,8,6] + Numero[5,8,7]
   + Numero[5,8,8] = 1
 R240: Numero[6,8,0] + Numero[6,8,1] + Numero[6,8,2] + Numero[6,8,3]
   + Numero[6,8,4] + Numero[6,8,5] + Numero[6,8,6] + Numero[6,8,7]
   + Numero[6,8,8] = 1
 R241: Numero[7,8,0] + Numero[7,8,1] + Numero[7,8,2] + Numero[7,8,3]
   + Numero[7,8,4] + Numero[7,8,5] + Numero[7,8,6] + Numero[7,8,7]
   + Numero[7,8,8] = 1
 R242: Numero[8,8,0] + Numero[8,8,1] + Numero[8,8,2] + Numero[8,8,3]
   + Numero[8,8,4] + Numero[8,8,5] + Numero[8,8,6] + Numero[8,8,7]
   + Numero[8,8,8] = 1
 R243: Numero[0,0,0] + Numero[0,1,0] + Numero[0,2,0] + Numero[1,0,0]
   + Numero[1,1,0] + Numero[1,2,0] + Numero[2,0,0] + Numero[2,1,0]
   + Numero[2,2,0] = 1
 R244: Numero[0,3,0] + Numero[0,4,0] + Numero[0,5,0] + Numero[1,3,0]
   + Numero[1,4,0] + Numero[1,5,0] + Numero[2,3,0] + Numero[2,4,0]
   + Numero[2,5,0] = 1
 R245: Numero[0,6,0] + Numero[0,7,0] + Numero[0,8,0] + Numero[1,6,0]
   + Numero[1,7,0] + Numero[1,8,0] + Numero[2,6,0] + Numero[2,7,0]
   + Numero[2,8,0] = 1
 R246: Numero[3,0,0] + Numero[3,1,0] + Numero[3,2,0] + Numero[4,0,0]
   + Numero[4,1,0] + Numero[4,2,0] + Numero[5,0,0] + Numero[5,1,0]
   + Numero[5,2,0] = 1
 R247: Numero[3,3,0] + Numero[3,4,0] + Numero[3,5,0] + Numero[4,3,0]
   + Numero[4,4,0] + Numero[4,5,0] + Numero[5,3,0] + Numero[5,4,0]
   + Numero[5,5,0] = 1
 R248: Numero[3,6,0] + Numero[3,7,0] + Numero[3,8,0] + Numero[4,6,0]
   + Numero[4,7,0] + Numero[4,8,0] + Numero[5,6,0] + Numero[5,7,0]
   + Numero[5,8,0] = 1
 R249: Numero[6,0,0] + Numero[6,1,0] + Numero[6,2,0] + Numero[7,0,0]
   + Numero[7,1,0] + Numero[7,2,0] + Numero[8,0,0] + Numero[8,1,0]
   + Numero[8,2,0] = 1
 R250: Numero[6,3,0] + Numero[6,4,0] + Numero[6,5,0] + Numero[7,3,0]
   + Numero[7,4,0] + Numero[7,5,0] + Numero[8,3,0] + Numero[8,4,0]
   + Numero[8,5,0] = 1
 R251: Numero[6,6,0] + Numero[6,7,0] + Numero[6,8,0] + Numero[7,6,0]
   + Numero[7,7,0] + Numero[7,8,0] + Numero[8,6,0] + Numero[8,7,0]
   + Numero[8,8,0] = 1
 R252: Numero[0,0,1] + Numero[0,1,1] + Numero[0,2,1] + Numero[1,0,1]
   + Numero[1,1,1] + Numero[1,2,1] + Numero[2,0,1] + Numero[2,1,1]
   + Numero[2,2,1] = 1
 R253: Numero[0,3,1] + Numero[0,4,1] + Numero[0,5,1] + Numero[1,3,1]
   + Numero[1,4,1] + Numero[1,5,1] + Numero[2,3,1] + Numero[2,4,1]
   + Numero[2,5,1] = 1
 R254: Numero[0,6,1] + Numero[0,7,1] + Numero[0,8,1] + Numero[1,6,1]
   + Numero[1,7,1] + Numero[1,8,1] + Numero[2,6,1] + Numero[2,7,1]
   + Numero[2,8,1] = 1
 R255: Numero[3,0,1] + Numero[3,1,1] + Numero[3,2,1] + Numero[4,0,1]
   + Numero[4,1,1] + Numero[4,2,1] + Numero[5,0,1] + Numero[5,1,1]
   + Numero[5,2,1] = 1
 R256: Numero[3,3,1] + Numero[3,4,1] + Numero[3,5,1] + Numero[4,3,1]
   + Numero[4,4,1] + Numero[4,5,1] + Numero[5,3,1] + Numero[5,4,1]
   + Numero[5,5,1] = 1
 R257: Numero[3,6,1] + Numero[3,7,1] + Numero[3,8,1] + Numero[4,6,1]
   + Numero[4,7,1] + Numero[4,8,1] + Numero[5,6,1] + Numero[5,7,1]
   + Numero[5,8,1] = 1
 R258: Numero[6,0,1] + Numero[6,1,1] + Numero[6,2,1] + Numero[7,0,1]
   + Numero[7,1,1] + Numero[7,2,1] + Numero[8,0,1] + Numero[8,1,1]
   + Numero[8,2,1] = 1
 R259: Numero[6,3,1] + Numero[6,4,1] + Numero[6,5,1] + Numero[7,3,1]
   + Numero[7,4,1] + Numero[7,5,1] + Numero[8,3,1] + Numero[8,4,1]
   + Numero[8,5,1] = 1
 R260: Numero[6,6,1] + Numero[6,7,1] + Numero[6,8,1] + Numero[7,6,1]
   + Numero[7,7,1] + Numero[7,8,1] + Numero[8,6,1] + Numero[8,7,1]
   + Numero[8,8,1] = 1
 R261: Numero[0,0,2] + Numero[0,1,2] + Numero[0,2,2] + Numero[1,0,2]
   + Numero[1,1,2] + Numero[1,2,2] + Numero[2,0,2] + Numero[2,1,2]
   + Numero[2,2,2] = 1
 R262: Numero[0,3,2] + Numero[0,4,2] + Numero[0,5,2] + Numero[1,3,2]
   + Numero[1,4,2] + Numero[1,5,2] + Numero[2,3,2] + Numero[2,4,2]
   + Numero[2,5,2] = 1
 R263: Numero[0,6,2] + Numero[0,7,2] + Numero[0,8,2] + Numero[1,6,2]
   + Numero[1,7,2] + Numero[1,8,2] + Numero[2,6,2] + Numero[2,7,2]
   + Numero[2,8,2] = 1
 R264: Numero[3,0,2] + Numero[3,1,2] + Numero[3,2,2] + Numero[4,0,2]
   + Numero[4,1,2] + Numero[4,2,2] + Numero[5,0,2] + Numero[5,1,2]
   + Numero[5,2,2] = 1
 R265: Numero[3,3,2] + Numero[3,4,2] + Numero[3,5,2] + Numero[4,3,2]
   + Numero[4,4,2] + Numero[4,5,2] + Numero[5,3,2] + Numero[5,4,2]
   + Numero[5,5,2] = 1
 R266: Numero[3,6,2] + Numero[3,7,2] + Numero[3,8,2] + Numero[4,6,2]
   + Numero[4,7,2] + Numero[4,8,2] + Numero[5,6,2] + Numero[5,7,2]
   + Numero[5,8,2] = 1
 R267: Numero[6,0,2] + Numero[6,1,2] + Numero[6,2,2] + Numero[7,0,2]
   + Numero[7,1,2] + Numero[7,2,2] + Numero[8,0,2] + Numero[8,1,2]
   + Numero[8,2,2] = 1
 R268: Numero[6,3,2] + Numero[6,4,2] + Numero[6,5,2] + Numero[7,3,2]
   + Numero[7,4,2] + Numero[7,5,2] + Numero[8,3,2] + Numero[8,4,2]
   + Numero[8,5,2] = 1
 R269: Numero[6,6,2] + Numero[6,7,2] + Numero[6,8,2] + Numero[7,6,2]
   + Numero[7,7,2] + Numero[7,8,2] + Numero[8,6,2] + Numero[8,7,2]
   + Numero[8,8,2] = 1
 R270: Numero[0,0,3] + Numero[0,1,3] + Numero[0,2,3] + Numero[1,0,3]
   + Numero[1,1,3] + Numero[1,2,3] + Numero[2,0,3] + Numero[2,1,3]
   + Numero[2,2,3] = 1
 R271: Numero[0,3,3] + Numero[0,4,3] + Numero[0,5,3] + Numero[1,3,3]
   + Numero[1,4,3] + Numero[1,5,3] + Numero[2,3,3] + Numero[2,4,3]
   + Numero[2,5,3] = 1
 R272: Numero[0,6,3] + Numero[0,7,3] + Numero[0,8,3] + Numero[1,6,3]
   + Numero[1,7,3] + Numero[1,8,3] + Numero[2,6,3] + Numero[2,7,3]
   + Numero[2,8,3] = 1
 R273: Numero[3,0,3] + Numero[3,1,3] + Numero[3,2,3] + Numero[4,0,3]
   + Numero[4,1,3] + Numero[4,2,3] + Numero[5,0,3] + Numero[5,1,3]
   + Numero[5,2,3] = 1
 R274: Numero[3,3,3] + Numero[3,4,3] + Numero[3,5,3] + Numero[4,3,3]
   + Numero[4,4,3] + Numero[4,5,3] + Numero[5,3,3] + Numero[5,4,3]
   + Numero[5,5,3] = 1
 R275: Numero[3,6,3] + Numero[3,7,3] + Numero[3,8,3] + Numero[4,6,3]
   + Numero[4,7,3] + Numero[4,8,3] + Numero[5,6,3] + Numero[5,7,3]
   + Numero[5,8,3] = 1
 R276: Numero[6,0,3] + Numero[6,1,3] + Numero[6,2,3] + Numero[7,0,3]
   + Numero[7,1,3] + Numero[7,2,3] + Numero[8,0,3] + Numero[8,1,3]
   + Numero[8,2,3] = 1
 R277: Numero[6,3,3] + Numero[6,4,3] + Numero[6,5,3] + Numero[7,3,3]
   + Numero[7,4,3] + Numero[7,5,3] + Numero[8,3,3] + Numero[8,4,3]
   + Numero[8,5,3] = 1
 R278: Numero[6,6,3] + Numero[6,7,3] + Numero[6,8,3] + Numero[7,6,3]
   + Numero[7,7,3] + Numero[7,8,3] + Numero[8,6,3] + Numero[8,7,3]
   + Numero[8,8,3] = 1
 R279: Numero[0,0,4] + Numero[0,1,4] + Numero[0,2,4] + Numero[1,0,4]
   + Numero[1,1,4] + Numero[1,2,4] + Numero[2,0,4] + Numero[2,1,4]
   + Numero[2,2,4] = 1
 R280: Numero[0,3,4] + Numero[0,4,4] + Numero[0,5,4] + Numero[1,3,4]
   + Numero[1,4,4] + Numero[1,5,4] + Numero[2,3,4] + Numero[2,4,4]
   + Numero[2,5,4] = 1
 R281: Numero[0,6,4] + Numero[0,7,4] + Numero[0,8,4] + Numero[1,6,4]
   + Numero[1,7,4] + Numero[1,8,4] + Numero[2,6,4] + Numero[2,7,4]
   + Numero[2,8,4] = 1
 R282: Numero[3,0,4] + Numero[3,1,4] + Numero[3,2,4] + Numero[4,0,4]
   + Numero[4,1,4] + Numero[4,2,4] + Numero[5,0,4] + Numero[5,1,4]
   + Numero[5,2,4] = 1
 R283: Numero[3,3,4] + Numero[3,4,4] + Numero[3,5,4] + Numero[4,3,4]
   + Numero[4,4,4] + Numero[4,5,4] + Numero[5,3,4] + Numero[5,4,4]
   + Numero[5,5,4] = 1
 R284: Numero[3,6,4] + Numero[3,7,4] + Numero[3,8,4] + Numero[4,6,4]
   + Numero[4,7,4] + Numero[4,8,4] + Numero[5,6,4] + Numero[5,7,4]
   + Numero[5,8,4] = 1
 R285: Numero[6,0,4] + Numero[6,1,4] + Numero[6,2,4] + Numero[7,0,4]
   + Numero[7,1,4] + Numero[7,2,4] + Numero[8,0,4] + Numero[8,1,4]
   + Numero[8,2,4] = 1
 R286: Numero[6,3,4] + Numero[6,4,4] + Numero[6,5,4] + Numero[7,3,4]
   + Numero[7,4,4] + Numero[7,5,4] + Numero[8,3,4] + Numero[8,4,4]
   + Numero[8,5,4] = 1
 R287: Numero[6,6,4] + Numero[6,7,4] + Numero[6,8,4] + Numero[7,6,4]
   + Numero[7,7,4] + Numero[7,8,4] + Numero[8,6,4] + Numero[8,7,4]
   + Numero[8,8,4] = 1
 R288: Numero[0,0,5] + Numero[0,1,5] + Numero[0,2,5] + Numero[1,0,5]
   + Numero[1,1,5] + Numero[1,2,5] + Numero[2,0,5] + Numero[2,1,5]
   + Numero[2,2,5] = 1
 R289: Numero[0,3,5] + Numero[0,4,5] + Numero[0,5,5] + Numero[1,3,5]
   + Numero[1,4,5] + Numero[1,5,5] + Numero[2,3,5] + Numero[2,4,5]
   + Numero[2,5,5] = 1
 R290: Numero[0,6,5] + Numero[0,7,5] + Numero[0,8,5] + Numero[1,6,5]
   + Numero[1,7,5] + Numero[1,8,5] + Numero[2,6,5] + Numero[2,7,5]
   + Numero[2,8,5] = 1
 R291: Numero[3,0,5] + Numero[3,1,5] + Numero[3,2,5] + Numero[4,0,5]
   + Numero[4,1,5] + Numero[4,2,5] + Numero[5,0,5] + Numero[5,1,5]
   + Numero[5,2,5] = 1
 R292: Numero[3,3,5] + Numero[3,4,5] + Numero[3,5,5] + Numero[4,3,5]
   + Numero[4,4,5] + Numero[4,5,5] + Numero[5,3,5] + Numero[5,4,5]
   + Numero[5,5,5] = 1
 R293: Numero[3,6,5] + Numero[3,7,5] + Numero[3,8,5] + Numero[4,6,5]
   + Numero[4,7,5] + Numero[4,8,5] + Numero[5,6,5] + Numero[5,7,5]
   + Numero[5,8,5] = 1
 R294: Numero[6,0,5] + Numero[6,1,5] + Numero[6,2,5] + Numero[7,0,5]
   + Numero[7,1,5] + Numero[7,2,5] + Numero[8,0,5] + Numero[8,1,5]
   + Numero[8,2,5] = 1
 R295: Numero[6,3,5] + Numero[6,4,5] + Numero[6,5,5] + Numero[7,3,5]
   + Numero[7,4,5] + Numero[7,5,5] + Numero[8,3,5] + Numero[8,4,5]
   + Numero[8,5,5] = 1
 R296: Numero[6,6,5] + Numero[6,7,5] + Numero[6,8,5] + Numero[7,6,5]
   + Numero[7,7,5] + Numero[7,8,5] + Numero[8,6,5] + Numero[8,7,5]
   + Numero[8,8,5] = 1
 R297: Numero[0,0,6] + Numero[0,1,6] + Numero[0,2,6] + Numero[1,0,6]
   + Numero[1,1,6] + Numero[1,2,6] + Numero[2,0,6] + Numero[2,1,6]
   + Numero[2,2,6] = 1
 R298: Numero[0,3,6] + Numero[0,4,6] + Numero[0,5,6] + Numero[1,3,6]
   + Numero[1,4,6] + Numero[1,5,6] + Numero[2,3,6] + Numero[2,4,6]
   + Numero[2,5,6] = 1
 R299: Numero[0,6,6] + Numero[0,7,6] + Numero[0,8,6] + Numero[1,6,6]
   + Numero[1,7,6] + Numero[1,8,6] + Numero[2,6,6] + Numero[2,7,6]
   + Numero[2,8,6] = 1
 R300: Numero[3,0,6] + Numero[3,1,6] + Numero[3,2,6] + Numero[4,0,6]
   + Numero[4,1,6] + Numero[4,2,6] + Numero[5,0,6] + Numero[5,1,6]
   + Numero[5,2,6] = 1
 R301: Numero[3,3,6] + Numero[3,4,6] + Numero[3,5,6] + Numero[4,3,6]
   + Numero[4,4,6] + Numero[4,5,6] + Numero[5,3,6] + Numero[5,4,6]
   + Numero[5,5,6] = 1
 R302: Numero[3,6,6] + Numero[3,7,6] + Numero[3,8,6] + Numero[4,6,6]
   + Numero[4,7,6] + Numero[4,8,6] + Numero[5,6,6] + Numero[5,7,6]
   + Numero[5,8,6] = 1
 R303: Numero[6,0,6] + Numero[6,1,6] + Numero[6,2,6] + Numero[7,0,6]
   + Numero[7,1,6] + Numero[7,2,6] + Numero[8,0,6] + Numero[8,1,6]
   + Numero[8,2,6] = 1
 R304: Numero[6,3,6] + Numero[6,4,6] + Numero[6,5,6] + Numero[7,3,6]
   + Numero[7,4,6] + Numero[7,5,6] + Numero[8,3,6] + Numero[8,4,6]
   + Numero[8,5,6] = 1
 R305: Numero[6,6,6] + Numero[6,7,6] + Numero[6,8,6] + Numero[7,6,6]
   + Numero[7,7,6] + Numero[7,8,6] + Numero[8,6,6] + Numero[8,7,6]
   + Numero[8,8,6] = 1
 R306: Numero[0,0,7] + Numero[0,1,7] + Numero[0,2,7] + Numero[1,0,7]
   + Numero[1,1,7] + Numero[1,2,7] + Numero[2,0,7] + Numero[2,1,7]
   + Numero[2,2,7] = 1
 R307: Numero[0,3,7] + Numero[0,4,7] + Numero[0,5,7] + Numero[1,3,7]
   + Numero[1,4,7] + Numero[1,5,7] + Numero[2,3,7] + Numero[2,4,7]
   + Numero[2,5,7] = 1
 R308: Numero[0,6,7] + Numero[0,7,7] + Numero[0,8,7] + Numero[1,6,7]
   + Numero[1,7,7] + Numero[1,8,7] + Numero[2,6,7] + Numero[2,7,7]
   + Numero[2,8,7] = 1
 R309: Numero[3,0,7] + Numero[3,1,7] + Numero[3,2,7] + Numero[4,0,7]
   + Numero[4,1,7] + Numero[4,2,7] + Numero[5,0,7] + Numero[5,1,7]
   + Numero[5,2,7] = 1
 R310: Numero[3,3,7] + Numero[3,4,7] + Numero[3,5,7] + Numero[4,3,7]
   + Numero[4,4,7] + Numero[4,5,7] + Numero[5,3,7] + Numero[5,4,7]
   + Numero[5,5,7] = 1
 R311: Numero[3,6,7] + Numero[3,7,7] + Numero[3,8,7] + Numero[4,6,7]
   + Numero[4,7,7] + Numero[4,8,7] + Numero[5,6,7] + Numero[5,7,7]
   + Numero[5,8,7] = 1
 R312: Numero[6,0,7] + Numero[6,1,7] + Numero[6,2,7] + Numero[7,0,7]
   + Numero[7,1,7] + Numero[7,2,7] + Numero[8,0,7] + Numero[8,1,7]
   + Numero[8,2,7] = 1
 R313: Numero[6,3,7] + Numero[6,4,7] + Numero[6,5,7] + Numero[7,3,7]
   + Numero[7,4,7] + Numero[7,5,7] + Numero[8,3,7] + Numero[8,4,7]
   + Numero[8,5,7] = 1
 R314: Numero[6,6,7] + Numero[6,7,7] + Numero[6,8,7] + Numero[7,6,7]
   + Numero[7,7,7] + Numero[7,8,7] + Numero[8,6,7] + Numero[8,7,7]
   + Numero[8,8,7] = 1
 R315: Numero[0,0,8] + Numero[0,1,8] + Numero[0,2,8] + Numero[1,0,8]
   + Numero[1,1,8] + Numero[1,2,8] + Numero[2,0,8] + Numero[2,1,8]
   + Numero[2,2,8] = 1
 R316: Numero[0,3,8] + Numero[0,4,8] + Numero[0,5,8] + Numero[1,3,8]
   + Numero[1,4,8] + Numero[1,5,8] + Numero[2,3,8] + Numero[2,4,8]
   + Numero[2,5,8] = 1
 R317: Numero[0,6,8] + Numero[0,7,8] + Numero[0,8,8] + Numero[1,6,8]
   + Numero[1,7,8] + Numero[1,8,8] + Numero[2,6,8] + Numero[2,7,8]
   + Numero[2,8,8] = 1
 R318: Numero[3,0,8] + Numero[3,1,8] + Numero[3,2,8] + Numero[4,0,8]
   + Numero[4,1,8] + Numero[4,2,8] + Numero[5,0,8] + Numero[5,1,8]
   + Numero[5,2,8] = 1
 R319: Numero[3,3,8] + Numero[3,4,8] + Numero[3,5,8] + Numero[4,3,8]
   + Numero[4,4,8] + Numero[4,5,8] + Numero[5,3,8] + Numero[5,4,8]
   + Numero[5,5,8] = 1
 R320: Numero[3,6,8] + Numero[3,7,8] + Numero[3,8,8] + Numero[4,6,8]
   + Numero[4,7,8] + Numero[4,8,8] + Numero[5,6,8] + Numero[5,7,8]
   + Numero[5,8,8] = 1
 R321: Numero[6,0,8] + Numero[6,1,8] + Numero[6,2,8] + Numero[7,0,8]
   + Numero[7,1,8] + Numero[7,2,8] + Numero[8,0,8] + Numero[8,1,8]
   + Numero[8,2,8] = 1
 R322: Numero[6,3,8] + Numero[6,4,8] + Numero[6,5,8] + Numero[7,3,8]
   + Numero[7,4,8] + Numero[7,5,8] + Numero[8,3,8] + Numero[8,4,8]
   + Numero[8,5,8] = 1
 R323: Numero[6,6,8] + Numero[6,7,8] + Numero[6,8,8] + Numero[7,6,8]
   + Numero[7,7,8] + Numero[7,8,8] + Numero[8,6,8] + Numero[8,7,8]
   + Numero[8,8,8] = 1
Bounds
 Numero[0,0,4] = 1
 Numero[0,1,2] = 1
 Numero[0,4,6] = 1
 Numero[1,0,5] = 1
 Numero[1,3,0] = 1
 Numero[1,4,8] = 1
 Numero[1,5,4] = 1
 Numero[2,1,8] = 1
 Numero[2,2,7] = 1
 Numero[2,7,5] = 1
 Numero[3,0,7] = 1
 Numero[3,4,5] = 1
 Numero[3,8,2] = 1
 Numero[4,0,3] = 1
 Numero[4,3,7] = 1
 Numero[4,5,2] = 1
 Numero[4,8,0] = 1
 Numero[5,0,6] = 1
 Numero[5,4,1] = 1
 Numero[5,8,5] = 1
 Numero[6,1,5] = 1
 Numero[6,6,1] = 1
 Numero[6,7,7] = 1
 Numero[7,3,3] = 1
 Numero[7,4,0] = 1
 Numero[7,5,8] = 1
 Numero[7,8,4] = 1
 Numero[8,4,7] = 1
 Numero[8,7,6] = 1
 Numero[8,8,8] = 1
Binaries
 Numero[0,0,0] Numero[0,0,1] Numero[0,0,2] Numero[0,0,3] Numero[0,0,4]
 Numero[0,0,5] Numero[0,0,6] Numero[0,0,7] Numero[0,0,8] Numero[0,1,0]
 Numero[0,1,1] Numero[0,1,2] Numero[0,1,3] Numero[0,1,4] Numero[0,1,5]
 Numero[0,1,6] Numero[0,1,7] Numero[0,1,8] Numero[0,2,0] Numero[0,2,1]
 Numero[0,2,2] Numero[0,2,3] Numero[0,2,4] Numero[0,2,5] Numero[0,2,6]
 Numero[0,2,7] Numero[0,2,8] Numero[0,3,0] Numero[0,3,1] Numero[0,3,2]
 Numero[0,3,3] Numero[0,3,4] Numero[0,3,5] Numero[0,3,6] Numero[0,3,7]
 Numero[0,3,8] Numero[0,4,0] Numero[0,4,1] Numero[0,4,2] Numero[0,4,3]
 Numero[0,4,4] Numero[0,4,5] Numero[0,4,6] Numero[0,4,7] Numero[0,4,8]
 Numero[0,5,0] Numero[0,5,1] Numero[0,5,2] Numero[0,5,3] Numero[0,5,4]
 Numero[0,5,5] Numero[0,5,6] Numero[0,5,7] Numero[0,5,8] Numero[0,6,0]
 Numero[0,6,1] Numero[0,6,2] Numero[0,6,3] Numero[0,6,4] Numero[0,6,5]
 Numero[0,6,6] Numero[0,6,7] Numero[0,6,8] Numero[0,7,0] Numero[0,7,1]
 Numero[0,7,2] Numero[0,7,3] Numero[0,7,4] Numero[0,7,5] Numero[0,7,6]
 Numero[0,7,7] Numero[0,7,8] Numero[0,8,0] Numero[0,8,1] Numero[0,8,2]
 Numero[0,8,3] Numero[0,8,4] Numero[0,8,5] Numero[0,8,6] Numero[0,8,7]
 Numero[0,8,8] Numero[1,0,0] Numero[1,0,1] Numero[1,0,2] Numero[1,0,3]
 Numero[1,0,4] Numero[1,0,5] Numero[1,0,6] Numero[1,0,7] Numero[1,0,8]
 Numero[1,1,0] Numero[1,1,1] Numero[1,1,2] Numero[1,1,3] Numero[1,1,4]
 Numero[1,1,5] Numero[1,1,6] Numero[1,1,7] Numero[1,1,8] Numero[1,2,0]
 Numero[1,2,1] Numero[1,2,2] Numero[1,2,3] Numero[1,2,4] Numero[1,2,5]
 Numero[1,2,6] Numero[1,2,7] Numero[1,2,8] Numero[1,3,0] Numero[1,3,1]
 Numero[1,3,2] Numero[1,3,3] Numero[1,3,4] Numero[1,3,5] Numero[1,3,6]
 Numero[1,3,7] Numero[1,3,8] Numero[1,4,0] Numero[1,4,1] Numero[1,4,2]
 Numero[1,4,3] Numero[1,4,4] Numero[1,4,5] Numero[1,4,6] Numero[1,4,7]
 Numero[1,4,8] Numero[1,5,0] Numero[1,5,1] Numero[1,5,2] Numero[1,5,3]
 Numero[1,5,4] Numero[1,5,5] Numero[1,5,6] Numero[1,5,7] Numero[1,5,8]
 Numero[1,6,0] Numero[1,6,1] Numero[1,6,2] Numero[1,6,3] Numero[1,6,4]
 Numero[1,6,5] Numero[1,6,6] Numero[1,6,7] Numero[1,6,8] Numero[1,7,0]
 Numero[1,7,1] Numero[1,7,2] Numero[1,7,3] Numero[1,7,4] Numero[1,7,5]
 Numero[1,7,6] Numero[1,7,7] Numero[1,7,8] Numero[1,8,0] Numero[1,8,1]
 Numero[1,8,2] Numero[1,8,3] Numero[1,8,4] Numero[1,8,5] Numero[1,8,6]
 Numero[1,8,7] Numero[1,8,8] Numero[2,0,0] Numero[2,0,1] Numero[2,0,2]
 Numero[2,0,3] Numero[2,0,4] Numero[2,0,5] Numero[2,0,6] Numero[2,0,7]
 Numero[2,0,8] Numero[2,1,0] Numero[2,1,1] Numero[2,1,2] Numero[2,1,3]
 Numero[2,1,4] Numero[2,1,5] Numero[2,1,6] Numero[2,1,7] Numero[2,1,8]
 Numero[2,2,0] Numero[2,2,1] Numero[2,2,2] Numero[2,2,3] Numero[2,2,4]
 Numero[2,2,5] Numero[2,2,6] Numero[2,2,7] Numero[2,2,8] Numero[2,3,0]
 Numero[2,3,1] Numero[2,3,2] Numero[2,3,3] Numero[2,3,4] Numero[2,3,5]
 Numero[2,3,6] Numero[2,3,7] Numero[2,3,8] Numero[2,4,0] Numero[2,4,1]
 Numero[2,4,2] Numero[2,4,3] Numero[2,4,4] Numero[2,4,5] Numero[2,4,6]
 Numero[2,4,7] Numero[2,4,8] Numero[2,5,0] Numero[2,5,1] Numero[2,5,2]
 Numero[2,5,3] Numero[2,5,4] Numero[2,5,5] Numero[2,5,6] Numero[2,5,7]
 Numero[2,5,8] Numero[2,6,0] Numero[2,6,1] Numero[2,6,2] Numero[2,6,3]
 Numero[2,6,4] Numero[2,6,5] Numero[2,6,6] Numero[2,6,7] Numero[2,6,8]
 Numero[2,7,0] Numero[2,7,1] Numero[2,7,2] Numero[2,7,3] Numero[2,7,4]
 Numero[2,7,5] Numero[2,7,6] Numero[2,7,7] Numero[2,7,8] Numero[2,8,0]
 Numero[2,8,1] Numero[2,8,2] Numero[2,8,3] Numero[2,8,4] Numero[2,8,5]
 Numero[2,8,6] Numero[2,8,7] Numero[2,8,8] Numero[3,0,0] Numero[3,0,1]
 Numero[3,0,2] Numero[3,0,3] Numero[3,0,4] Numero[3,0,5] Numero[3,0,6]
 Numero[3,0,7] Numero[3,0,8] Numero[3,1,0] Numero[3,1,1] Numero[3,1,2]
 Numero[3,1,3] Numero[3,1,4] Numero[3,1,5] Numero[3,1,6] Numero[3,1,7]
 Numero[3,1,8] Numero[3,2,0] Numero[3,2,1] Numero[3,2,2] Numero[3,2,3]
 Numero[3,2,4] Numero[3,2,5] Numero[3,2,6] Numero[3,2,7] Numero[3,2,8]
 Numero[3,3,0] Numero[3,3,1] Numero[3,3,2] Numero[3,3,3] Numero[3,3,4]
 Numero[3,3,5] Numero[3,3,6] Numero[3,3,7] Numero[3,3,8] Numero[3,4,0]
 Numero[3,4,1] Numero[3,4,2] Numero[3,4,3] Numero[3,4,4] Numero[3,4,5]
 Numero[3,4,6] Numero[3,4,7] Numero[3,4,8] Numero[3,5,0] Numero[3,5,1]
 Numero[3,5,2] Numero[3,5,3] Numero[3,5,4] Numero[3,5,5] Numero[3,5,6]
 Numero[3,5,7] Numero[3,5,8] Numero[3,6,0] Numero[3,6,1] Numero[3,6,2]
 Numero[3,6,3] Numero[3,6,4] Numero[3,6,5] Numero[3,6,6] Numero[3,6,7]
 Numero[3,6,8] Numero[3,7,0] Numero[3,7,1] Numero[3,7,2] Numero[3,7,3]
 Numero[3,7,4] Numero[3,7,5] Numero[3,7,6] Numero[3,7,7] Numero[3,7,8]
 Numero[3,8,0] Numero[3,8,1] Numero[3,8,2] Numero[3,8,3] Numero[3,8,4]
 Numero[3,8,5] Numero[3,8,6] Numero[3,8,7] Numero[3,8,8] Numero[4,0,0]
 Numero[4,0,1] Numero[4,0,2] Numero[4,0,3] Numero[4,0,4] Numero[4,0,5]
 Numero[4,0,6] Numero[4,0,7] Numero[4,0,8] Numero[4,1,0] Numero[4,1,1]
 Numero[4,1,2] Numero[4,1,3] Numero[4,1,4] Numero[4,1,5] Numero[4,1,6]
 Numero[4,1,7] Numero[4,1,8] Numero[4,2,0] Numero[4,2,1] Numero[4,2,2]
 Numero[4,2,3] Numero[4,2,4] Numero[4,2,5] Numero[4,2,6] Numero[4,2,7]
 Numero[4,2,8] Numero[4,3,0] Numero[4,3,1] Numero[4,3,2] Numero[4,3,3]
 Numero[4,3,4] Numero[4,3,5] Numero[4,3,6] Numero[4,3,7] Numero[4,3,8]
 Numero[4,4,0] Numero[4,4,1] Numero[4,4,2] Numero[4,4,3] Numero[4,4,4]
 Numero[4,4,5] Numero[4,4,6] Numero[4,4,7] Numero[4,4,8] Numero[4,5,0]
 Numero[4,5,1] Numero[4,5,2] Numero[4,5,3] Numero[4,5,4] Numero[4,5,5]
 Numero[4,5,6] Numero[4,5,7] Numero[4,5,8] Numero[4,6,0] Numero[4,6,1]
 Numero[4,6,2] Numero[4,6,3] Numero[4,6,4] Numero[4,6,5] Numero[4,6,6]
 Numero[4,6,7] Numero[4,6,8] Numero[4,7,0] Numero[4,7,1] Numero[4,7,2]
 Numero[4,7,3] Numero[4,7,4] Numero[4,7,5] Numero[4,7,6] Numero[4,7,7]
 Numero[4,7,8] Numero[4,8,0] Numero[4,8,1] Numero[4,8,2] Numero[4,8,3]
 Numero[4,8,4] Numero[4,8,5] Numero[4,8,6] Numero[4,8,7] Numero[4,8,8]
 Numero[5,0,0] Numero[5,0,1] Numero[5,0,2] Numero[5,0,3] Numero[5,0,4]
 Numero[5,0,5] Numero[5,0,6] Numero[5,0,7] Numero[5,0,8] Numero[5,1,0]
 Numero[5,1,1] Numero[5,1,2] Numero[5,1,3] Numero[5,1,4] Numero[5,1,5]
 Numero[5,1,6] Numero[5,1,7] Numero[5,1,8] Numero[5,2,0] Numero[5,2,1]
 Numero[5,2,2] Numero[5,2,3] Numero[5,2,4] Numero[5,2,5] Numero[5,2,6]
 Numero[5,2,7] Numero[5,2,8] Numero[5,3,0] Numero[5,3,1] Numero[5,3,2]
 Numero[5,3,3] Numero[5,3,4] Numero[5,3,5] Numero[5,3,6] Numero[5,3,7]
 Numero[5,3,8] Numero[5,4,0] Numero[5,4,1] Numero[5,4,2] Numero[5,4,3]
 Numero[5,4,4] Numero[5,4,5] Numero[5,4,6] Numero[5,4,7] Numero[5,4,8]
 Numero[5,5,0] Numero[5,5,1] Numero[5,5,2] Numero[5,5,3] Numero[5,5,4]
 Numero[5,5,5] Numero[5,5,6] Numero[5,5,7] Numero[5,5,8] Numero[5,6,0]
 Numero[5,6,1] Numero[5,6,2] Numero[5,6,3] Numero[5,6,4] Numero[5,6,5]
 Numero[5,6,6] Numero[5,6,7] Numero[5,6,8] Numero[5,7,0] Numero[5,7,1]
 Numero[5,7,2] Numero[5,7,3] Numero[5,7,4] Numero[5,7,5] Numero[5,7,6]
 Numero[5,7,7] Numero[5,7,8] Numero[5,8,0] Numero[5,8,1] Numero[5,8,2]
 Numero[5,8,3] Numero[5,8,4] Numero[5,8,5] Numero[5,8,6] Numero[5,8,7]
 Numero[5,8,8] Numero[6,0,0] Numero[6,0,1] Numero[6,0,2] Numero[6,0,3]
 Numero[6,0,4] Numero[6,0,5] Numero[6,0,6] Numero[6,0,7] Numero[6,0,8]
 Numero[6,1,0] Numero[6,1,1] Numero[6,1,2] Numero[6,1,3] Numero[6,1,4]
 Numero[6,1,5] Numero[6,1,6] Numero[6,1,7] Numero[6,1,8] Numero[6,2,0]
 Numero[6,2,1] Numero[6,2,2] Numero[6,2,3] Numero[6,2,4] Numero[6,2,5]
 Numero[6,2,6] Numero[6,2,7] Numero[6,2,8] Numero[6,3,0] Numero[6,3,1]
 Numero[6,3,2] Numero[6,3,3] Numero[6,3,4] Numero[6,3,5] Numero[6,3,6]
 Numero[6,3,7] Numero[6,3,8] Numero[6,4,0] Numero[6,4,1] Numero[6,4,2]
 Numero[6,4,3] Numero[6,4,4] Numero[6,4,5] Numero[6,4,6] Numero[6,4,7]
 Numero[6,4,8] Numero[6,5,0] Numero[6,5,1] Numero[6,5,2] Numero[6,5,3]
 Numero[6,5,4] Numero[6,5,5] Numero[6,5,6] Numero[6,5,7] Numero[6,5,8]
 Numero[6,6,0] Numero[6,6,1] Numero[6,6,2] Numero[6,6,3] Numero[6,6,4]
 Numero[6,6,5] Numero[6,6,6] Numero[6,6,7] Numero[6,6,8] Numero[6,7,0]
 Numero[6,7,1] Numero[6,7,2] Numero[6,7,3] Numero[6,7,4] Numero[6,7,5]
 Numero[6,7,6] Numero[6,7,7] Numero[6,7,8] Numero[6,8,0] Numero[6,8,1]
 Numero[6,8,2] Numero[6,8,3] Numero[6,8,4] Numero[6,8,5] Numero[6,8,6]
 Numero[6,8,7] Numero[6,8,8] Numero[7,0,0] Numero[7,0,1] Numero[7,0,2]
 Numero[7,0,3] Numero[7,0,4] Numero[7,0,5] Numero[7,0,6] Numero[7,0,7]
 Numero[7,0,8] Numero[7,1,0] Numero[7,1,1] Numero[7,1,2] Numero[7,1,3]
 Numero[7,1,4] Numero[7,1,5] Numero[7,1,6] Numero[7,1,7] Numero[7,1,8]
 Numero[7,2,0] Numero[7,2,1] Numero[7,2,2] Numero[7,2,3] Numero[7,2,4]
 Numero[7,2,5] Numero[7,2,6] Numero[7,2,7] Numero[7,2,8] Numero[7,3,0]
 Numero[7,3,1] Numero[7,3,2] Numero[7,3,3] Numero[7,3,4] Numero[7,3,5]
 Numero[7,3,6] Numero[7,3,7] Numero[7,3,8] Numero[7,4,0] Numero[7,4,1]
 Numero[7,4,2] Numero[7,4,3] Numero[7,4,4] Numero[7,4,5] Numero[7,4,6]
 Numero[7,4,7] Numero[7,4,8] Numero[7,5,0] Numero[7,5,1] Numero[7,5,2]
 Numero[7,5,3] Numero[7,5,4] Numero[7,5,5] Numero[7,5,6] Numero[7,5,7]
 Numero[7,5,8] Numero[7,6,0] Numero[7,6,1] Numero[7,6,2] Numero[7,6,3]
 Numero[7,6,4] Numero[7,6,5] Numero[7,6,6] Numero[7,6,7] Numero[7,6,8]
 Numero[7,7,0] Numero[7,7,1] Numero[7,7,2] Numero[7,7,3] Numero[7,7,4]
 Numero[7,7,5] Numero[7,7,6] Numero[7,7,7] Numero[7,7,8] Numero[7,8,0]
 Numero[7,8,1] Numero[7,8,2] Numero[7,8,3] Numero[7,8,4] Numero[7,8,5]
 Numero[7,8,6] Numero[7,8,7] Numero[7,8,8] Numero[8,0,0] Numero[8,0,1]
 Numero[8,0,2] Numero[8,0,3] Numero[8,0,4] Numero[8,0,5] Numero[8,0,6]
 Numero[8,0,7] Numero[8,0,8] Numero[8,1,0] Numero[8,1,1] Numero[8,1,2]
 Numero[8,1,3] Numero[8,1,4] Numero[8,1,5] Numero[8,1,6] Numero[8,1,7]
 Numero[8,1,8] Numero[8,2,0] Numero[8,2,1] Numero[8,2,2] Numero[8,2,3]
 Numero[8,2,4] Numero[8,2,5] Numero[8,2,6] Numero[8,2,7] Numero[8,2,8]
 Numero[8,3,0] Numero[8,3,1] Numero[8,3,2] Numero[8,3,3] Numero[8,3,4]
 Numero[8,3,5] Numero[8,3,6] Numero[8,3,7] Numero[8,3,8] Numero[8,4,0]
 Numero[8,4,1] Numero[8,4,2] Numero[8,4,3] Numero[8,4,4] Numero[8,4,5]
 Numero[8,4,6] Numero[8,4,7] Numero[8,4,8] Numero[8,5,0] Numero[8,5,1]
 Numero[8,5,2] Numero[8,5,3] Numero[8,5,4] Numero[8,5,5] Numero[8,5,6]
 Numero[8,5,7] Numero[8,5,8] Numero[8,6,0] Numero[8,6,1] Numero[8,6,2]
 Numero[8,6,3] Numero[8,6,4] Numero[8,6,5] Numero[8,6,6] Numero[8,6,7]
 Numero[8,6,8] Numero[8,7,0] Numero[8,7,1] Numero[8,7,2] Numero[8,7,3]
 Numero[8,7,4] Numero[8,7,5] Numero[8,7,6] Numero[8,7,7] Numero[8,7,8]
 Numero[8,8,0] Numero[8,8,1] Numero[8,8,2] Numero[8,8,3] Numero[8,8,4]
 Numero[8,8,5] Numero[8,8,6] Numero[8,8,7] Numero[8,8,8]
End
