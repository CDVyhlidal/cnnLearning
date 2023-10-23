# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:58:58 2023

@author: Krimmet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from icecream import ic
from scipy import signal

import operator
import random

operators = {
    "&": operator.and_,
    "|": operator.or_,
    "^": operator.xor
}

def interference_maker(t, y, rfTime):
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    interference_frequency = ic(np.random.randint(1,1000))
    interference_duty = ic(np.random.rand()*.99+.01)
    interference_envelope = np.rint(.5*signal.square(2*np.pi*interference_frequency*t,duty=interference_duty)+.5).astype(int)
    interference_envelope = np.where((t>=interfereStart) & (t<=interfereStart+interfereDuration),interference_envelope,0)
    
    random_operation = random.choice(list(operators.keys()))
    y = np.where(interference_envelope,operators[random_operation](y,interference_envelope),y)
    
    # return y, interference_envelope
    return y



t = np.linspace(-1,6,7001)


#cat 1s
for a in range(100):
    
    ch4 = np.rint(.5*signal.square(2*np.pi*t/.02)+.5).astype(int)
    ch5 = np.rint(.5*signal.square(2*np.pi*t/.04)+.5).astype(int)
    ch6 = np.rint(.5*signal.square(2*np.pi*t/.08)+.5).astype(int)
    ch7 = np.rint(.5*signal.square(2*np.pi*t/.16)+.5).astype(int)
    ch8 = np.rint(.5*signal.square(2*np.pi*t/.32)+.5).astype(int)
    ch9 = np.rint(.5*signal.square(2*np.pi*t/.64)+.5).astype(int)

    random_shift = np.random.randint(0,1000)
    
    ch4 = np.roll(ch4,random_shift)
    ch5 = np.roll(ch5,random_shift)
    ch6 = np.roll(ch6,random_shift)
    ch7 = np.roll(ch7,random_shift)
    ch8 = np.roll(ch8,random_shift)
    ch9 = np.roll(ch9,random_shift)
    
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    
    df = pd.DataFrame()
    df['time'] = t
    df['ch4'] = ch4
    df['ch5'] = ch5
    df['ch6'] = ch6
    df['ch7'] = ch7
    df['ch8'] = ch8
    df['ch9'] = ch9
    df['rf'] = rf
    
    
    df.to_csv('./CNN_multichannel/cat_1/{}.csv'.format(a))

#cat 2s    
for a in range(400):

    ch4 = np.rint(.5*signal.square(2*np.pi*t/.02)+.5).astype(int)
    ch5 = np.rint(.5*signal.square(2*np.pi*t/.04)+.5).astype(int)
    ch6 = np.rint(.5*signal.square(2*np.pi*t/.08)+.5).astype(int)
    ch7 = np.rint(.5*signal.square(2*np.pi*t/.16)+.5).astype(int)
    ch8 = np.rint(.5*signal.square(2*np.pi*t/.32)+.5).astype(int)
    ch9 = np.rint(.5*signal.square(2*np.pi*t/.64)+.5).astype(int)

    random_shift = np.random.randint(0,1000)
    
    ch4 = np.roll(ch4,random_shift)
    ch5 = np.roll(ch5,random_shift)
    ch6 = np.roll(ch6,random_shift)
    ch7 = np.roll(ch7,random_shift)
    ch8 = np.roll(ch8,random_shift)
    ch9 = np.roll(ch9,random_shift)
    
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    
    
    interference_code = np.random.randint(1,64)
    interference_code = "{:08b}".format(interference_code)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    
    ch4 = interference_maker(t, ch4, rfTime)
    ch5 = interference_maker(t, ch5, rfTime)
    ch6 = interference_maker(t, ch6, rfTime)
    ch7 = interference_maker(t, ch7, rfTime)
    ch8 = interference_maker(t, ch8, rfTime)
    ch9 = interference_maker(t, ch9, rfTime)
    
    df = pd.DataFrame()
    df['time'] = t
    df['ch4'] = ch4
    df['ch5'] = ch5
    df['ch6'] = ch6
    df['ch7'] = ch7
    df['ch8'] = ch8
    df['ch9'] = ch9
    df['rf'] = rf
    
    
    df.to_csv('./CNN_multichannel/cat_2/{}.csv'.format(a))    

    
#cat 3s suppress
for a in range(34):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    y = np.where((t>=interfereStart) & (t<=(rfTime+.1)+1.4*np.random.rand()),0,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_3/{}.csv'.format(a))
    

    
#cat 4s suppress
for a in range(400):
    
    ch4 = np.rint(.5*signal.square(2*np.pi*t/.02)+.5).astype(int)
    ch5 = np.rint(.5*signal.square(2*np.pi*t/.04)+.5).astype(int)
    ch6 = np.rint(.5*signal.square(2*np.pi*t/.08)+.5).astype(int)
    ch7 = np.rint(.5*signal.square(2*np.pi*t/.16)+.5).astype(int)
    ch8 = np.rint(.5*signal.square(2*np.pi*t/.32)+.5).astype(int)
    ch9 = np.rint(.5*signal.square(2*np.pi*t/.64)+.5).astype(int)

    random_shift = np.random.randint(0,1000)
    
    ch4 = np.roll(ch4,random_shift)
    ch5 = np.roll(ch5,random_shift)
    ch6 = np.roll(ch6,random_shift)
    ch7 = np.roll(ch7,random_shift)
    ch8 = np.roll(ch8,random_shift)
    ch9 = np.roll(ch9,random_shift)
    
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    
    
    interference_code = np.random.randint(1,64)
    interference_code = "{:08b}".format(interference_code)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    
    ch4 = interference_maker(t, ch4, rfTime)
    ch5 = interference_maker(t, ch5, rfTime)
    ch6 = interference_maker(t, ch6, rfTime)
    ch7 = interference_maker(t, ch7, rfTime)
    ch8 = interference_maker(t, ch8, rfTime)
    ch9 = interference_maker(t, ch9, rfTime)
    

    
    kill_time = np.random.rand()*rfTime
    
    if int(np.random.rand()):
        ch4 = np.where(t>=kill_time,ch4[np.where(t>=kill_time)[0][0]],ch4)
        ch5 = np.where(t>=kill_time,ch5[np.where(t>=kill_time)[0][0]],ch5)
        ch6 = np.where(t>=kill_time,ch6[np.where(t>=kill_time)[0][0]],ch6)
        ch7 = np.where(t>=kill_time,ch7[np.where(t>=kill_time)[0][0]],ch7)
        ch8 = np.where(t>=kill_time,ch8[np.where(t>=kill_time)[0][0]],ch8)
        ch9 = np.where(t>=kill_time,ch9[np.where(t>=kill_time)[0][0]],ch9)
    else:
        ch4 = np.where(t>=kill_time,0,ch4)
        ch5 = np.where(t>=kill_time,0,ch5)
        ch6 = np.where(t>=kill_time,0,ch6)
        ch7 = np.where(t>=kill_time,0,ch7)
        ch8 = np.where(t>=kill_time,0,ch8)
        ch9 = np.where(t>=kill_time,0,ch9)
        
    
    df = pd.DataFrame()
    df['time'] = t
    df['ch4'] = ch4
    df['ch5'] = ch5
    df['ch6'] = ch6
    df['ch7'] = ch7
    df['ch8'] = ch8
    df['ch9'] = ch9
    df['rf'] = rf
    
    df.to_csv('./CNN_multichannel/cat_4/{}.csv'.format(a))  
    

    
    