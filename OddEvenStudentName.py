name = ['1.Laurence', '2.James', '3.Bob', '4.Owen', '5.Andro', '6.Jino', '7.Bobbie',
        '8.Julie', '9.Emman', '10.Redd', '11.Balon', '12.Sempi', '13.karding', 
        '14.Jassy', '15.Hector', '16.Leonardo', '17.Herold', '18.Sam', '19.Mica', '20.Beth']

print("List on Odd Numbers")
for i in range(len(name)):
        if i & 3 == 0:
          print(name[i])

print("List on Even Number")
i = 1
while i < len(name):
     print(name[i])
     i += 2