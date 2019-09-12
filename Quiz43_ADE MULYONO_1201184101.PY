ListGPA = [2.1,2.5,4,3]

def Reward (GPA):
    bonus = 500000
    Reward = GPA*bonus
    return Reward

for GPA in ListGPA:
    if GPA > 2.5:
        print("Selamat atas kerja keras anda! anda mendapatkan : Rp", Reward(GPA))
    else :
            print("Maaf anda kurang beruntung! tingkatkan lagi keja keras anda,")
