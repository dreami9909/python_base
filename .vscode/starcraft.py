from random import*

def game_Start() :
    input("종족을 선택하세요 T/F/Z ")
    print("게임을 시작합니다.")

def game_over() :
    print("Player : gg")
    print("[Player가 게임을 나갔습니다]")

class Unit :

    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}이/가 생성되었습니다.".format(self.name))

    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0}이 {1}방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

    def damaged(self, damage) :
        self.hp -= damage
        print("{0}이/가 {1}의 damage를 받았습니다. [체력 : {2}]".format(self.name,damage,self.hp))
        if self.hp <= 0 :
            print("{0}이/가 소멸되었습니다.".format(self.name))

class AttackUnit(Unit) :

    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location) :
        print("{0}이/가 {1}시 방향으로 공격합니다. [공격력 : {2}]".format(self.name,location,self.damage))

class Flyable :

    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self,name,location) :
        print("{0}이 {1}시 방향으로 비행합니다. [속도 : {2}]".format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable) :

    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location) :
        print("[공중 유닛 이동]") 
        self.fly(self.name, location)

# 테란의 지상 유닛
class Marine(AttackUnit) :

    def __init__ (self) :
        AttackUnit.__init__(self, "마린", 40, 15, 5)

    def stimpack(self) :

        if self.hp > 10 :
          print("{0}이/가 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        
        elif self.hp < 10 :
          print("{0}이/가 체력이 낮아 스팀팩을 사용할 수 없습니다.".format(self.name))

class Tank(AttackUnit) :
    
    seize_developed = False

    def __init__(self) :
        AttackUnit.__init__(self, "시즈탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self) :
        if Tank.seize_developed == False : 
           return 0  

        # seize_developed = True  
        if self.seize_mode == False :
            print("{0}이/가 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        elif self.seize_mode == True :
            print("{0}이/가 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
    

# 테란의 공중 유닛
class Dropship(Unit) :
    
    def __init__(self) :
        Unit.__init__(self,"드랍쉽",200,30)

    def drop(self, number) :
        number = input("드랍쉽에 태울 인원 : ")
        print("{0}이/가 {1}명을 태웠습니다.".format(self.name,number))


class Wraith(FlyableAttackUnit) :
    
    clocking_developed = False

    def __init__(self) :
        FlyableAttackUnit.__init__(self, "레이스", 150, 15, 40)
        self.clocking_mode = False

    def set_clocking_mode(self) :
        if Wraith.clocking_developed == False :
            return 0

        # clocking_developed = True
        if self.clocking_mode == False :
            print("{0}이/가 클로킹모드를 실행했습니다.".format(self.name))
            self.clocking_mode = True

        elif self.clocking_mode == True :
            print("{0}이/가 클로킹모드를 해제하였습니다.".format(self.name))
            self.clocking_mode = False


game_Start()

attack_units = []
m1 = Marine()
m2 = Marine()
m3 = Marine()
m4 = Marine()
m5 = Marine()
m6 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()
w2 = Wraith()

attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(m4)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

normal_units = []
d1 = Dropship()
d1.drop(2)

normal_units.append(d1)

for unit in attack_units :
    unit.move("1시")


Tank.seize_developed = True
Wraith.clocking_developed = True
print("[커멘드] 탱크 시즈 모드 개발이 완료되었습니다.")
print("[커멘드] 레이스 클로킹 모드 개발이 완료되었습니다.")

for unit in attack_units :
    if isinstance(unit,Marine) :
        unit.stimpack()
    elif isinstance(unit,Tank) :
        unit.set_seize_mode()
    elif isinstance(unit,Wraith) :
        unit.set_clocking_mode() 

for unit in attack_units :
    unit.attack("1시")

for unit in attack_units :
    unit.damaged(randint(1,25))

game_over()
