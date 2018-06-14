import stack
st = stack.stack()
print("size: {}".format(st.get_size()))
print("{}".format(st.get_stacked()))

st.push(1)
print("size: {}".format(st.get_size()))
print("{}".format(st.get_stacked()))

st.push(5)
st.push(24)
print("size: {}".format(st.get_size()))
print("{}".format(st.get_stacked()))

for i in range(10):
    st.push(i * 3)
print("size: {}".format(st.get_size()))
print("{}".format(st.get_stacked()))
