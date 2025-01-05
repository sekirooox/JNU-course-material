def Hanoi_Tower(height:int,fromPole,toPole,withPole):
    if height >=1:
        Hanoi_Tower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        Hanoi_Tower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print('moving bottom disk from',fp,"to",tp)
if __name__ == '__main__':
    Hanoi_Tower(8,1,3,2)

