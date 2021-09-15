pre_text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged.
'''

print(pre_text.lower())

print(pre_text.title())


lower_str = pre_text.lower()
count = 0
for i in lower_str:
    if i == 't':
        count += 1

print((f"Co {count} chu t"))
