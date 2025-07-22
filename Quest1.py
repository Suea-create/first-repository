import random

class Account:
    bank_name = "SCbank"
    account_count = 0
    
    def __init__(self, owner, balance):
        self.owner= owner
        self.balance= balance
        self.account_number= self.generate_account_numbers()
        self.deposit_count= 0
        self.deposit_log=[]
        self.withdraw_log=[]
        Account.account_count +=1

    def generate_account_numbers(self):
        return f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(100000,999999)}"
        
    @classmethod
    def get_account_num(cls):
        return cls.account_count
        
    def deposit(self, amount):
        if amount >=1 :
            self.balance +=amount
            self.deposit_count +=1
            self.deposit_log.append(amount)
            if self.deposit_count %5 ==0:
                self.balance +=int(self.balance *0.01)
        else:
            print("입금은 1원 이상부터 가능합니다.")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            self.withdraw_log.append(amount)
        else:
            print("잔액 부족")
            
    def display_info(self):
        print(f"은행이름: {Account.bank_name}")
        print(f"예금주: {self.owner}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {format(self.balance,',')}원")

    acc1= Account("Alice", 100000)
    acc2= Account("Smile", 200000)
    acc3= Account("Peter", 300000)
    
    account_list=[acc1, acc2, acc3]

    for acc in account_list:
        if acc.balance >= 1000000:
            acc.display_info()
    def deposit_history(self):
        print(f"{self.owner}의 입금 내역: {self.deposit_log}")
    def withdraw_history(self):
        print(f"{self.owner}의 출금 내역: {self.withdraw_log}")


import random
class Character:
    def __init__(self, name, level, hp, attack, defense):
        self.name=name
        self.level=level
        self.hp=hp
        self.attack=attack
        self.defense=defense

    def is_alive(self):
        return self.hp > 0
        
    def take_damage(Self.damage):
        final_damage = damage - self.defense
        if final_damage >0 :
            self.hp -=final_damage
            print(f"{self.name} 이(가) {final_damage} 데미지를 입었습니다. (남은 HP:{self.hp})")
        else:
            print(f"{self.name}이(가) 공격을 막아냈습니다. (방어력{self.defense} > 데미지{damage})")

    def attack_target(self.target):
        damage= random.randint(1,self.attack)
        print(f"{self.name}이(가) {target.name}에게 {damage} 데미지를 입히려 합니다.")
        target.take_damage(damage)
       
player= Chracter("용사", level=1, hp=180, attack=20, defense=5)
monster= Character("슬라임", level=1, hp=30, attack=10, defense=2)

class Character:
    def __init__(self, name, level=1, hp=100, attack=10, defense=5):
        self.name=name
        self.level=level
        self.hp=hp
        self.attack=attack
        self.defense=defense

class Player(character):
    def __init__(self,name):
        super().__init__(name, level=1, hp=100, attack=25, defense=5)
        self.exp=0

    def gain_experience(self, amount):
        self.exp +=amount
        print(f"{self.name} 경험치 + {amount} (현재 EXP: {self.exp})")

    def level_up(self):
        while self.exp >=50 :
            self.level +=1
            self.attack +=10
            self.defense +=5
            self.exp -=50
            print(f"레벨 업! {self.name}는 이제 레벨 {self.level}입니다. ")
            print(f"공격력: {self.attack}, 방어력: {self.defense}")
import random
class Monster(character):
    def __init__(self, name, level):
        hp= random.randint(10,30) *level
        attack= random.randint(5,20) *level
        defense= random.randint(1,5) *level
        super().__init__(name, level, hp, attack, defense)

    def battle(player, monster):
        print(f"\n {player.name} vs {monster.name} (LV.{monster.level}) 전투시작!"
        while player.hp > 0 and monster.hp > 0:
            damage_to_monster = max(player.attack - monster.defense, 0)
            monster.hp -=damage_to_monster
            print(f"{player.name} {monster.name}에게 {damage_to_monster} 데미지! (플레이어 HP:{player.hp})")
            if monster.hp <= 0:
                damage_to_player = max(monster.attack -player.defense,0)
                player.hp -= damage_to_player
                print(f"{monster.name} {player.name}에게 {damage_to_player} 데미지! (플레이어 HP:{player.hp})")
        if player.hp >0 :
            print("전투 승리")
            exp = monster.level *20
            player.gain_experience(exp)
            player.level_up()

        else:
            print("전투 패배")
            
    def main():
        monster_dict ={'슬라임':1, '고블린':2, '오크':3}
        name= input("플레이어 이름을 입력하세요:")
        player=player(name)

        for monster_name, level in monster_dict.items():
            monster= Monster(monster_name,level)
            battle(player,monster)

            if player.hp <= 0:
                print("게임 오버)"
                return
                
        print ("승리")
            
                

    
                
        
    
        
    
    

        
    
        
                
        



        
        