server_log = list(map(int,input("Enter the server logs: ").split()))
new = server_log[-5:]
print(f"Last 5: {new} | Critical Error Found: {500 in new}")