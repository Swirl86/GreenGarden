/* Draw humidity indicator 
TODO: convert fetch data to % for real time update */

function drawGuage() {
  ctx.clearRect(0, 0, cw, ch);
  // draw full guage outline
  ctx.beginPath();
  ctx.arc(cx, cy, r, min, max);
  ctx.strokeStyle = "lightgray";
  ctx.lineWidth = 20;
  ctx.stroke();
  // draw percent indicator
  ctx.beginPath();
  ctx.arc(cx, cy, r, min, min + ((max - min) * percent) / 100);
  ctx.strokeStyle = "#642EFE";
  ctx.lineWidth = 10;
  ctx.stroke();
  ctx.fillText(percent + "%", cx, cy);
}
