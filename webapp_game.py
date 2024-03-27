from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import random
import math

def random_num():
    put_text('Enter the range taht you guse the Number..')

    lowe_bound = input('Enter the 1st number of range: ',type=NUMBER)
    styled_text_lower = f'''
<div style="border: 2px solid black; padding: 10px; width: 250px; text-align: center;">
    <span style="font-weight: bold; font-family: Arial, sans-serif; color:red;">Lower Number:{lowe_bound}</span><br>
   
</div>
'''
    put_html(styled_text_lower)

    # Taking Input uper Bound
    uper_bound = input('Enter the 2nd number of range: ',type=NUMBER)
    styled_text_upper = f'''
<div style="border: 2px solid black; padding: 10px; width: 250px; text-align: center;">
    <span style="font-weight: bold; font-family: Arial, sans-serif; color:red;">Upper Number:{uper_bound}</span><br>
   
</div>
'''
    put_html(styled_text_upper)
    guse_number = random.randint(lowe_bound,uper_bound)

    count=0
    chance = math.log(uper_bound-lowe_bound+1,2)
    put_text(f'You Have only {round(chance)} chance for guse the number')
    while True:
        while(count<chance):
            count+=1
            #taking gussing number as input
            user_guse = int(input('Guse A Number: '))

            #condition testing
            if user_guse >guse_number:
                put_text('Try Again! Your Guse too High...')
            elif user_guse <guse_number:
                put_text('Try again! your guse number too Short..')
            else: 
                put_text(f'Congrats! Your guse is correct, you try {count} times.')
                break
        put_text(f'You try {round(count,2)} time! Better Than next time')
        ans=input("Do You Want To Play AGin Y/N: ",type=TEXT)
        if ans == 'n' or ans =='N':
          break
        restart = put_buttons(['Restart'])
        if restart[restart]:
            random_num()
    # style(put_text("Thankx to play Game..."),'color:red;font-size:25px;')
    put_markdown("""
    <div style="border: 3px solid black; padding: 10px;">
        <p align='center' style="color: red; font-size: 25px;"><h2>Thankx to play Game...</h2></p>
    </div>
    """)


if __name__ == '__main__':
    random_num()

hold()
