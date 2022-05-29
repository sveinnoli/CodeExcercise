console.log("Start");

function loginUser(email,password) {
    return new Promise((resolve, reject) => {
         setTimeout(() => {
            return resolve( {userEmail: email, userPassword: password} );
        }, 1500);
    })
}

function getUserVideos(email) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(["video1", "video2", "video3"]);
        }, 1000);
    });
}

function videoDetails(video) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('title of the video');
        }, 2000)
    })
} 

// const user = loginUser("someguy@goolgool.dom", "12345abc", (user) => {
//     console.log(user)
//     getUserVideos(user.userEmail, (videos) => {
//         console.log(videos);
//         videoDetails(videos[0], (video) => {
//             console.log(video);
//         });
//     }) 
// });


// Same as above but with promises
loginUser('ed', 'bubma')
.then(user => getUserVideos(user.email))
.then(videos => videoDetails(videos[0]))
.then(detail => console.log(detail));

async function displayUser() {
    try {
        const user = await loginUser('Ed', 12345);
        const videos = await getUserVideos(user.userEmail);
        const details = await videoDetails(videos[0]);
        console.log(details); 
    } catch (err) {
        console.log(`Error occurred: ${err}`);
    }
}

displayUser();

// SYNC
// const user = await loginUser('ed', 'bumbajdads');
// const videos = await videoDetails(user.email);

// const yt = new Promise(resolve => {
//     setTimeout(() => {
//         console.log("Getting stuff from yt");
//         resolve({videos: [1,2,3,4,5]});
//     }, 2000)
// })


// const fb = new Promise(resolve => {
//     setTimeout(() => {
//         console.log("Getting stuff from fb");
//         resolve({user: "Name"});
//     }, 1000)
// })

// // Resolve both at same time
// Promise.all([yt, fb])
// .then((result) => console.log(result));

console.log("End");