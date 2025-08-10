tasks=[]
while True:
 print("1.Add Task:")
 print("2.Display Task:")
 print("3.Removed Task:")
 print("4.Exit:")

 select=input("enter a task:")

 if select=="1":
  task=input("Add a task:")
  tasks.append(task)
  print("task is added!")

 elif select=="2":
  print("your task:")
  for t in tasks:
   print(".",t)

 elif select=="3":
  print("removed your task:")
  for t in tasks:
   print("-",t)

 elif select=="4":
  print("see you soon!")
  break

 else:
  pass  