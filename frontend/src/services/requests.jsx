export const FetchResults = (proteinName) => {
    return fetch(`http://localhost:8000/api/${proteinName}`)
        .then(res => res.json())
        .then(json => json.map(protein => ({
            proteinId: protein.id,
            DNASequence: protein.sequence,
            proteinName: protein.proteinName,
            proteinLocation: protein.proteinLocation,
            organism: protein.organism
        })))
        .catch(res => console.log(res))
};
