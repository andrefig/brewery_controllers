

//Geral -----------------------------------------------------

int i=0;
int AA [10];
int BB=0;
int CC=0;
int SA [10];

unsigned long tempo_serial=0;
unsigned long tempo_cooktop=0;
unsigned long tempo_sensor=0;
unsigned long tempo_sens_ligado=0;

#define periodo_serial 1000
#define periodo_cooktop 600 //assincrono 400
#define periodo_sensor 50
#define periodo_sens_ligado 5

//Cooktop -----------------------------------------------------

#define BTN_liga 5
#define BTN_modo 3
#define BTN_menos 4
#define BTN_mais 2//NA

#define SNS_ligado 10

int cooktop_estado=8;
int cooktop_ligado=0; //0 = desligado 1 = ligado 2 = ligando 3 = desligando 4 =atuando 5 = LIGANDO PT2
int sensor_ligado=0;

int cont_estado_erro=0;

//OneWire ------------------------------------------------------
#define ONE_WIRE_BUS A2   // Sensores de Temperatura

//#include <Thermistor.h>
#include <OneWire.h>

OneWire ds(ONE_WIRE_BUS);


float tempC1;
float tempC2;
float tempC3;
float tempC4;
float tempC5;
float tempC6;

#define add_temp_1 0x03D6
#define add_temp_2 0x0053
#define add_temp_3 0x03BC
#define add_temp_4 0x0389
#define add_temp_5 0x0489

//28FF6B5993160489

//28D6B3CD04000053
//28FFE550621603D6

//28FF03038B160389
//28FF66D6431603BC

//Termistor --------------------------------------------------------
//
//#define pinTemp1 A0
//#define pinTemp2 A1

//Thermistor temp1(pinTemp1);
//Thermistor temp2(pinTemp2);
//
//int t1;
//int t2;

 int16_t volume;
//Sonar --------------------------------------------------------------

#include <Ultrasonic.h>

//#define Tr1 7
#define Tr1 7
#define Ech1 7

#define Tr2 13//7
#define Ech2 13

//pino 7 - terminal aparafusável
//pino 8 - conector pequeno, fio vermelho
//pino 9 - conector pequeno, fio preto(VRF)

//Testar com TR2=7 (mesmo q tr1) e ECh2=6 (mesmo que o servo)



 //1 cm = 28 ms

// (30cm) = 0L (840ms)
//1,045 l/cm <=considerado
//
//28,5 ms/cm - veloc som
//
//27,25 ms / L



 #define vol_1_offset 890
 #define vol_1_mult 10
 #define vol_1_div 31
 #define vol_1_filt 9 //0 a 10
 #define vol_1_filt_ 1 //



 //1 cm = 28 ms

// 47cm (50cm) =  2,5L
//na regua
//9,5CM = 8L   ----1,188
//24L = 28,75  ----1,198 cm/l <=considerado
//??
//28,5 ms/cm - veloc som
//
//23,789 ms / L
// ???


 
 #define vol_2_offset 770//770
 #define vol_2_mult 8
 #define vol_2_div 35
 #define vol_2_filt 2 //0 a 10
 #define vol_2_filt_ 8 //




 
Ultrasonic ultrasonic1(Tr1, Ech1,3000);
Ultrasonic ultrasonic2(Tr2, Ech2,3000);

int32_t vol_ant1;
int32_t vol_ant2;


//Lupulo --------------------------------------------------------------
#include <Servo.h>
Servo Servo_1;  // create servo object to control a servo
#define Srv1 6
#define ts1 4
#define ts2 3
int cont_servo=ts1;


void setup() 
{
  // initialize serial:
  Servo_1.attach(Srv1);
  atua_servo();
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
//     for (int i=0; i <= 7; i++){
//      pinMode(rele[i], OUTPUT); 
//   } 
   pinMode(BTN_liga,OUTPUT);
   pinMode(BTN_modo,OUTPUT);
   pinMode(BTN_menos,OUTPUT);
   pinMode(BTN_mais,OUTPUT);

   
   pinMode(22,INPUT);
   pinMode(23,INPUT); 

   pinMode(SNS_ligado,INPUT_PULLUP);
   digitalWrite(ONE_WIRE_BUS,HIGH);
}

void loop() 
{
   if(millis()>tempo_sensor)
   {
      //sensor_ligado = min((sensor_ligado*70)/100,150) + 300*(!digitalRead(SNS_ligado));
      le_volume();
      //le_temperatura();
      le_onewire();
      le_onewire();
      le_onewire();
      tempo_sensor+=periodo_sensor;
   }
   if(millis()>tempo_sens_ligado)
   {
      //Serial.println("!");
      sensor_ligado = min((sensor_ligado*50)/100,150) + 300*(!digitalRead(SNS_ligado));
      tempo_sens_ligado+=periodo_sens_ligado;
   }
   if(millis()>tempo_serial)
   {
      le_serial();
      envia_serial();    
      tempo_serial+=periodo_serial;
      if (cont_servo==1)
      {
         Servo_1.detach();
         
      }
      else if (cont_servo==ts2)
      {
        atua_servo();
      }
      cont_servo-=1;
   } 
   if(millis()>tempo_cooktop)
   {
      if (cooktop_ligado>1)//estados transitórios
      {
        atualiza_botoes();
        //Serial.write("#"); //atuação pendente - concluir (botoes em HIGH)
      } 
      else //estados permanentes
      {
        atua_cooktop();
        //Serial.println("!!");
      }  
   }
   
}

