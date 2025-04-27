// HTML Casting Variables
const htmlRightAnalog = document.getElementById('rightDriveCtrl');
const htmlLeftAnalog = document.getElementById('leftDriveCtrl');
const htmlPitch = document.getElementById('pitchDriveCtrl');
const htmlYaw = document.getElementById('yawDriveCtrl');
const htmlLights = document.getElementById('lightsCtrl');
const htmlbaseAngle = document.getElementById('baseAngle');
const mapElement = document.getElementById("map");
const mapCurrentPosition = document.getElementById("currentPosition");
const mapTargetPosition = document.getElementById("targetPosition");

// Create Gamepad Constants
window.gamepads = null;
window.standardGamepad = null;
window.controllerCode = null;

// Define current payload variables
var currentPitch = 90;
var currentYaw = 90;
var currentBase = 10;
var currentDriveR = 0;
var currentDriveL = 0;
var currentLightsStatus = false;

// Check for initial gamepad connection
var haveEvents = 'GamepadEvent' in window; // is there a case of gamepad usage in the window
var haveWebkitEvents = 'WebKitGamepadEvent' in window;
var controllers = {};
var rAF = window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.requestAnimationFrame;

// Check for web browser support
if (haveEvents) {
  // Chrome and Firefox and Edge
  console.log("Use Chrome Firefox and Edge Framework")
  window.addEventListener("gamepadconnected", connectHandler);
  window.addEventListener("gamepaddisconnected", disconnectHandler);
} else if (haveWebkitEvents) {
  // Safari
  console.log("Safari")
  window.addEventListener("webkitgamepadconnected", connectHandler);
  window.addEventListener("webkitgamepaddisconnected", disconnectHandler);
} else {
  setInterval(scangamepads, 500);
  console.log("Looking for Gamepad");
}

// Gamepad Functions
function connectHandler(e) {
  addGamepad(e.gamepad);
}

function addGamepad() {
  console.log("New gamepad detected")
  gamepads = navigator.getGamepads();
    standardGamepad = {
        id: gamepads[0].id,
        Laxes: gamepads[0].axes[1].toFixed(2),
        Raxes: gamepads[0].axes[3].toFixed(2),
        ArmUp: gamepads[0].buttons[5].pressed,
        ArmDown: gamepads[0].buttons[4].pressed,
        FireOne: gamepads[0].buttons[3].pressed,
        FireTwo: gamepads[0].buttons[12].pressed,
        ctrlRetractArm: gamepads[0].buttons[9].pressed,
        ctrlDeployArm: gamepads[0].buttons[8].pressed
    } 
    document.getElementById("ctrlStatus").classList =  "btn btn-success";
    document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: ` + " The " + gamepads[0].id + " has connected successfully";
    socket.send("Controller Connected");
}

function disconnectHandler(e) {
    console.log("Gamepad Disconnected")
    document.getElementById("ctrlStatus").classList =  "btn btn-danger";
    document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: ` + "Gamepad Disconnected"
    removeGamepad(gamepads);
}

function removeGamepad(gamepads) {
    console.log("Gamepad is now disconnected and removed from cache")
  gamepads = null;
}

function updateStatus() {
  scanGamepads();
  for (j in controllers) {
    var controller = controllers[j];
    var d = document.getElementById("controller" + j);
    var buttons = d.getElementsByClassName("button");
    for (var i=0; i<controller.buttons.length; i++) {
      var b = buttons[i];
      var val = controller.buttons[i];
      var pressed = val == 1.0;
      var touched = false;
      if (typeof(val) == "object") {
        pressed = val.pressed;
        if ('touched' in val) {
          touched = val.touched;
        }
        val = val.value;
      }
      var pct = Math.round(val * 100) + "%";
      b.style.backgroundSize = pct + " " + pct;
      b.className = "button";
      if (pressed) {
        b.className += " pressed";
      }
      if (touched) {
        b.className += " touched";
      }
    }

    var axes = d.getElementsByClassName("axis");
    for (var i=0; i<controller.axes.length; i++) {
      var a = axes[i];
      a.innerHTML = i + ": " + controller.axes[i].toFixed(4);
      a.setAttribute("value", controller.axes[i]);
    }
  }
  rAF(updateStatus);
}

function scanGamepads() {
  var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads() : []);
  for (var i = 0; i < gamepads.length; i++) {
    if (gamepads[i] && (gamepads[i].index in controllers)) {
      controllers[gamepads[i].index] = gamepads[i];
    }
  }
}

