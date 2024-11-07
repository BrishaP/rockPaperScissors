Libraries/dependencies:
- mediapipe : detect hands and fingers. determines this from data of joints from each finger. helps you see and count which finger is raised or not (rock would have no fingers displayed, paper would have all (?) and scissors 2)-tracks 3d hand landmarks. Does the machine learning stuff of indentifying hands and fingers.

-OpenCV-python : computer vision library- so I can use/access computer cam (mediapipe alone doesn't have built-in fucntionality for camera input) Can also draw on top to outlinw/highlight the joints and fingers on screen/display

.Hands() has four default parameters

1. static_ image mode, It tracks and detects, false means sometimes it detects and sometimes it tracks
2. Max_min_hands
3. min_detection_confidence
4. mintracking_confidence

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


MVP3: determining what user has chosen 
THIS CONSIDERS THE Y COORDINATE OF THE FINGERTIP IN COMPARISON WITH THE Y CORRDINATE OF THE KNUCKLE 

FOR ROCK:
the finger tip coordinates need to be below the 'hand knuckle joints MCP landmarks: 5,9,13,17' (ignoring the thhumb)
- get the word 'rock' to display on the screen and then countdown from 5 to 'confirm' the user has chosen rock
-store this as user choice

FOR PAPER:
All finger tip landmark coordinates need to be above the knuckles (5,9,13,17 MCP) IGNORE THUMB
-get the word paper to display on the screen and then countdown from 5 to confirm the user has chosen paper
-store this as user choice

FOR SCISSORS:
only the 8 and 12 fingertips should be above the 5 and 9 MCP knuckles respectively, the 16 and 20 fingertips must be below the fingerknuckles. IGNORE THUMBS
-get the word scissors to display on the screen and then countdown from 5 to confirm the user has chosen scissors
-store this as user choice

mvp 4: 
Do the last bit where user and computer result is compared

mvp5:
determine the result

Store the result

Store the number of rounds

thumbs up if you want to play again
thumbs down if you don't want to play again

DONE THE MAIN GAME ASPECT 


FOR ROCK:



(if the Y coordinates of 8 (fingertip)  are less than Landmark 5 Y coordinates then=true

&&

if the Y coordinates of 12 (fingertip) are less than landmark 9 Y coordinates =true

&&

if the Y coordinates of 16 (fingertip) are less than landmark  13 y coordinates = true 

&&

if the Y coordinates of 20 (fingertip) are less than landmark 17 Y coordinates = true)

SO FAR ONLY STICK TO THE LEFT HAND, WE CAN INCORPORATE THE RIGHT HAND LATER ON

Structure of hand_landmarks
hand_landmarks is a NormalizedLandmarkList object.
Each element in hand_landmarks.landmark is a NormalizedLandmark object.
Each NormalizedLandmark object has the following attributes:
x: The normalized x-coordinate (ranging from 0 to 1).
y: The normalized y-coordinate (ranging from 0 to 1).
z: The normalized z-coordinate (ranging from 0 to 1).

for hand_landmarks in results.multi_hand_landmarks:
    RING_FINGER_TIP_Y = hand_landmarks.landmark[16].y
    RING_FINGER_MCP_Y = hand_landmarks.landmark[13].y

    PINKY_TIP_Y = hand_landmarks.landmark[20].y
    PINKY_MCP_Y = hand_landmarks.landmark[17].y

    MIDDLE_FINGER_TIP_Y = hand_landmarks.landmark[12].y
    MIDDLE_FINGER_MCP_Y = hand_landmarks.landmark[9].y

    INDEX_FINGER_TIP_Y = hand_landmarks.landmark[8].y
    INDEX_FINGER_MCP_Y = hand_landmarks.landmark[5].y

if PINKY_TIP_Y < PINKY_MCP_Y and \
   RING_FINGER_TIP_Y < RING_FINGER_MCP_Y and \
   MIDDLE_FINGER_TIP_Y < MIDDLE_FINGER_MCP_Y and \
   INDEX_FINGER_TIP_Y < INDEX_FINGER_MCP_Y:
    userChoice = "ROCK"

if PINKY_TIP_Y > PINKY_MCP_Y and \
   RING_FINGER_TIP_Y > RING_FINGER_MCP_Y and \
   MIDDLE_FINGER_TIP_Y > MIDDLE_FINGER_MCP_Y and \
   INDEX_FINGER_TIP_Y > INDEX_FINGER_MCP_Y:
    userChoice = "PAPER"

    if PINKY_TIP_Y < PINKY_MCP_Y and \
   RING_FINGER_TIP_Y < RING_FINGER_MCP_Y and \
   MIDDLE_FINGER_TIP_Y > MIDDLE_FINGER_MCP_Y and \
   INDEX_FINGER_TIP_Y > INDEX_FINGER_MCP_Y:
    userChoice = "SCISSORS"