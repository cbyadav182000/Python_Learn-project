# write a prgram to fill in a letter templet given below with name and date.

letter='''Dear <|Name|>,
          You are selected!
          <|Date|> '''

print(letter.replace("<|Name|>","Chandrabhan").replace("<|Date|>","28 june 2024"))