void envia_serial()
{
    SA[0]=vol_ant1;
    SA[1]=vol_ant2;
    SA[2]=floor(tempC1*10);
    SA[3]=floor(tempC2*10);
    SA[4]=floor(tempC3*10);
    SA[5]=floor(tempC4*10);
    SA[6]=floor(tempC5*10);
    SA[7]=floor(tempC6*10);
    //SA[8]=floor(tempC5*10);
    //SA[9]=floor(tempC5*10);       
    Serial.print("DAT ");
    for (i=0; i <= 9; i++){
      if (i==0)
        {Serial.print(float(SA[i])/(10*vol_1_div));}
      else if (i==1)
        {Serial.print(float(SA[i])/(10*vol_2_div));}
      else
        {Serial.print(float(SA[i])/10);}
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
                //y++;
              }
              x++;
              delay(1);      //Delay para o Arduino não perder o dado da Serial
      }while((c!='\n')&&(x<9));
    str_entrada[0]=' ';
    //sscanf(str_entrada, "%d", &valor_entrada); //converte char array para inteiro
    valor_entrada=atoi(str_entrada);
    if (nome_entrada.substring(0,3)=="BB0")//Cooktop - 1 a 8 de potência
    {
       //LSerial.println(valor_entrada/14);
       BB=valor_entrada/14;// 7 POSIÇÕES - PARA 8, ALTERAR DIVISOR PARA 12
    }
    //Serial.println(nome_entrada.substring(0,3));
    //Serial.println(valor_entrada);
    if (nome_entrada.substring(0,3)=="CC0")//Cooktop - 1 a 8 de potência
    {
       CC=valor_entrada/10;// 6 POSIÇÕES - PARA 8, ALTERAR DIVISOR PARA 12
       Servo_1.attach(Srv1);
       cont_servo=ts1;
    }
  }
}  

void le_onewire() {
  byte i;
  byte data[12];
  byte addr[8];
  if ( !ds.search(addr)) {
    ds.reset_search();
    return;
  }
  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);        // start conversion, use ds.write(0x44,1) with parasite power on at the end
  delay(100);     // maybe 750ms is enough, maybe not TESTE!!!
  // we might do a ds.depower() here, but the reset will take care of it.
  ds.reset();
  ds.select(addr);
  ds.write(0xBE); 
  
  for ( i = 0; i < 9; i++) {
    data[i] = ds.read();
  }
  int16_t raw = (data[1] << 8) | data[0];
  int address_2 = (addr [6] << 8) | addr [7];
  //Serial.println(address_2,HEX);
  if (address_2==add_temp_1)// endereço do sensor (TESTADO COM PROGRAMA DE EXEMPLO DA LIB!)
  {
    tempC1 = (float)raw / 16.0;
  }
  else if (address_2==add_temp_2)
  {
    tempC2 = (float)raw / 16.0;
  }
  else if (address_2==add_temp_3)
  {
    tempC3 = (float)raw / 16.0;
  }
  else if (address_2==add_temp_4)
  {
    tempC4 = (float)raw / 16.0;
  }
  else if (address_2==add_temp_5)
  {
    tempC5 = (float)raw / 16.0;
  }else
  {
    tempC6 = (float)raw / 16.0;
  }
}

//void le_temperatura()
//{
//  int temp;
//  temp = 100*(temp1.getTemp());
//  temp = t1*7 + temp*3;
//  t1 = temp/10;
//  //t1=t1+1;
//  
//  temp = 100*(temp2.getTemp());
//  temp = t1*7 + temp*3;
//  t2 = temp/10; 
//  //t2=t2+1;
//}

void le_volume()
{
 
  int32_t volume;

  volume = ultrasonic1.distanceRead(1);
  volume =vol_1_offset-volume;
  volume= volume*vol_1_mult;
  volume= volume*vol_1_filt_;
  //volume/=vol_1_div;
  volume += vol_1_filt*vol_ant1;
  volume/=10;
  vol_ant1=max(volume,1);; 

  volume = ultrasonic2.distanceRead(1);
  volume =vol_2_offset-volume;
  volume= volume*vol_2_mult;
  volume= volume*vol_2_filt_;
  //volume/=vol_2_div;
  volume += vol_2_filt*vol_ant2;
  volume/=10;
  vol_ant2=max(volume,1);; 
 
}

