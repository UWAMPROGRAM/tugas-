#queue
queue = []

def isEmpty(q):
  if len(q) == 0:
    print("Queue Empty")
    return True
  return False

def enqueue(q):
  p = input("Add: ")
  q.append(p)
  print(f"{p} added")

def dequeue(q):
  if isEmpty(q) == False:
    print(q.pop(0), "removed")

def front(q):
  if isEmpty(q) == False:
    print('front item:', q[0])

def rear(q):
  if isEmpty(q) == False:
    print("rear item:", q[-1])

while True:
  perintah = input("(Dequeue/Enqueue/Front/Rear), ketik selain itu untuk berhenti: ").lower()
  
  if perintah == 'enqueue':
    enqueue(queue)
  elif perintah == 'dequeue':
    dequeue(queue)
  elif perintah == 'front':
    front(queue)
  elif perintah == 'rear':
    rear(queue)
  else:
    break

print("Queue items:", queue)

stack=[]
max_size=int(input("masukkan ukuran maksimal stack: "))
def isEmpty():
  if len(stack)==0:
    print("stack kosong")
    return True
  return False

def isFull():
  if len(stack)==max_size:
    print("stack penuh")
    return True
  return False

def pop():
   if isEmpty()== False:
     print(stack.pop(),"terhapus")

def push():
   if isFull()==False:
     a=input("masukkan itembaru: ")
     stack.append(a)
     print(a,"ditambahkan")

def peek():
   if isEmpty()==False:
      print("Top:",stack[-1])

  
p = 0
while p!='6':
  print('''\n1.Push => Menambah Item 
2.Pop => Menghapus Item
3.Peek => Melihat Item Teratas
4.Empty => Memeriksa Apakah Stack Penuh 
5.Size => Melihat Ukuran Stack''')
  p= input("ketik 6 untuk berhenti\nMasukkan Perintah: ")
  print()

  if p=='1':
    push()
  elif p=='2':
    pop()
  elif p=='3':
     
    peek()
  elif p=='4':
    if isEmpty()==false:
      print("stack memiliki isi.")
  elif p=='5':
    print("ukuran stack saat ini:",len(stack),"\nUkuran maksimal stack:",max_size)
  else:
    break