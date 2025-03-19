<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Drawing App with Hidden Clear Menu</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  <style>
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      overflow: hidden !important;
      background: black !important;
    }
    /* Hide scrollbars in WebKit browsers */
    ::-webkit-scrollbar {
      display: none !important;
    }
    /* Canvas fills the viewport, intrinsic size 1920x1080, with background image and custom cursor */
    #canvas {
      display: block;
      width: 100vw;
      height: 100vh;
      background: url('BG_V6.png') no-repeat center center;
      background-size: cover;
      cursor: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PGNpcmNsZSBjeD0iOCIgY3k9IjgiIHI9IjgiIGZpbGw9InJlZCIvPjwvc3ZnPg==") 8 8, auto;
    }
    /* Hidden pull-in menu: initially off-screen to the left */
    #pullMenu {
      position: fixed;
      top: 0;
      left: -160px; /* Off-screen initially */
      width: 160px;
      height: 100vh;
      background: rgba(0, 0, 0, 0.7);
      color: white;
      padding: 20px;
      box-sizing: border-box;
      transition: left 0.3s ease;
      z-index: 1000;
    }
    #pullMenu button {
      font-size: 20px;
      padding: 10px 15px;
      margin-top: 20px;
      cursor: pointer;
    }
    /* A small handle along the left edge to reveal the menu */
    #menuHandle {
      position: fixed;
      top: 50%;
      left: 0;
      width: 20px;
      height: 60px;
      background: rgba(255, 255, 255, 0.3);
      cursor: pointer;
      z-index: 1001;
      transform: translateY(-50%);
    }
  </style>
</head>
<body>
  <canvas id="canvas" width="1920" height="1080"></canvas>
  
  <!-- Hidden pull-in menu -->
  <div id="pullMenu">
    <h3 style="margin:0 0 10px 0;">Menu</h3>
    <button id="clearBtn">Clear Drawing</button>
    <button id="hideMenuBtn">Hide Menu</button>
  </div>
  <!-- Handle to reveal the pull-in menu -->
  <div id="menuHandle"></div>
  
  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let drawing = false;
    let paths = [];
    let currentPath = [];
    
    // Convert event coordinates to canvas coordinates,
    // accounting for scaling between intrinsic (1920x1080) and displayed size.
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
      ctx.strokeStyle = '#FFEA00'; // Yellow drawing color
      
      paths.forEach(path => {
        ctx.beginPath();
        path.forEach((point, i) => {
          if(i === 0) {
            ctx.moveTo(point.x, point.y);
          } else {
            ctx.lineTo(point.x, point.y);
          }
        });
        ctx.stroke();
      });
      
      if(currentPath.length) {
        ctx.beginPath();
        currentPath.forEach((point, i) => {
          if(i === 0) {
            ctx.moveTo(point.x, point.y);
          } else {
            ctx.lineTo(point.x, point.y);
          }
        });
        ctx.stroke();
      }
    }
    
    // Pull-in menu functionality
    const pullMenu = document.getElementById('pullMenu');
    const menuHandle = document.getElementById('menuHandle');
    const clearBtn = document.getElementById('clearBtn');
    const hideMenuBtn = document.getElementById('hideMenuBtn');
    
    // Show the menu when the handle is clicked
    menuHandle.addEventListener('click', () => {
      pullMenu.style.left = '0';
    });
    
    // Hide the menu when the hide button is clicked
    hideMenuBtn.addEventListener('click', () => {
      pullMenu.style.left = '-160px';
    });
    
    // Clear the drawing when the clear button is pressed and then auto-hide the menu.
    clearBtn.addEventListener('click', () => {
      paths = [];
      currentPath = [];
      redraw();
      setTimeout(() => {
        pullMenu.style.left = '-160px';
      }, 500);
    });
  </script>
</body>
</html>
