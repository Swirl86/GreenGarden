int moistureIn_1 = 0;
int moistureIn_2 = 1;
int moistureIn_3 = 2;
int moistureIn_4 = 3;
int moistureIn_5 = 4;

const int powerOut_1 = 2;
const int powerOut_2 = 3;
const int powerOut_3 = 4;
const int powerOut_4 = 5;
const int powerOut_5 = 6;

void setup() {
  Serial.begin(9600);
  
  pinMode(powerOut_1,OUTPUT);
  pinMode(powerOut_2,OUTPUT);
  pinMode(powerOut_3,OUTPUT);
  pinMode(powerOut_4,OUTPUT);
  pinMode(powerOut_5,OUTPUT);
}

void loop() {

  int moisture = 0;
  
  digitalWrite(powerOut_1, HIGH);
  delay(5000);
  moisture += analogRead(moistureIn_1);
  int moist_1 = analogRead(moistureIn_1);
  //Serial.println("s1: " + String(moist_1));
  delay(3000);
  digitalWrite(powerOut_1, LOW);
  delay(5000);

  digitalWrite(powerOut_2, HIGH);
  delay(5000);
  moisture += analogRead(moistureIn_2);
  int moist_2 = analogRead(moistureIn_2);
  //Serial.println("s2: " + String(moist_2));
  delay(3000);
  digitalWrite(powerOut_2, LOW);
  delay(5000);

  
  digitalWrite(powerOut_3, HIGH);
  delay(5000);
  moisture += analogRead(moistureIn_3);
  int moist_3 = analogRead(moistureIn_3);
  //Serial.println("s3: " + String(moist_3));
  delay(3000);
  digitalWrite(powerOut_3, LOW);
  delay(5000);

  
  digitalWrite(powerOut_4, HIGH);
  delay(5000);
  moisture += analogRead(moistureIn_4);
  int moist_4 = analogRead(moistureIn_4);
  //Serial.println("s4: " + String(moist_4));
  delay(3000);
  digitalWrite(powerOut_4, LOW);
  delay(5000);

  
  digitalWrite(powerOut_5, HIGH);
  delay(5000);
  moisture += analogRead(moistureIn_5);
  int moist_5 = analogRead(moistureIn_5);
  //Serial.println("s5: " + String(moist_5));
  delay(3000);
  digitalWrite(powerOut_5, LOW);
  delay(5000);

  Serial.println((moisture/5));
  delay(5000);
}
