#"w" สามารถเขียนทับไฟล์เดิมได้
with open("./files/output.txt", "w") as file:
    file.write("Hello!!!")
    
#ถ้าต้องการต่อท้าย ใช้ "a"

with open("./files/output.txt", "a") as file:
    file.write("\nTest failed")