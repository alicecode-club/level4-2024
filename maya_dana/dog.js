let num=-1;
async function CuteDogs(){
        num=num+1;
        const response = await fetch("https://api.thedogapi.com/v1/images/search");
        const data = await response.json();
        const processed = data[0].url;
        console.log(processed);
        let dog= document.createElement("img");
        dog.setAttribute ('src', processed);
        dog.setAttribute('height', 500);
        dog.setAttribute('alt', 'nature');
        dog.setAttribute('id', num);
        dog.setAttribute('class', "DoggtImg");
        document.getElementById("a").appendChild(dog);
}

CuteDogs()

async function random() {
    for (save=0; save<=num; save++ ) {
        console.log(save);
        const response2 = await fetch("https://api.thedogapi.com/v1/images/search");
        const data2 = await response2.json();
        const processed2 = data2[0].url;
        document.getElementById(save).setAttribute ('src', processed2);
    }
}

// async function CuteDogs(){
//    var num= document.getElementById("num").value;
//        const response = await fetch("https://api.thedogapi.com/v1/images/search");
//        const data = await response.json();
//        const processed = data[0].url;
//        console.log(processed);
//        let dog= document.getElementById("DoggyImg");
//        dog.src= processed;
//}

// CuteDogs()
