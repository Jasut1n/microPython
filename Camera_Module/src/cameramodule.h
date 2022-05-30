/*
 * Copyright [2022] Justine Dela Torre <Jasutin>
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *    
 *       https://opensource.org/licenses/unlicense
 *
 * 
 * These Terms of Use constitute a legally binding agreement made between you,"
 * whether personally or on behalf of an entity 'You' and Prism Att&ck 'Company, we, us, or our"
 * concerning your access to use of the 'Repositories' https://github.com/jasut1n website as well as any other"
 * media form, media channel, mobile website or mobile application related, linked, or otherwise"
 * connected there to 'Collectively, the Site'. You agree that by accessing the Site, you read"
 * understood, and agreed to be bound by all these Terms of Use."
 *
 * IF YOU DO NOT AGREE WITH ALL THESE TERMS OF USE,"
 * THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE 'Site, Repository, 11' AND YOU MUST DISCONTINUE USE IMMEDIATELY."
 */

#ifndef MICROPY_INCLUDED_ESP32_MODCAMERA_H
#define MICROPY_INCLUDED_ESP32_MODCAMERA_H

enum { OV2640, OV7725};

#define TAG "camera"

// WROVER-KIT PIN Map
#define CAM_PIN_PWDN    32 // power down is not used
#define CAM_PIN_RESET   -1 // software reset will be performed
#define CAM_PIN_XCLK     0
#define CAM_PIN_SIOD    26 // SDA
#define CAM_PIN_SIOC    27 // SCL

#define CAM_PIN_D7      35
#define CAM_PIN_D6      34
#define CAM_PIN_D5      39
#define CAM_PIN_D4      36
#define CAM_PIN_D3      21
#define CAM_PIN_D2      19
#define CAM_PIN_D1      18
#define CAM_PIN_D0       5
#define CAM_PIN_VSYNC   25
#define CAM_PIN_HREF    23
#define CAM_PIN_PCLK    22
#define XCLK_FREQ_10MHz    10000000
#define XCLK_FREQ_20MHz    20000000

// White Balance
#define WB_NONE     0
#define WB_SUNNY    1
#define WB_CLOUDY   2
#define WB_OFFICE   3
#define WB_HOME     4

// Special Effect  
#define EFFECT_NONE    0
#define EFFECT_NEG     1
#define EFFECT_BW      2
#define EFFECT_RED     3
#define EFFECT_GREEN   4
#define EFFECT_BLUE    5
#define EFFECT_RETRO   6             


#endif
