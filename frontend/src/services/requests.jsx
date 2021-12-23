export const FetchResults = (proteinName) => {
    const formattedName = proteinName.toUpperCase();

    // production
    return fetch(`https://ginkgo-back-end.herokuapp.com/api/${proteinName}`)

        // development
        // return fetch(`http://localhost:8000/api/${formattedName}`)
        .then(res => res.json())
        .then(json => json.map(protein => ({
            proteinId: protein.id,
            DNASequence: protein.sequence,
            proteinName: protein.proteinName,
            proteinLocation: protein.proteinLocation,
            organism: protein.organism
        })))
        .catch(err => console.log(err))
};
