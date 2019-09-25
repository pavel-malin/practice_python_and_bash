
st = open("st.txt", "w")
st.write("Hello from Python")
st.close()

with open('st.txt', 'r') as f:
    print(f.read())