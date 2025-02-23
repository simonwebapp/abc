<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Drawing App</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: black;
    }
    /* Hide scrollbars for WebKit browsers */
    ::-webkit-scrollbar {
      display: none;
    }
    /* Canvas with a background image and custom red cursor */
    #canvas {
      display: block;
      width: 100vw;
      height: 100vh;
      background: url('https://simonbrun.no/BG.png') no-repeat center center;
      background-size: cover;
      cursor: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PGNpcmNsZSBjeD0iOCIgY3k9IjgiIHI9IjgiIGZpbGw9InJlZCIvPjwvc3ZnPg==") 8 8, auto;
    }
  </style>
</head>
<body>
  <canvas id="canvas" width="1920" height="1080"></canvas>
  <!-- Include Socket.IO client library -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.1/socket.io.min.js"></script>
  <script>
    const socket = io();
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let drawing = false;
    let paths = [];
    let currentPath = [];
    
    // Convert input coordinates to canvas coordinates,
    // taking into account the scaling between the intrinsic size (1920x1080) and displayed size.
    function getMousePos(evt) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      let x, y;
      if (evt.touches && evt.touches.length > 0) {
        x = evt.touches[0].clientX;
        y = evt.touches[0].clientY;
      } else {
        x = evt.clientX;
        y = evt.clientY;
      }
      return {
        x: (x - rect.left) * scaleX,
        y: (y - rect.top) * scaleY
      };
    }
    
    // Mouse events
    canvas.addEventListener('mousedown', (evt) => {
      drawing = true;
      currentPath = [];
      currentPath.push(getMousePos(evt));
    });
    
    canvas.addEventListener('mousemove', (evt) => {
      if (!drawing) return;
      currentPath.push(getMousePos(evt));
      redraw();
    });
    
    function endDrawing(evt) {
      if (!drawing) return;
      drawing = false;
      paths.push([...currentPath]);
      currentPath = [];
    }
    canvas.addEventListener('mouseup', endDrawing);
    canvas.addEventListener('mouseleave', endDrawing);
    
    // Touch events
    canvas.addEventListener('touchstart', (evt) => {
      evt.preventDefault();
      drawing = true;
      currentPath = [];
      currentPath.push(getMousePos(evt));
    });
    
    canvas.addEventListener('touchmove', (evt) => {
      evt.preventDefault();
      if (!drawing) return;
      currentPath.push(getMousePos(evt));
      redraw();
    });
    
    canvas.addEventListener('touchend', (evt) => {
      evt.preventDefault();
      if (!drawing) return;
      drawing = false;
      paths.push([...currentPath]);
      currentPath = [];
    });
    
    function redraw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.lineWidth = 4;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.strokeStyle = '#FFEA00';
      
      paths.forEach(path => {
        ctx.beginPath();
        path.forEach((point, i) => {
          if (i === 0) {
            ctx.moveTo(point.x, point.y);
          } else {
            ctx.lineTo(point.x, point.y);
          }
        });
        ctx.stroke();
      });
      
      if (currentPath.length) {
        ctx.beginPath();
        currentPath.forEach((point, i) => {
          if (i === 0) {
            ctx.moveTo(point.x, point.y);
          } else {
            ctx.lineTo(point.x, point.y);
          }
        });
        ctx.stroke();
      }
    }
    
    // Listen for the "clearCanvas" event from the server and clear the drawing.
    socket.on('clearCanvas', () => {
      paths = [];
      currentPath = [];
      redraw();
    });
  </script>
</body>
</html>
