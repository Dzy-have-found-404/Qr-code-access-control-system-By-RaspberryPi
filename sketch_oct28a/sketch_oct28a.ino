int ledPin=10;//定义数字10接口
void setup()
{
pinMode(ledPin,OUTPUT);//定义小灯接口为输出接口
}
void loop()
{
digitalWrite(ledPin,HIGH);//点亮小灯
delay(1000);//延时1秒
digitalWrite(ledPin,LOW);//熄灭小灯
delay(1000);//延时1秒
}
