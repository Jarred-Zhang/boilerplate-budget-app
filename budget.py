
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger=[]

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self, amount, description=""):
        if sum([ i["amount"] for i in self.ledger]) >= amount:
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else: return False

    def get_balance(self):
        return sum([ i["amount"] for i in self.ledger])

    def transfer(self, amount, c):
        if sum([ i["amount"] for i in self.ledger]) >= amount:
            self.ledger.append({"amount":-amount,"description":"Transfer to "+c.category})
            c.ledger.append({"amount":amount,"description":"Transfer from "+self.category})
            return True
        else: return False

    def check_funds(self, amount):
        return sum([ i["amount"] for i in self.ledger]) >= amount

    def __str__(self):
        #title
        size1 = (30-len(self.category))//2
        size2 = size1 if (30-len(self.category))%2 == 0 else size1+1
        title = size1*"*"+str(self.category)+size2*"*"+"\n"
        #content
        l = [ (i["description"]+23*" ")[:23] + (7*" "+str("%.2f" % i["amount"]))[-7:] +"\n" for i in self.ledger]
        #total
        total="Total: "+ str(round(sum([ i["amount"] for i in self.ledger]),2))
        return title + "".join(l) + total

def create_spend_chart(categories):
    withdrawals =[sum(j["amount"] for j in i.ledger if j["amount"] < 0) for i in categories]
    s=sum(withdrawals)
    percentages = [i/s*100 for i in withdrawals]
    a=[]
    for i in range(100,-1,-10):
        a.append((2*" "+str(i))[-3:]+"|"+"".join([" o " if j>=i else "   "for j in percentages]))
    a.append("    "+len(categories)*"---")
    for j in range(max(len(i.category) for i in categories)):
        a.append("     "+"  ".join(k.category[j] if len(k.category) > j else " " for k in categories)+"  ")

    return "\n".join(a)
