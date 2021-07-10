def color_count(color):
  num_color=thread_sold_split.count(color)
  return num_color

#print(color_count('white'))

colors = ['red','yellow','green','white','black','blue','purple']
empty_colors=[]
thread_sold_split = ['white', 'white', 'blue', 'white', 'blue', 'white', 'white', 'yellow', 'purple', 'purple', 'yellow',
                     'purple', 'yellow', 'blue', 'blue', 'purple', 'blue', 'white', 'white', 'red', 'white', 'blue', 'red',
                     'blue', 'green', 'blue', 'green', 'blue', 'red', 'green', 'blue', 'red', 'black', 'black', 'yellow', 'white',
                     'black', 'yellow', 'white', 'black', 'yellow', 'green', 'green', 'yellow', 'green', 'yellow', 'blue', 'green',
                     'yellow', 'purple', 'blue', 'black', 'black', 'blue', 'black', 'blue', 'black', 'black', 'purple', 'black',
                     'purple', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'red', 'black', 'black', 'red',
                     'black', 'red', 'white', 'black', 'red', 'yellow', 'yellow', 'black', 'green', 'yellow', 'black', 'yellow', 'white',
                     'yellow', 'white', 'yellow', 'black', 'yellow', 'yellow', 'white', 'white', 'black', 'white', 'black', 'white', 'black',
                     'red', 'purple', 'purple', 'yellow', 'purple', 'yellow', 'green', 'purple', 'yellow', 'red', 'yellow', 'red', 'green', 'yellow',
                     'red', 'red', 'green', 'red', 'green', 'white', 'red', 'white', 'white', 'red', 'purple', 'purple', 'green', 'green', 'green',
                     'red', 'white', 'red', 'white', 'purple', 'red', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'green', 'green', 'yellow',
                     'green', 'yellow', 'blue', 'purple', 'purple', 'black', 'yellow', 'yellow', 'yellow', 'blue', 'green', 'green', 'white', 'white', 'blue',
                     'white', 'black', 'blue', 'green', 'green', 'yellow', 'green', 'yellow', 'black', 'green', 'green', 'green', 'purple', 'green', 'green', 'white', 'green', 'white', 'blue', 'green', 'white', 'blue']

for i in thread_sold_split:
    if i not in empty_colors:
        color=i
        count=color_count(i)
        sentence = "We sold {count} {color} threads today".format(count=count, color=color)
        empty_colors.append(i)
    print(sentence)

