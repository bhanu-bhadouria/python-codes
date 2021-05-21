class User:
    allowed=["aditi","bhanu","sadhana","uday"]
    active_user_count=0
    def __repr__(self):
        return f"there are {User.active_user_count} active users"
    def __init__(self,fname,lname,age):
        if fname not in User.allowed:
            raise ValueError(f"{fname} not a valid username")
        self.fname=fname
        self.lname=lname
        self.age=age
        User.active_user_count+=1
    def hb(self):
        self.age+=1
        return f"Happy {self.age}'th, {self.fname}"
    @property
    def full_name(self):
        return f"Hello {self.fname} {self.lname}"
    def initials(self):
        print(f"Mr/Mrs./Miss {self.fname[0]}.{self.lname[0]}.")
    def display_users(self):
        print(f"the number of active members are: {User.active_user_count}")
    def likes(self,thing):
        return f"{self.fname} likes {thing}"
    def logout(self):
        User.active_user_count-=1
        print(f"{self.fname} has logged out")
class moderator(User):
    active_moderator_count=0
    def __init__(self, fname, lname, age,community):
        super().__init__(fname, lname, age)
        self.community=community
        moderator.active_moderator_count+=1
    def __repr__(self):
        return f"there are currently {moderator.active_moderator_count} active moderators"
    def deleted(self):
        return f"{self.full_name} deleted the post from the {self.community} community"
    def logout(self):
        moderator.active_moderator_count-=1
        User.active_user_count-=1
        return f"{self.full_name} has logged out from the moderator side"


u1=User("bhanu","bhadouria",20)
u2=User("aditi","bhadouria",18)
m1=moderator("sadhana","bhadouria",47,"soccer")
m2=moderator("uday","bhadouria",47,"IT-sector")
print(u2)
print(m2)
u1.logout()
print(u2)
print(m1.logout())
print(u2)
print(m2)
m2.logout()