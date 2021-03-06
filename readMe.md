# DNA Sequence Translator
Inputted DNA sequence filters through organism genomes from Genbank files for matching sequence in a protein. Once the sequence matches a portion of the corresponding protein CDS (coding sequence) region, the function will return the organism and location the sequence was found at in the protein.


Organism genomes were obtained using GenBank files from NCBI, <br/> i.e. [complete genome for Paramecium bursaria Chlorella virus](https://www.ncbi.nlm.nih.gov/nuccore/NC_000852.5)


Submitting ``'CGCAGGCGCT'`` will return <br/> 
in protein ``'YP_004678872.1'`` <br/> 
in organism ``'NC_000852.5'`` <br/>
at location ``'1370..1380'``

![image](https://user-images.githubusercontent.com/55855284/148847834-a8e479e4-ac90-4d03-835d-bc0a6ae17f34.png)

Celery asynchronous architecture![image](https://user-images.githubusercontent.com/55855284/147893245-450e234e-c266-462a-b1b0-279c01837733.png)


# Resources
Utilized `BioPython` library and `SeqIO` to parse `genbank` files that store sequence data, representing nucleotide sequences. <br/> 
Asynchronous search capabilities with celery and Redis as message broker and result store. <br/> 
React frontend uses local storage to persist searched sequences and generated results.

# To run locally
Have instance of React app, server, and celery worker running

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
``npm run test`` <br/>
<img src="https://user-images.githubusercontent.com/55855284/148110251-ab88919d-d765-4ffd-a1a5-48a2feab156e.png" width="350" height="200" />

# Available on
UI ``http://localhost:3000/`` <br/> and <br/> 
API ``http://localhost:8000/api/:DNASequence``
<br/> to get results from Celery TaskResult table <br/> 
 ``http://localhost:8000/api/results/tasks``