void atua_servo() 
{
          Servo_1.write(35*CC); 

}
void atua_cooktop() 
{
  //Serial.println(cont_estado_erro);
  //Serial.println(sensor_ligado);

  //------------VRF INCONSISTÊNCIA---------------------------
    if ((cooktop_ligado & B00000001)^(sensor_ligado>0))
    {// 1, 3 ou 5
      cont_estado_erro+=2;
      tempo_cooktop=millis()+periodo_cooktop;
    }
    else if(cont_estado_erro>0)
    {
      cont_estado_erro-=1;
      tempo_cooktop=millis()+periodo_cooktop;
    }
    
    if (cont_estado_erro>5) //Inconsistência de estado se repete
    {
      if (cooktop_ligado) //Acusa ligado, mas há inconsistência
      {
        cooktop_liga();
        //Serial.println("liga!");
        cont_estado_erro=0;
      }
      else
      {
        cooktop_desliga();
        //Serial.println("desliga!");
        cont_estado_erro=0;
      }
      
      }
    //--------------------------------
  
  if (BB>7)
  {
    BB=7;//limita estados de potência
  }
  if (BB>0)//Potencia >0
  {
    if (cooktop_ligado==0)
      {
        cooktop_liga();
      }
    //if (sensor_ligado==0)
    //{
    //  cooktop_liga();
    //}
    //else
    //{//Serial.println("!");
    // if (cooktop_ligado==0) 
    // {
    //  cont_estado_erro+=1;
    //  cooktop_ligado=1;
    //}
    //}
    if (cooktop_ligado==1)//<=1
     {
          if (BB<cooktop_estado)
          {
              //delay(500);
              cooktop_diminui();
              //Serial.println("DIMINUI!");
              //Serial.println(BB);
          }
          if (BB>cooktop_estado)
          {
              //delay(500);
              //cooktop_desliga();
              cooktop_aumenta();
              //Serial.println("AUMENTA!");
          }
     }
    
  }
  else
  {
    if (cooktop_ligado==1)
    {
        cooktop_desliga();
    }
    //if (sensor_ligado>0)
    //{     cooktop_desliga();}
    //else
    //{ //Serial.println(sensor_ligado);
    //  if (cooktop_ligado==1) {cooktop_ligado=0;}}
  }

}

void cooktop_liga()
{
  //if (cooktop_ligado==0)
  //{//0 = desligado 1 = ligado 2 = ligando 3 = desligando 4 =atuando
    //SEQUENCIA_LIGAR:  0>2>5>4>1  

  //  {
      digitalWrite(BTN_liga,HIGH);
      tempo_cooktop=millis()+periodo_cooktop;
      //Serial.println("liga");
      //delay(200);
      //digitalWrite(BTN_liga,LOW);
      //delay(200);
      //digitalWrite(BTN_modo,HIGH);
      //delay(200);
      //digitalWrite(BTN_modo,LOW);
      //delay(200);
      cooktop_ligado=2;
      cooktop_estado=5;//8
    //}
  //}


}

void cooktop_desliga()
{
 // if (cooktop_ligado==1)
  //{
  //if (sensor_ligado>0)
  //{
    digitalWrite(BTN_liga,HIGH);
    tempo_cooktop=millis()+periodo_cooktop;
    cooktop_ligado = 3;
    //delay(200);
    //digitalWrite(BTN_liga,LOW);
    //delay(1000);
  //}
  //}
  //cooktop_ligado=false;

}

void cooktop_aumenta()
{
    digitalWrite(BTN_mais,HIGH);
    tempo_cooktop=millis()+periodo_cooktop;
    cooktop_estado+=1;
    cooktop_ligado = 4;
    //0 = desligado 1 = ligado 2 = ligando 3 = desligando 4 =atuando
}

void cooktop_diminui()
{
    digitalWrite(BTN_menos,HIGH);
    tempo_cooktop=millis()+periodo_cooktop;
    cooktop_estado-=1;
    cooktop_ligado = 4;
}

void atualiza_botoes()
{
      //0 = desligado 1 = ligado 2 = ligando 3 = desligando 4 =atuando 5 = alterando modo (interlockligar)
  if (cooktop_ligado==3)
  {
      digitalWrite(BTN_liga,LOW);
      cooktop_ligado=0;
  }
  else if (cooktop_ligado==2)
  {
      cooktop_ligado=1;//5
      digitalWrite(BTN_liga,LOW);
      //cooktop_ligado=5;
  }
  else if (cooktop_ligado==4)
  {
    //digitalWrite(BTN_modo,LOW);
    digitalWrite(BTN_mais,LOW);
    digitalWrite(BTN_menos,LOW);
    cooktop_ligado=1;
  }
 // else if (cooktop_ligado==5)
 // {
 //   digitalWrite(BTN_modo,HIGH);
 //   cooktop_ligado=4;
 // }
 // tempo_cooktop=millis()+periodo_cooktop;
}