function speedControl(anaNum) {
    var max = 0.2
    var deadzone = 0.05
   
    if (anaNum < -deadzone){
      if (Math.abs(anaNum) >= max) {
        return -max;
      } else {
        return anaNum;
      }
    } else if (anaNum >= -deadzone && anaNum <= deadzone) {
        return 0
    } else if (anaNum > deadzone){
      if (Math.abs(anaNum) >= max) {
        return max;
      } else {
        return anaNum;
      }
    } else {
      return 0
    }
  }

// Socket.io Variables
const serverIp = "{{ server_ip }}";
const socket = io(`https://fond-jointly-oryx.ngrok-free.app/`);
socket.on('connect',function(){
    document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: ` + "WSIO Status: Connected";
})

socket.on('message', function (msg) {
  if (msg.length != 0) {
    document.getElementById("displayVoltage").innerHTML = msg[0];
    document.getElementById("displayInternalTemp").innerHTML = msg[1];
    document.getElementById("displayInternalHumidity").innerHTML = msg[2];
    document.getElementById("displayExternalTemp").innerHTML = msg[3];
    document.getElementById("displayExternalHumidity").innerHTML = msg[4];
    document.getElementById("xTilt").innerHTML = msg[5];
    document.getElementById("yTilt").innerHTML = msg[6];
    document.getElementById("zTilt").innerHTML = msg[7];
    document.getElementById("xAccel").innerHTML = msg[8];
    document.getElementById("yAccel").innerHTML = msg[9];
    document.getElementById("zAccel").innerHTML = msg[10];
    document.getElementById("xMag").innerHTML = msg[11];
    document.getElementById("yMag").innerHTML = msg[12];
    document.getElementById("zMag").innerHTML = msg[13];
    document.getElementById("gpsLat").innerHTML = msg[14];
    document.getElementById("gpsLon").innerHTML = msg[15];
    document.getElementById("range").innerHTML = msg[16];
  } else {
    alert("Unexpected Signal... System may need to be reset. \nProceed With Caution.");
  }

  gamepads = navigator.getGamepads(); // Refresh the gamepads array
  if (gamepads[0] && gamepads[0].connected) {
    // Drive
    currentDriveL = speedControl(-1 * parseFloat(gamepads[0].axes[1].toFixed(2))); // Left
    currentDriveR = speedControl(-1 * parseFloat(gamepads[0].axes[3].toFixed(2))); // Right

    // Payload Trim
    var incSpeed = .49;
    if (gamepads[0].buttons[12].pressed) { // pitch up
      if (currentPitch > 178) {
        currentPitch = 178;
      } else {
        currentPitch = currentPitch + incSpeed;
      }
    }

    if (gamepads[0].buttons[13].pressed) { // pitch down
      if (currentPitch < 1) {
        currentPitch = 1;
      } else {
        currentPitch = currentPitch - incSpeed;
      }
    }

    if (gamepads[0].buttons[15].pressed) { // yaw left
      if (currentYaw > 178) {
        currentYaw = 178;
      } else {
        currentYaw = currentYaw + incSpeed;
      }
    }

    if (gamepads[0].buttons[14].pressed) { // yaw right
      if (currentYaw < 1) {
        currentYaw = 1;
      } else {
        currentYaw = currentYaw - incSpeed;
      }
    }

    if (gamepads[0].buttons[8].pressed) { // Retract Arm
      currentPitch = 90;
      currentYaw = 90;
      currentBase = 10;
      document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: Payload Set to Retract`;
    }
    if (gamepads[0].buttons[9].pressed) { // Deploy Arm
      currentPitch = 0;
      currentYaw = 90;
      currentBase = 90;
      document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: Payload Set to Deploy`;
    }

    // Lights
    if (gamepads[0].buttons[3].pressed) { // Lights On
      currentLightsStatus = true;
    }
    if (gamepads[0].buttons[0].pressed) { // Lights Off
      currentLightsStatus = false;
    }

    htmlLeftAnalog.textContent = currentDriveL;
    htmlRightAnalog.textContent = currentDriveR;
    htmlPitch.textContent = Math.round(currentPitch);
    htmlYaw.textContent = Math.round(currentYaw);
    htmlbaseAngle.textContent = currentBase;
    htmlLights.textContent = currentLightsStatus;

    // controllerCode to send to python
    controllerCode = [
      currentDriveL,
      currentDriveR,
      Math.round(currentPitch),
      Math.round(currentYaw),
      currentBase,
      currentLightsStatus
    ];
    console.log(controllerCode);
    socket.send(controllerCode); // Send out to Receive more
  }

  mapElement.setAttribute("center", `${msg[14]},${msg[15]}`);
  mapElement.setAttribute("zoom", `15`);
  mapCurrentPosition.setAttribute("position", `${msg[14]},${msg[15]}`);
});

socket.on('disconnect',function(){
    document.getElementById("robotStatus").innerHTML = `${new Date().toISOString()}: WSIO Status: Disconnected `;
})


