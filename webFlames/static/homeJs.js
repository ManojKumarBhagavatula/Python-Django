function displayNames() {
    var name1 = document.getElementById("name1").value;
    var name2 = document.getElementById("name2").value;

    document.getElementById("result").style.display = "block";

    const uncommonInfo = calculateUncommonLetters(name1, name2);
    document.getElementById("uncommonLettersDisplay").textContent = uncommonInfo;

    // Call the modified calcFlames function
    calcFlames(uncommonInfo);
}


function calculateUncommonLetters(name1, name2) {
    const name1Array = name1.toLowerCase().replace(/[^a-z]/g, "").split('');
    const name2Array = name2.toLowerCase().replace(/[^a-z]/g, "").split('');

    for (let i = 0; i < name1Array.length; i++) {
        for (let j = 0; j < name2Array.length; j++) {
            if (name1Array[i] === name2Array[j]) {
                name1Array[i] = '0';
                name2Array[j] = '0';
                break;
            }
        }
    }

    let count = 0;

    for (let i = 0; i < name1Array.length; i++) {
        if (name1Array[i] !== '0') {
            count++;
        }
    }

    for (let i = 0; i < name2Array.length; i++) {
        if (name2Array[i] !== '0') {
            count++;
        }
    }

    return count;
}

function calcFlames(count) {
    const flames = ['F', 'L', 'A', 'M', 'E', 'S'];
    const remainingLetterIndex = (count - 1) % flames.length;
    const remainingLetter = flames[remainingLetterIndex];

    let currentIndex = 0;
    const displayElement = document.getElementById("uncommonLettersDisplay");

    const interval = setInterval(() => {
        if (currentIndex !== remainingLetterIndex) {
            flames[currentIndex] = ' ';
            currentIndex = (currentIndex + 1) % flames.length;
            displayElement.textContent = flames.join(" ");
        } else {
            clearInterval(interval);
            displayElement.textContent = remainingLetter;
        }
    }, 1000); // Adjust the interval duration as needed
}




