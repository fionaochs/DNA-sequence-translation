# DNA Sequence Translator
Inputted DNA sequence is found at a specific location in the corresponding protein, that is then mapped to an organism, by searching through list of genomes for the organism and location that the sequence was found at.
Utilized CDS (coding sequence) regions, to get the translateed protein name from the DNA sequence.

Organism genomes were obtained using GenBank files from NCBI, <br/> i.e. [complete genome for Paramecium bursaria Chlorella virus](https://www.ncbi.nlm.nih.gov/nuccore/NC_000852.5)

i.e. <br/>
Submitting ``'CGCAGGCGCT'`` will return <br/> 
in protein ``'YP_004678872.1'`` <br/> 
in organism ``'NC_000852.5'`` <br/>
at location ``'1370..1380'``

celery asynchronous architecture![image](https://user-images.githubusercontent.com/55855284/147863657-5c7f9b92-f9de-4f85-9750-940e8ac0dac3.png)


# Resources
Utilized `BioPython` library and `SeqIO` to parse `genbank` files that store sequence data, representing nucleotide sequences.
Asynchronous search capabilities with celery and Redis as message broker and result store.
React frontend uses local storage to persist searched sequences and generated results.

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
