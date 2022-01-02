# DNA Sequence Translator
Converts inputted DNA sequence to the corresponding Amino Acid sequence, then searches through list of genomes for the specific organism and location that the sequence was found at.
DNA transcription converts DNA sequence to mRNA which is translated to sequence of amino acids, or polypeptide.

i.e. <br/>
Submitting ``'AAGGTCGCCTCGGTGTC'`` will return <br/> 
amino acid sequence ``'KVASV'`` <br/> 
in organism ``'NC_009899.1'`` <br/>
at location ``'331..348'``

celery asynchronis architecture![image](https://user-images.githubusercontent.com/55855284/147863657-5c7f9b92-f9de-4f85-9750-940e8ac0dac3.png)



# Resources
Utilized `BioPython` library to parse `.fasta` files that store sequence data, representing nucleotide sequences.

# To run
``cd ./frontend`` <br/>
``npm start``

# To run tests
``cd ./frontend`` <br/>
``npm run test``

# Available on
``http://localhost:3000/`` <br/> and <br/> ``http://127.0.0.1:8000/api/:DNASequence``

# Hosted on
``https://ginkgo-take-home.herokuapp.com`` 
    <br/> and <br/> 
``https://ginkgo-back-end.herokuapp.com/api/:DNASequence``
