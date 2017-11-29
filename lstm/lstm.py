

class LSTM(object):
    def __init__(self,iput_size,hidden_size,init_range=1.0,previous=None):
        self.input_size,self.hidden_size=input_size,hidden_size

        if previous:
            self.previous=previous
            previous.next=self

    def init(x,y):
        return initialize((x,y),init_range)

    h,n=hidden_size,iput_size

    self.W_hi,self.W_hf,self.W_ho,self.W_hj=init(h,h),init(h,h)