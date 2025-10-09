 color Black = 000000;
 float diametroMaior = 50;
 float diametroMenor = 15;
 PImage bg, pin;
 
 void setup (){
   size (360, 337);
   pin = loadImage("Linux.png");
   bg = loadImage("b.png");
   background(bg);
 }
 void draw (){
 circle(200, 25, diametroMaior);
 circle(210, 24, diametroMenor);
 circle(190, 24, diametroMenor);
 line(200, 48, 200, 220);
 line(200, 68, 300, 100);
 line(200, 68, 100, 100);
 line(200, 220, 270, 280);
 line(200, 220, 150, 280);
 arc(200, 22, 40, 40, 1.2, 2);
 image(pin, 10, 10, 10, 10);
 
 }
