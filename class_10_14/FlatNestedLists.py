
home= []

list=[  [  [20] , [1,2,0],[5,6,14 ],[11,12,13],"zzz "  ],[[7,8],[9,10]],[[123,124]],12344,{},"blue",[4444,[[5555]]], [[["QQQ"]]],[[[["RRRR"]]]]     ]
for i in range (0,len(list)):
  if type(list[i])!= type(list):
      home.append(list[i])
  elif type(list[i])== type(list) :
     for j in range(0,len(list[i])):
         if type(list[i][j])!= type(list):
             home.append(list[i][j])
         elif type(list[i][j])==type(list):
            for k in range(0,len(list[i][j])):
              if type(list[i][j][k])!= type(list):
                 home.append(list[i][j][k])
              elif type(list[i][j][k])==type(list):
                  for l in range(0,len(list[i][j][k])):
                      if type(list[i][j][k][l])!= type(list):
                           home.append(list[i][j][k][l] )   # 5 level list test
                      elif type(list[i][j][k][l])== type(list):
                          home.append(list[i][j][k][l])


print(home)

