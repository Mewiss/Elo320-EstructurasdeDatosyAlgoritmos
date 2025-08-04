
var aperturaBlock = document.getElementById("apertura-1-0");
var aperturaObject = document.getElementById("apertura-1-0");
var flanco = document.getElementById("flanco1");
var flanco2 = document.getElementById("flanco2");
var flanco3 = document.getElementById("flanco3");
var clock = document.getElementById("clkBlock");
const svg = document.getElementById('mysvg');

var delta = 0;


// translate page to SVG coordinate
function svgPoint(svgElement, x, y) {
  var pt = svgElement.createSVGPoint();
  pt.x = x;
  pt.y = y;
  var svgPoint = pt.matrixTransform(svgElement.getScreenCTM().inverse());
  return svgPoint;
}

function movePolygonX(polygonId, start, end) {
  var polygon = document.getElementById(polygonId);
  var points = polygon.getAttribute("points").split(" ");
  
  // Modificar las posiciones X de los puntos
  points[0] = (start + 10) + "," + points[0].split(",")[1];
  points[1] = (start) + "," + points[1].split(",")[1];
  points[2] = (start + 10) + "," + points[2].split(",")[1];
  points[3] = (end- 10) + "," + points[3].split(",")[1];
  points[4] = (end) + "," + points[4].split(",")[1];
  points[5] = (end - 10) + "," + points[5].split(",")[1];

  polygon.setAttribute("points", points.join(" "));
}

function animate() {
  pt = flanco.getPointAtLength(0);
  var posx = Math.round(pt.x);
  //print(posx)

  var posFlanco = posx;//parseInt(document.getElementById("flanco1").getAttribute('d').split(' ')[1],10);
  var posd = posFlanco + delta;
  //console.log(posFlanco);
  //console.log(delta);

  //aperturaBlock.setAttribute("transform", `translate(${posd})`);
  aperturaObject.setAttribute("x", posd);

  requestAnimationFrame(animate);
}

// Move obj element along path based on percentage of total length
function moveObj(prcnt) {
  console.log(prcnt);
  var newClock = 1.0 - 0.23 * prcnt / 100;
  console.log(newClock);


  clock.setAttribute("transform", `scale(${newClock}, 1.0)`);



  var bboxFlanco = flanco.getBoundingClientRect();
  var flancoX = svgPoint(flanco.ownerSVGElement, bboxFlanco.x, bboxFlanco.y).x;
  console.log(flancoX);
  console.log(delta);
  document.getElementById("apertura-1-0").setAttribute('x', flancoX + delta);
  document.getElementById("apertura-1-1").setAttribute('x', flancoX + delta);

  

  document.getElementById("g2249").setAttribute("transform", `translate(${flancoX - 224},0)`);



  
  var t2 = flanco2.getBoundingClientRect();
  console.log(t2.x);

  var bboxFlanco2 = flanco2.getBoundingClientRect();
  var flanco2X = svgPoint(flanco2.ownerSVGElement, bboxFlanco2.x, bboxFlanco2.y).x;
  console.log(flanco2X);
  console.log(delta);
  document.getElementById("apertura-2-0").setAttribute('x', flanco2X + delta);
  document.getElementById("apertura-2-1").setAttribute('x', flanco2X + delta);
  
  var widthSlack=Math.max((flanco2X-30)-(flancoX + 340),0);
  document.getElementById("tslack").setAttribute('x', flancoX + 320);
  document.getElementById("tslack").setAttribute('width', widthSlack);
  

  
  var bboxFlanco3 = flanco3.getBoundingClientRect();
  var flanco3X = svgPoint(flanco3.ownerSVGElement, bboxFlanco3.x, bboxFlanco3.y).x;
  
  document.getElementById("g2249_2").setAttribute("transform", `translate(${flanco2X -680},0)`);
  document.getElementById("g2317_3").setAttribute("transform", `translate(${flanco3X -1125},0)`);
  
  
  //var polygon =document.getElementById("startChange1");
  movePolygonX("startChange1", flancoX + 175, flanco2X + 35 );
  movePolygonX("startChange2", flancoX + 175, flanco2X + 35 );
  movePolygonX("startChange3", flancoX + 300, flanco2X + 240 );
  movePolygonX("startChange4", flanco2X + 175, flanco3X + 35 );
  movePolygonX("startChange5", flanco2X + 175, flanco3X + 35 );
  movePolygonX("startChange6", flanco2X + 300, flanco3X + 240 );
  
  movePolygonX("startChange7", flanco3X + 175, flanco3X + 500 );
  movePolygonX("startChange8", flanco3X + 175, flanco3X + 500 );

}


var bboxFlanco = flanco.getBBox();
var bboxApertura = aperturaBlock.getBBox();//document.getElementById("apertura-1").getBBox();

var flancoXOrigin = bboxFlanco.x;
var aperturaX = bboxApertura.x;

var delta = 170 - 220;//aperturaX - flancoXOrigin;
console.log(aperturaX)
console.log(flancoXOrigin)
console.log(delta);

// Initialize
moveObj(0);


// Slider functionality
var sliderEl = document.getElementById('slider');
sliderEl.addEventListener('mousemove', function () {


  moveObj(this.value);
});

