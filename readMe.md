# DNA Sequence Translator
Inputted DNA sequence filters through organism genomes from Genbank files for matching sequence in a protein. Once the sequence matches a portion of the corresponding protein CDS (coding sequence) region, the function will return the organism and location the sequence was found at in the protein.


Organism genomes were obtained using GenBank files from NCBI, <br/> i.e. [complete genome for Paramecium bursaria Chlorella virus](https://www.ncbi.nlm.nih.gov/nuccore/NC_000852.5)


Submitting ``'CGCAGGCGCT'`` will return <br/> 
in protein ``'YP_004678872.1'`` <br/> 
in organism ``'NC_000852.5'`` <br/>
at location ``'1370..1380'``

Celery asynchronous architecture![image](https://user-images.githubusercontent.com/55855284/147893245-450e234e-c266-462a-b1b0-279c01837733.png)


# Resources
Utilized `BioPython` library and `SeqIO` to parse `genbank` files that store sequence data, representing nucleotide sequences. <br/> 
Asynchronous search capabilities with celery and Redis as message broker and result store. <br/> 
React frontend uses local storage to persist searched sequences and generated results.

# To run React app
``cd ./frontend`` <br/>
``npm start``

# To run celery worker
``cd ./backend`` <br/>
``pipenv shell`` <br/>
``celery -A sequences_api  worker -l info``

# To run Django server
``cd ./backend`` <br/>
``pipenv shell`` <br/>
``pip install -r requirements.txt`` <br/>
``python manage.py runserver``

# To run tests
``cd ./frontend`` <br/>
``npm run test``

# Available on
UI ``http://localhost:3000/`` <br/> and <br/> 
API ``http://localhost:8000/api/:DNASequence``
<br/> to get results from Celery TaskResult table <br/> 
 ``http://localhost:8000/api/results/tasks``

# Hosted on
UI ``https://ginkgo-take-home.herokuapp.com`` 
    <br/> and <br/> 
API ``https://ginkgo-back-end.herokuapp.com/api/:DNASequence``
    <br/> to get results from Celery TaskResult table <br/> 
 ``https://ginkgo-back-end.herokuapp.com/results/tasks``
