
int i=0;
int AA [8];
int BB [8];
int CC [2];
int ZZ;
int SA [10];

//Geral --------------------------------------------------------------------------------

unsigned long tempo_serial=0;
unsigned long tempo_cooktop=0;
unsigned long tempo_sensor=0;

const int rele[8]= {2, 3, 4,5,6,7,8,12};
const int rele2[8]= {13, 15, 16,17,18,19,11,10};
const int ssr[2]={14,14};
const int falante=9;

#include <avr/wdt.h>


#define periodo_serial 1000

//OneWire ------------------------------------------------------------------------------

#include <OneWire.h>

#define ONE_WIRE_BUS A0   // Sensores de Temperatura
OneWire ds(ONE_WIRE_BUS);

float tempC1;
float tempC2;
float tempC3;

boolean tom_ativo;

#define add_temp_1 0xBC
#define add_temp_2 0xD6

//#define pino_rst A7


void setup() 
{
  // initialize serial:
  //digitalWrite(pino_rst, HIGH);
  //pinMode(pino_rst, INPUT);
  //digitalWrite(pino_rst, LOW);
  wdt_disable();
  ////delay(1000);
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
   for (int i=0; i <= 7; i++){
      pinMode(rele[i], OUTPUT); 
      pinMode(rele2[i], OUTPUT); 
   }
   for (int i=0; i <= 1; i++){
      pinMode(ssr[i], OUTPUT); 
   }
   pinMode(falante, OUTPUT);


   for (int i=0; i <= 7; i++)
          {
              digitalWrite(rele[i],!AA[i]); 
              digitalWrite(rele2[i],!BB[i]); 
              
              //Serial.println(AA[i]);
              //Serial.println(i);
          }
          
    for (int i=0; i <= 1; i++)
          {
              analogWrite(ssr[i],CC[i]); 
          } 
       // sets the digital pin as output
    //delay(5000);
    //pinMode(pino_rst, OUTPUT);
    //digitalWrite(pino_rst, HIGH);
    //wdt_reset();
    //wdt_enable(WDTO_8S);
   tone(falante,1000);
   delay(1000);
   noTone(falante);      
}

void loop() 
{
  //wdt_reset();
  //digitalWrite(pino_rst, HIGH);
  while (Serial.available()) 
  {
          le_serial();
          delay(200);
  }
  for (int i=0; i <= 7; i++)
          {
              digitalWrite(rele[i],!AA[i]); 
              digitalWrite(rele2[i],!BB[i]); 
              //Serial.println(AA[i]);
              //Serial.println(i);
          }
          
  for (int i=0; i <= 1; i++)
          {
              analogWrite(ssr[i],CC[i]); 
          } 
//   if(millis()>tempo_sensor)
//   {
//      tempo_sensor+=periodo_sensor;
//   }
   if(millis()>tempo_serial)
   {
      le_onewire();
      le_onewire();
      le_onewire();
      if ((ZZ>0)&&(!tom_ativo))
      {
              tone(falante,10*ZZ);
              tom_ativo=true;
      }
      else
      {
         noTone(falante); 
         tom_ativo=false;
      }   
      envia_serial();    
      tempo_serial+=periodo_serial;
      //digitalWrite(pino_rst, LOW);
      

   }   
   
}

void envia_serial()
{
    SA[0]=floor(tempC1*10);
    SA[1]=floor(tempC2*10);
    SA[2]=floor(tempC3*10);
    Serial.print("DAT2 ");
    for (i=0; i <= 9; i++){
        Serial.print(float(SA[i])/10);
        Serial.print(" ");
   } 
   Serial.println("");
}



void le_serial()
{
  String nome_entrada;
  int nome_entrada_val;
  char c;
  char str_entrada[20];
  int x,y;
  int valor_entrada;

  nome_entrada_val=-1;
  if(Serial.available())
    {
    x=0;
    y=0;
    do
      {
              c=Serial.read();
              Serial.write(c);
              if ((c !=';')&&(y==0))
              {
                str_entrada[x]=c;
              }
              else
              {
                //Serial.println("@");
                if (y==0) //caiu aqui porque o char é ' '   
                  //str_entrada[x-1]='\0'; ??
                  {
                    str_entrada[x]='\0';
                    nome_entrada = str_entrada;
                    memset(str_entrada, 0, sizeof str_entrada); //zera char array
                    x=0;
                  }
                str_entrada[x]=c;
                y++;
              }
              //Serial.print(str_entrada[x],DEC);
              
              x++;
              delay(50);      //Delay para o Arduino não perder o dado da Serial
      }while((c!='\n')&&(Serial.available()>0)&&(x<10));

    
    //Serial.println("!@!");
    //Serial.println(nome_entrada.substring(0,2));
    //Serial.println(nome_entrada.substring(2));
    
    str_entrada[0]=' ';
    //sscanf(str_entrada, "%d", &valor_entrada); //converte char array para inteiro
    valor_entrada=atoi(str_entrada);
    if (nome_entrada.substring(0,2)=="AA")
    {
      x=(nome_entrada.substring(2).toInt());
      //Serial.println(x);
      if (x<8)
      {
        AA[x]=valor_entrada;
        //Serial.println("##");
        //Serial.println(valor_entrada);
      }
    }
    else if (nome_entrada.substring(0,2)=="BB")
    {
      x=(nome_entrada.substring(2).toInt());
      //Serial.println(x);
      if (x<8)
      {
        BB[x]=valor_entrada;
        //Serial.println("##");
        //Serial.println(valor_entrada);
      }
    }
    else if (nome_entrada.substring(0,2)=="CC")
    {
      x=(nome_entrada.substring(2).toInt());
      //Serial.println(x);
      if (x<2)
      {
        CC[x]=map(valor_entrada,0,100,0,255);
      }

    }
    else if (nome_entrada.substring(0,2)=="ZZ")
    
      {
         x=(nome_entrada.substring(2).toInt());
        x = 2 << x;  //2 4 8 16 32 64 128 256 512 1024
        if (valor_entrada)
        {
           ZZ = x;
        }
        else
        {
          ZZ=0;
        }
      }
    else
    {
           // serialFlush();
    }
  }
}  

void le_onewire() {
  byte i;
  byte data[12];
  byte addr[8];
  if ( !ds.search(addr)) {
    ds.reset_search();
    //Serial.print("!@!!");
    delay(250);
    return;
  }
  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);        // start conversion, use ds.write(0x44,1) with parasite power on at the end
  //delay(1000);     // maybe 750ms is enough, maybe not TESTE!!!
  // we might do a ds.depower() here, but the reset will take care of it.
  ds.reset();
  ds.select(addr);
  //Serial.println("!@!");
  //Serial.println(addr[7], HEX);
  ds.write(0xBE); 
  
  for ( i = 0; i < 9; i++) {
    data[i] = ds.read();
  }
  //Serial.print("!@");
  //Serial.println((int)data);
  int16_t raw = (data[1] << 8) | data[0];
  //Serial.println(raw);
 // Serial.println("!@!");
 // Serial.println(addr [7]);
 // Serial.println(add_temp_1);
 // Serial.println(add_temp_2);
  if (addr [7]==add_temp_1)// endereço do sensor (TESTADO COM PROGRAMA DE EXEMPLO DA LIB!)
  {
    tempC1 = (float)raw / 16.0;
  }
  else if (addr [7]==add_temp_2)//D6
  {
    tempC2 = (float)raw / 16.0;
//    int t = RTC.temperature();
//    tempC3 = t / 4.0;
  }else
  {
    tempC3 = (float)raw / 16.0;
   }
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}   
