print('Welcome how are you feeling today?: ')

while True:

   x1=int(input('Select 1 for Happy Select 2 for Sad :'))
   
   if(x1 == 2):
    print('I''m really sorry to know that you had a tough day')
    print('Here is something to cheer you up https://www.youtube.com/results?search_query=baby+funny+video')
    break
   elif(x1 == 1): 
    print('That is so good to know here is some amazing music to keep this mood alive https://www.youtube.com/results?search_query=when+chai+met+toast')
    break
   else:
     print('I don''t know how to respond to it, can you please select between 1 Happy or 2 Sad: ')

   continue



while True:
   a=int(input('Is there anything else to help you with? Press 1 for yes and 2 for no: '))
   if(a==1):
    print('Please select what I can help you with?')
    break
   elif(a==2):
    print('Thank you have a great day!')
    break
   else:
      print('You have entered an invalid option please select 1 yes or 2 no :')
      continue
if(a==1):
   while True:
      x = int(input('Please Select 1.Music 2.Funny 3. Inspirational :'))
      if(x==1):
         print('Here are the latest songs for you https://www.youtube.com/playlist?list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU')
         break
      elif(x==2):
       print('Here are some funny stand up''s for you https://www.youtube.com/playlist?list=PLw0OS4SJWbYBjpgcIQvCWyaffXd6w_DG4')
       break
      elif(x==3):
         print('Here are some inspiring videos for you https://www.youtube.com/playlist?list=PLcWa6kvxTA3Npc8MQiKG46f87iyZZQS1e') 
         break
      else:
         print('You have entered an invalid option, please select 1.Music 2. Funny 3. Inpirational: ')
         continue

print('Hope you feel more better today!, have a great day!!')


   


  


