# DNA Sequence Translator
Inputted DNA sequence filters through organism genomes from Genbank files for matching sequence in a protein. Once the sequence matches a portion of the corresponding protein CDS (coding sequence) region, the function will return the organism and location the sequence was found at in the protein.


Organism genomes were obtained using GenBank files from NCBI, <br/> i.e. [complete genome for Paramecium bursaria Chlorella virus](https://www.ncbi.nlm.nih.gov/nuccore/NC_000852.5)


Submitting ``'CGCAGGCGCT'`` will return <br/> 
in protein ``'YP_004678872.1'`` <br/> 
in organism ``'NC_000852.5'`` <br/>
at location ``'1370..1380'``

Celery asynchronous architecture![image](https://user-images.githubusercontent.com/55855284/147890723-8d00a4bf-256a-4067-8e03-88a639a666f6.png)


# Resources
Utilized `BioPython` library and `SeqIO` to parse `genbank` files that store sequence data, representing nucleotide sequences. <br/> 
Asynchronous search capabilities with celery and Redis as message broker and result store. <br/> 
React frontend uses local storage to persist searched sequences and generated results.

# To run
``cd ./frontend`` <br/>
``npm start``

# To run tests
``cd ./frontend`` <br/>
``npm run test``

# Available on
UI ``http://localhost:3000/`` <br/> and <br/> 
API ``http://localhost:8000/api/:DNASequence``
<br/> to get results from Celery TaskResult table <br/> 
Results ``http://localhost:8000/api/results/tasks``

# Hosted on
UI ``https://ginkgo-take-home.herokuapp.com`` 
    <br/> and <br/> 
API ``https://ginkgo-back-end.herokuapp.com/api/:DNASequence``
    <br/> to get results from Celery TaskResult table <br/> 
Results ``https://ginkgo-back-end.herokuapp.com/results/tasks``
