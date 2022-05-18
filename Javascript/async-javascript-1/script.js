import fetch from "node-fetch";
// SetTimeout
// setTimeout(() => {
//     console.log("Waited for 1 second")
// }, 1000);


// Promise
// const myPromise = new Promise((resolve, reject) => {
//     const rand = Math.random();
//     if (rand > 0.5) {
//         resolve();
//     } else {
//         reject();
//     }
// });

// myPromise.then(() => console.log('Success')).catch(() => {
//     console.log("Error occured");
// });

// Fetch with promises
// fetch('https://pokeapi.co/api/v2/pokemon/ditto')
//     .then((res) => res.json())
//     .then((data) => console.log(data))
//     .catch((err) => console.log(err)); 

// Updates fetch

const fetchPokemon = async (id) => {
    try {
        const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        const data = await res.json();
        console.log(data);
    } catch(err) {
        console.error(err);
    }
}

fetchPokemon(2);