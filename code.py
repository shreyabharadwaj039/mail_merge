CONTENT="[name]"

with open ("mail_merge/names.txt") as name_file:
  names=name_file.readlines()
  
with open ("mail_merge\mail.txt") as mail_file:
  content= mail_file.read()
  
  for name in names:
    y=name.strip()
    x=content.replace(CONTENT,y)
    with open(f"mail_merge/Ready_to_send_to/letter_to_{y}.txt", mode="w") as completed:
      completed.write(x)
    
  