
# Prerequisites

This project relies on the following libraries:
	
	- sys
	- getopt
	- os
	- re
	- time
	- bluepy

All of them should be installed already except bluepy which needs to be installed with:

	pip3 install bluepy

# Deployment Setups

	The project was developed for and on the **Raspberry Pi** Ecosystem.
	I suggest using it with raspbian. It might also work on the Ubuntu distro for it but the installation of bluepy makes some trouble.

# Usage:

	┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │ Usage:                                                                                                           │
    │    ./USBNinja.py -m <mode> [options]                                                                             │
    │                                                                                                                  │
    │ Modes:                                                                                                           │
    │    r                                                   Remote:       Mimics the USB ninja Remote                 │
    │    c                                                   Converter:    Converts ducky.txt payloads into USBNinja.c │
    │                                                                                                                  │
    │ Remote:                                                                                                          │
    │    ./USBNinja.py -m r -d <BDADDR>                                                                                │
    │                                                                                                                  │
    │ Commands of Interactive mode:                                                                                    │
    │    I or Info                                           " "s device info                                          │
    │    A or Button A                                       Triggers payload A                                        │
    │    B or Button B                                       Triggers payload B                                        │
    │    Q or Quit                                           Leaves interactive mode                                   │
    │                                                                                                                  │
    │ Converter:                                                                                                       │
    │    ./USBNinja.py -m c -i <input file> -j <input file 2> -o <output file> -l <keyboard language> -t <triggermode> │
    └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

# Attributes of the USBNinja GATT Server

	┌──────────────┬───────────────────────────────────────────────────────┬─────────────────┬───────────────────────────────────────────────────────────────┐
	│   Handles    │               Service > Characteristics               │   Properties    │                             Data                              │
	├──────────────┼───────────────────────────────────────────────────────┼─────────────────┼───────────────────────────────────────────────────────────────┤
	│ 0001 -> 0009 │ Generic Access (1800)                                 │                 │                                                               │
	│ 0003         │     Device Name (2a00)                                │ READ, WRITE     │ Ninja                                                         │
	│ 0005         │     Appearance (2a01)                                 │ READ            │ Unknown                                                       │
	│ 0007         │     Peripheral Preferred Connection Parameters (2a04) │ READ            │ Connection Interval: 8 -> 8                                   │
	│              │                                                       │                 │ Slave Latency: 0                                              │
	│              │                                                       │                 │ Connection Supervision Timeout Multiplier: 500                │
	│ 0009         │     2aa6                                              │ READ            │ 01                                                            │
	│              │                                                       │                 │                                                               │
	│ 000a -> 000d │ Generic Attribute (1801)                              │                 │                                                               │
	│ 000c         │     Service Changed (2a05)                            │ INDICATE        │                                                               │
	│              │                                                       │                 │                                                               │
	│ 000e -> 001e │ Device Information (180a)                             │                 │                                                               │
	│ 0010         │     Manufacturer Name String (2a29)                   │ READ            │ Proxgrind                                                     │
	│ 0012         │     Model Number String (2a24)                        │ READ            │ Ninja                                                         │
	│ 0014         │     Serial Number String (2a25)                       │ READ            │ 20190912                                                      │
	│ 0016         │     Hardware Revision String (2a27)                   │ READ            │ V2.0                                                          │
	│ 0018         │     Firmware Revision String (2a26)                   │ READ            │ V1.0                                                          │
	│ 001a         │     Software Revision String (2a28)                   │ READ            │ v5.0                                                          │
	│ 001c         │     System ID (2a23)                                  │ READ            │ d000000009e0000                                               │
	│ 001e         │     PnP ID (2a50)                                     │ READ            │ Vendor ID: 0x00d2 (Bluetooth SIG assigned Company Identifier) │
	│              │                                                       │                 │ Product ID: 0x0810                                            │
	│              │                                                       │                 │ Product Version: 0x0001                                       │
	│              │                                                       │                 │                                                               │
	│ 001f -> 002a │ fff0                                                  │                 │                                                               │
	│ 0021         │     fff1                                              │ NOTIFY          │                                                               │
	│ 0025         │     fff2                                              │ READ, WRITE     │ «Æ×ÏÒ1f*97¿¼M97Ú9c08Y0e14¦Áéí                                 │
	│ 0028         │     fff3                                              │ WRITE, NOTIFY   │                                                               │
	│              │                                                       │                 │                                                               │
	│ 002b -> ffff │ fe59                                                  │                 │                                                               │
	│ 002d         │     8ec90003f3154f609fb8838830daea50                  │ WRITE, INDICATE │                                                               │
	│              │                                                       │                 │                                                               │
	└──────────────┴───────────────────────────────────────────────────────┴─────────────────┴───────────────────────────────────────────────────────────────┘

# Planned Updates

	- Conversion from bluepy to the bluez5.x python library
	- GATT Server which imitates the function of the USBNinja Cable of the Raspberry Pi Nano (can be triggered by the USB Ninja Remote)