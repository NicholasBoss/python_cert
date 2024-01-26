days = ['first','second','third','fourth'       \
       ,'fifth','sixth','seventh','eighth'      \
       ,'nineth','tenth','eleventh','twelveth']
 
verse = ['partridge in a pear tree.'     \
        ,'Two turtle doves,'             \
        ,'Three French hens,'            \
        ,'Four calling birds,'           \
        ,'Five gold rings,'              \
        ,'Six geese a-laying,'           \
        ,'Seven swans a-swimming,'       \
        ,'Eight maids a-milking,'        \
        ,'Nine ladies dancing,'          \
        ,'Tenth lords a-leaping,'        \
        ,'Eleven pipers piping,'         \
        ,'Twelve drummers drumming,']
 
# Loop forward, couple inner loop, and loop backward through list.
for i in range(0,len(days), 1):
  print("On the",str(days[i]),"day of Christmas my true love sent to me")
  for j in range(i, -1, -1):
    if (j > 0):
      print(" ",verse[j])
    elif (i == j):
      print("  A",verse[j])
    else:
      print("  and a",verse[j])