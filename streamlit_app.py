import streamlit as st
import itertools

st.title('Pandigital Multiplication\nPuzzle 🧩')

st.image("problem.png")

message = False

if st.button("**Geneate solutions**"):
    digits = [0,1,2,3,4,5,6,7,8,9]
    permutations = list(itertools.permutations(digits))

    sl_no = 1

    for i in permutations:
        # Making two-gigit number from 0th to 1st index.
        a = i[0]*10 + i[1]
        # Making three-digit number from 2nd to 4th index.
        b = i[2]*100 + i[3]*10 + i[4]
        # Making five-digit number from 5th to 9th index.
        c = i[5]*10000 + i[6]*1000 + i[7]*100 + i[8]*10 + i[9]

        # Checking condition and printing the result.
        if a*b==c:
            if c < 10000:
                # If the product is a four-digit, this will add a leading zero to the output.
                st.write(sl_no, str(a),"X",str(b),"=",str(c).zfill(5))
            else:
                st.write(sl_no, str(a),"X",str(b),"=",str(c))
            sl_no+=1
    message = True

if message:
    st.markdown("""
                        <h1 style='font-size:50px;'>
                            Total of <span style='color:red;'>16</span> solutions found out of 3,628,800 permutaions.
                        </h1>
                    """, unsafe_allow_html=True)
