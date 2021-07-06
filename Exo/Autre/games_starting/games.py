def color_count(color):
  num_color=thread_sold_split.count(color)
  return num_color

#print(color_count('white'))

colors = ['red','yellow','green','white','black','blue','purple']
empty_colors=[]

for i in thread_sold_split:
  #print(i)
  if i not in empty_colors:
    color=i
    count=color_count(i)
    sentence = "We sold {count} {color} threads today".format(count=count, color=color)
    print(sentence)
    empty_colors.append(i)