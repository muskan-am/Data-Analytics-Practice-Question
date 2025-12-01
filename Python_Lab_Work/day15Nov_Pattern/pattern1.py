#Heart-like upside triangle shape

rows = 7          
max_stars = 13    

for i in range(rows):
    stars = max_stars - 2 * i  
    spaces = (max_stars - stars) 
    print(" " * spaces + "* " * stars)

