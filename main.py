def wordToPig( word, ending_if_initial_vocal ):
  if word[ 0 ] in [ 'a', 'e', 'i', 'o', 'u', 'h' ]:
    return word + ending_if_initial_vocal
  else:
    leading_cons = ''
    while word[ 0 ] not in [ 'a', 'e', 'i', 'o', 'u' ]:
      leading_cons += word[ 0 ]
      word = word[ 1: ]

    if leading_cons[ - 1 ] == 'c':
      leading_cons = leading_cons[ 0 : -1 ] + 's'

    return word + leading_cons + 'ay'

ending_when_vocal = input( 'Enter the ending sound when a word starts with a vocal (some piglatin versions make it "ay" while others make it "yay", "way", or even "hay" (blank = "ay"): ' )
if ending_when_vocal == '':
  ending_when_vocal = 'ay'
a = input( 'Enter a word to convert to piglatin (exit to finish): ' )
while a != 'exit':
  print( wordToPig( a, ending_when_vocal ) )
  a = input( 'Enter a word to convert to piglatin (exit to finish): ' )
