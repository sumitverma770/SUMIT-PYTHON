import streamlit as st

st.title("demo app😀")

n1 = st.number_input('enter number')
n2 = st.number_input('enter another number')
c1, c2, c3,c4, c5, c6 = st.columns(6)
add = c1.button("Add")
sub =  c2.button('Subtract')
mul = c3.button("Multiply")
div = c4.button("Divide")
expo = c5.button("exponent")
mod = c6.button("modulus")
if add:
    r = int(n1) + int(n2)
    st.success(r)
if sub:
    r =int(n1) - int(n2)
    st.success(r)
if mul:
    r = int(n1) * int(n2)
    st.success(r)
if div:
    r = int(n1) / int(n2)
    st.success(r)
if expo :
    r = int(n1) ** int(n2)
    st.success(r)

if mod:
    r = int(n1) % int(n2)
    st.success(r)
