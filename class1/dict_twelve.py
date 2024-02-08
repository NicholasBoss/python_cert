lyric = {'first':'partridge in a pear tree.'
        ,'second':'Two turtle doves,'
        ,'third':'Three French hens,'
        ,'fourth':'Four calling birds,'
        ,'fifth':'Five gold rings,'
        ,'sixth':'Six geese a-laying,'
        ,'seventh':'Seven swans a-swimming,'
        ,'eighth':'maids a-milking,'
        ,'nineth':'Nine ladies dancing,'
        ,'tenth':'Ten lords a-leaping,'
        ,'eleventh':'Eleven pipers piping,'
        ,'twelfth':'Twelve drummers drumming,'}
 
# Intiate a list for collecting stanza.
stanza = list()
 
# Generate a list of keys.
for i in lyric.keys():
  # Append keys to list of stanza.
  stanza.append(i)
 
  # Print the first line of each stanza.
  print("On the",i,"day of Christmas my true love sent to me")
 
  # Print the progressive stanza.
  for j in reversed(stanza):
    if (j not in ['first','twelveth']):
      print(" ",lyric[j])
    elif (i == j):
      print("  A",lyric[j])
    else:
      print("  and a",lyric[j])