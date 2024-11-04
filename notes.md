Libraries/dependencies:
- mediapipe : detect hands and fingers. determines this from data of joints from each finger. helps you see and count which finger is raised or not (rock would have no fingers displayed, paper would have all (?) and scissors 2)-tracks 3d hand landmarks. Does the machine learning stuff of indentifying hands and fingers.

-OpenCV-python : computer vision library- so I can use/access computer cam (mediapipe alone doesn't have built-in fucntionality for camera input) Can also draw on top to outlinw/highlight the joints and fingers on screen/display


steps:
1) Use mediapipe/openCV :
-detect which hand landmarks would be rock, paper and scissors and store this


2) Refactor old javascript rock-paper scissors app into python (random generated rock paper and scissors from computer, compare this to user, store the outcome and store the number of rounds played)

//Change number input into rock paper or scissors
//To simplify we are going to start off with numbers representing each item, but later on we will chnage this if we have time
//1 = rock
//2 = paper
//3 = scissors

//function to determine winner
function getWinner(playerInputVariable, computerInputVariable)
{
    //Draw
    if (playerInputVariable === computerInputVariable) {
        playerScore.playerDraws++;
        playerScore.gamesPlayed++;
        return "Draw";
    }

    //Win
    else if (playerInputVariable === 1 && computerInputVariable === 3) {
        playerScore.playerWins++;
        playerScore.gamesPlayed++;
        return "Win";
    }

    else if (playerInputVariable === 2 && computerInputVariable === 1) {
        playerScore.playerWins++;
        playerScore.gamesPlayed++;
        return "Win";
    }

    else if (playerInputVariable === 3 && computerInputVariable === 2) {
        playerScore.playerWins++;
        playerScore.gamesPlayed++;
        return "Win";
    }

    //Lose
    else {
        playerScore.playerLosses++;
        playerScore.gamesPlayed++;
        return "Lose";
    }
}
//function to generate random computer number
function generateNum(){
return Math.floor(Math.random() * 3) + 1;
//This generates a random number between 1 and 3
}
//check username is less than 10 characters
function checkUserName (name) {
if (name.length >= 10) {
 alert('The name exceeds the character limit. Please refresh the webpage to try again.'); 
 playAgain = false; 
}

}

let playerScore = {
    playerWins:0, 
    playerDraws:0,
    playerLosses:0,
    gamesPlayed: 0};// setting up the score system 

let playAgain = true;
let playerUser = prompt('Welcome to Rock, Paper and Scissors. Please enter your name. (Ensure that this is no longer than 10 characters)')
checkUserName(playerUser)

while (playAgain === true){
    //Inputting both the users answer and computers random answer
    let playerInputVariable1 = Number(prompt(`Hi ${playerUser}! Using the key shown below, please type in 1, 2 or 3.Key: rock = 1 paper = 2 scissors = 3 `));
    console.log(typeof playerInputVariable1);
    //Checks player has entered 1, 2 or 3
    if (playerInputVariable1 != 1 && playerInputVariable1 != 2 && playerInputVariable1 != 3) {
        alert("Input not allowed, please refresh and try again");
        break;
    }

let computerInputVariable1 = generateNum()
    let result = getWinner(playerInputVariable1, computerInputVariable1);
    alert(`You ${result}, ${playerUser} `)

playAgain = confirm(`You won: ${playerScore.playerWins} times. You drew ${playerScore.playerDraws} times. You lost ${playerScore.playerLosses} times. Do you want to play again?`);
  if (playAgain===false) {
    alert(`Game over. You played a total of ${playerScore.gamesPlayed} games. Refresh the game if you change your mind and want to play again.`
    )
  }
}

//Computer win half the time statistically
//Everytime player plays, computer generates a number between 1 and 2 in a new variable
//If 2 then computers choice is the winning choice

//Computer win half the time alternating
//If it loses, then the computer will choose winning option next turn

3) FUTURE:
-Can I turn this into an app?
-Can you play against other players instead of just computer

-SEPARATE PROJECT :Research the library capabilities, can I feed in scans of stained bone marrow samples and see if I can get a basic cell count? this already exists- but I want to see how this works, maybe have an analysis of home accurate it is depending on the staining and slide quality. 

MVP1:

//Need to find out how to access my laptop camera to my laptop (using open cv)

//Use openCV for video processing, we need to access each frame from processing

//give these frames to mediapipe

MVP2:

//Need to then use mediapipe hands detetection and landmark tracking 

//Use OpenCV’s image display and drawing to show the hand landmarks 

MVP3:

//Use mediapipe hand and hand landmark tracking to determine how many fingers are being helld up and depending on this, we can assign the number of fingers being held up to whether a user is showing rock paper or scissors

MVP4:

//Refactor the old rock paper scissors code and just use basic functionality of determining what user is showing (rock paper or scissors)