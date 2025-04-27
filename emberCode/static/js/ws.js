// // Socket.io Variables
// import { gamepads } from "./ctrl.js";
// const socket = io('http://127.0.0.1:5000'); // Init and connect socketio client

// socket.on('connect',function(){
//     // A sort of hand shake to tell the server to send Data 
//     socket.send('ctrl');
//     document.getElementById("robotStatus").innerHTML =  "WSIO Status: Connected";
// })

// socket.on('message',function(msg){
//     // Receiving data and asking for data back, will also serve as the controller feedback and accumulation  
//     // console.log("Step 2 receive Array data via WS")
//     if (msg.length != 0 ){
//         document.getElementById("displayVoltage").innerHTML = msg[0];
//         document.getElementById("displayTemp").innerHTML = msg[1];
//         document.getElementById("displayHumidity").innerHTML = msg[2];
//         document.getElementById("xTilt").innerHTML = msg[3];
//         document.getElementById("yTilt").innerHTML = msg[4];
//         document.getElementById("zTilt").innerHTML = msg[5];
//         document.getElementById("xAccel").innerHTML = msg[6];
//         document.getElementById("yAccel").innerHTML = msg[7];
//         document.getElementById("zAccel").innerHTML = msg[8];
//         document.getElementById("xMag").innerHTML = msg[9];
//         document.getElementById("yMag").innerHTML = msg[10];
//         document.getElementById("zMag").innerHTML = msg[11];
//         document.getElementById("gps").innerHTML = msg[12];
//         document.getElementById("range").innerHTML = msg[13];

//         // console.log("Step 3: Finished changing HTML Data")
//     } else {
//         alert("Unexpected Signal... System my need to be reset. \nProceed With Caution.");
//     }
    

//     if (gamepads[0].connected){
//       // Drive
//       leftDrive = getAnalog((((gamepads[0].axes[1])*-50)+50).toFixed(0)); // Left
//       rightDrive = getAnalog((((gamepads[0].axes[3])*-50)+50).toFixed(0)); // Right
//       leftAnalog.textContent = leftDrive;
//       rightAnalog.textContent = rightDrive;


//     // controllerCode to send to python
//     controllerCode = [leftDrive, rightDrive, pitch, userReadyToFire, armSend]; 
//     console.log(controllerCode);
//     socket.send(controllerCode); // Send out to Receive more
  
//     }

// })

// socket.on('disconnect',function(){
//     document.getElementById("robotStatus").innerHTML =  "WSIO Status: Failed";
//     socket.send("150500000");
// })


