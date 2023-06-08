import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


t = np.linspace(-1,6,48001)

#cat 1s
for a in range(100):
    y = .1*np.random.rand(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_1/{}.csv'.format(a))
    

#cat 2s suppress
for a in range(34):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    y = np.where((t>=interfereStart) & (t<=interfereStart+interfereDuration),0,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_2/{}.csv'.format(a))
    
#cat 2s high
for a in range(34,67):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart) & (t<=interfereStart+interfereDuration),np.maximum(noise,y),y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_2/{}.csv'.format(a))
    
#cat 2s noisy
for a in range(67,100):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart) & (t<=interfereStart+interfereDuration),2*np.random.rand(len(t))-1,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_2/{}.csv'.format(a))
    
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
    
#cat 3s high
for a in range(34,67):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart) & (t<=(rfTime+.1)+1.4*np.random.rand()),np.maximum(noise,y),y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_3/{}.csv'.format(a))
    
#cat 3s noisy
for a in range(67,100):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart) & (t<=(rfTime+.1)+1.4*np.random.rand()),2*np.random.rand(len(t))-1,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_3/{}.csv'.format(a))
    
#cat 4s suppress
for a in range(34):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    y = np.where((t>=interfereStart),0,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_4/{}.csv'.format(a))
    
#cat 4s high
for a in range(34,67):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart),np.maximum(noise,y),y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_4/{}.csv'.format(a))
    
#cat 4s noisy
for a in range(67,100):
    y = np.zeros(len(t))
    for b in range(3):
        y = y + (np.random.rand()*.2+.1)*np.sin(np.random.randint(150,750,1)*2*np.pi*t+np.random.rand()*2*np.pi)
    y = y/np.max(np.abs(y))
    rf = np.zeros(len(t))
    rfTime = np.random.rand()*2.5+.5
    rf = np.where((t>=0) & (t<=rfTime),1,0)
    interfereStart = np.random.rand()*(rfTime-.1)
    interfereDuration = (rfTime-interfereStart)*np.random.rand()
    noise = np.random.rand(len(t))*.5+.5
    y = np.where((t>=interfereStart),2*np.random.rand(len(t))-1,y)
    y = y + .1*np.random.rand(len(t))
    df = pd.DataFrame(columns=['time','amplitude','rf'])
    df['time'] = t
    df['amplitude'] = y
    df['rf'] = rf
    df.to_csv('./Documents/fooData/cat_4/{}.csv'.format(a))
