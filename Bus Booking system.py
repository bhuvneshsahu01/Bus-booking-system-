#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BusBooking:
    booking_id=1
    W=['W'+str(i) for i in range(1,21)]
    A=['A'+str(i) for i in range(1,21)]
    wll=[]
    dict1={}
    dictwl={}
    
    def __init__(self):
        self.booking_id=BusBooking.booking_id
        self.dict1=BusBooking.dict1
        self.w=sorted(BusBooking.W)
        self.a=sorted(BusBooking.A)
       
        self.wll=BusBooking.wll
        self.menu()
        
    
    def menu(self):
        x=int(input('''What do you want to do ?
        1) Book a BusBooking seat 
        2) cancel the booking'''))
        if x==1:
            name=input('name')
            preference=input('preference')
            self.book(name,preference)
        else:
            id1=int(input('booking_id'))
            self.cancel(id1)
    
    
    def book(self,name,preference='no'):
        self.name=name
        self.preference=preference
        if self.preference in ['w','W','Window','window'] and len(self.w)>0:
            BusBooking.dict1[self.booking_id]=[self.name,self.w.pop(0)]
            
            BusBooking.booking_id+=1
        elif self.preference in ['a','A','aisle','Aisle'] and len(self.a)>0:
            BusBooking.dict1[self.booking_id]=[self.name,self.a.pop(0)]
            BusBooking.booking_id+=1
        else:
            if len(self.w)>0:
                BusBooking.dict1[self.booking_id]=[self.name,self.w.pop(0)] 
            
                BusBooking.booking_id+=1
            elif len(self.a)>0:
                BusBooking.dict1[self.booking_id]=[self.name,self.a.pop(0)] 
                BusBooking.booking_id+=1
            else :
                BusBooking.wll.append(self.booking_id)
                BusBooking.dictwl[self.booking_id]=[self.name]
                BusBooking.booking_id+=1
        #return (self.status(self.booking_id))
            
    def cancel(self,booking_id):
        self.booking_id=booking_id
        if self.booking_id in self.wll:
            BusBooking.wll.remove(self.booking_id)
            del BusBooking.dictwl[self.booking_id]
        elif len(self.wll)>0:
            BusBooking.dict1[self.wll[0]]=[self.dictwl[self.wll[0]][0],self.dict1[self.booking_id][1]]
            del BusBooking.dict1[self.booking_id]
        elif self.booking_id in self.dict1.keys()  :
            if (self.dict1[booking_id][1][0]=='W'):
                self.w.append(self.dict1[booking_id][1])
            elif (self.dict1[booking_id][1][0]=='A'):
                self.a.append(self.dict1[booking_id][1]) 
            del self.dict1[self.booking_id]    
                
    def status(self,booking_id):
                self.booking_id=booking_id
                if self.booking_id in self.dict1.keys():
                    print(self.dict1[self.booking_id])
                elif self.booking_id in self.wll:
                    print(self.dictwl[self.booking_id],'W'+str(self.wll.index(self.booking_id)))
                else:
                    print('invalid booking_id')
                return(self.booking_id,self.dict1[self.booking_id])
    def __str__(self):
                self.x=[(x,BusBooking.dict1[x][0],BusBooking.dict1[x][1]) for x in BusBooking.dict1.keys()]
                self.x=sorted(self.x)
                return str(self.x) 
    

