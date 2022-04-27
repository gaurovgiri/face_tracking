
#include <Servo.h>

Servo servo;

int inp[3];    // input from serial buffer
int init_byte; // first byte
int servo_id;  // which servo to run?
int pos;       // servo angle 0-180
int i;         // iterator
int ang = 90;  // variable to move to according angle

// Common servo setup
int min_pos = 600;  // min servo position
int max_pos = 2400; // max servo position

void setup()
{
  servo.attach(9, min_pos, max_pos); // attaching servo to digital pin no. 9
  Serial.begin(9600);                // serial connection in 9600 baud
}

void loop()
{
  if (Serial.available() > 2)  // checking for the input buffer that should contain more than 2 bytes
    init_byte = Serial.read(); // Read the first byte
  if (init_byte == 255)        // If it's really the startbyte (255) ...
  {
    for (i = 0; i < 2; i++) // ... then get the next two bytes
    {
      inp[i] = Serial.read();
    }
    servo_id = inp[0]; // which servo to run
    pos = inp[1];      // servo position
    if (pos == 255)    // checking extremes
    {
      servo_id = 255;
    }
    if (pos == 1)
    {
      ang = ang + 3;
      servo.write(t);
    }
    else if (pos == 2)
    {
      ang = ang - 3;
      servo.write(t);
    }
  }
}
}
