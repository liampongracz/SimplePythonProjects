import pandas.core.indexes.accessors
import pandas as pd
import streamlit as st
import altair as alt

# write header
st.write("""
# DNA Nucleotide Count App

This app counts the nucleotide composition of query DNA

""")

# input box

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# create text box, split the lines, exclude 'DNA query' from sequence, join lines
sequence = st.text_area("Sequnce imput", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

# print line
st.write("""
***
""")

# input header w/ input sequence
st.header('Input-DNA query')
sequence

# output - dna nucleotide count
st.header('Output-DNA nucleotide count')

st.subheader('Counts of Nucleotides via Dictionary')
# method below returns counts of nucleotides in dictionary
def nucleotide_count(seq):
    d = dict({
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    })
    return d

# use function
dna_counts = nucleotide_count(sequence)

#extract labels and values from dictionary
dna_label = list(dna_counts)
dna_values = list(dna_counts.values())

# display dictionary
dna_counts

st.subheader('Counts via DataFrame')
# create and transform data frame
df = pd.DataFrame.from_dict(dna_counts, orient = 'index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# display counts via barchart
st.subheader("Counts via barchart")
myChart = alt.Chart(df).mark_bar().encode(
     x = 'nucleotide',
     y = 'count'
)

myChart = myChart.properties(
    width=alt.Step(80)
)

st.write(myChart)
