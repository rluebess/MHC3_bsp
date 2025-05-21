"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

def instantiateComponent(bspComponent):

    # LED 3: RB10-P23
    Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_NAME", "LED3")
    Database.setSymbolValue("core", "BSP_PIN_23_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_23_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_23_LAT", "")

    # LED 4: RB12-P27
    Database.setSymbolValue("core", "BSP_PIN_27_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_27_FUNCTION_NAME", "LED4")
    Database.setSymbolValue("core", "BSP_PIN_27_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_27_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_27_LAT", "")

    # LED 7: P28_RB13
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_NAME", "LED7")
    Database.setSymbolValue("core", "BSP_PIN_13_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_13_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_13_LAT", "")

    # LED 8: P12-RB11
    Database.setSymbolValue("core", "BSP_PIN_24_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_24_FUNCTION_NAME", "LED8")
    Database.setSymbolValue("core", "BSP_PIN_24_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_24_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_24_LAT", "")

    # USB_SEL: P13-RB3
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_NAME", "USB_SEL")
    Database.setSymbolValue("core", "BSP_PIN_13_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_13_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_13_LAT", "")

    # USB_HOST_CS: P55-RD7
    Database.setSymbolValue("core", "BSP_PIN_55_FUNCTION_TYPE", "SWITCH_AH")
    Database.setSymbolValue("core", "BSP_PIN_55_FUNCTION_NAME", "USB_HOST_CS")
    Database.setSymbolValue("core", "BSP_PIN_55_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_55_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_55_DIR", "")

    #USB_OVER: P42:RD8
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_NAME", "USB_OVER")
    Database.setSymbolValue("core", "BSP_PIN_42_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_42_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_42_DIR", "")

     #VBUS_AH USB_H_EN P12:RB4
    Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_TYPE", "VBUS_AH")
    Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_NAME", "VBUS_AH")
    Database.setSymbolValue("core", "BSP_PIN_23_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_23_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_23_LAT", "")



#   #Switch 1: RD6
#   Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_TYPE", "SWITCH_AL")
#   Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_NAME", "SWITCH1")
#   Database.setSymbolValue("core", "BSP_PIN_54_MODE", "DIGITAL")
#   Database.setSymbolValue("core", "BSP_PIN_54_PU", "True")
#   Database.setSymbolValue("core", "BSP_PIN_54_DIR", "")
#
#    # LED 1: RB10
#   Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_TYPE", "LED_AL")
#   Database.setSymbolValue("core", "BSP_PIN_23_FUNCTION_NAME", "RGB_LED_RED")
#   Database.setSymbolValue("core", "BSP_PIN_23_MODE", "DIGITAL")
#   Database.setSymbolValue("core", "BSP_PIN_23_DIR", "Out")
#   Database.setSymbolValue("core", "BSP_PIN_23_LAT", "")
#
#   # LED 2: RB3
#   Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_TYPE", "LED_AL")
#   Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_NAME", "RGB_LED_GREEN")
#   Database.setSymbolValue("core", "BSP_PIN_13_MODE", "DIGITAL")
#   Database.setSymbolValue("core", "BSP_PIN_13_DIR", "Out")
#   Database.setSymbolValue("core", "BSP_PIN_13_LAT", "")
#
#   # LED 3: RB2
#   Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_TYPE", "LED_AL")
#   Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_NAME", "RGB_LED_BLUE")
#   Database.setSymbolValue("core", "BSP_PIN_14_MODE", "DIGITAL")
#   Database.setSymbolValue("core", "BSP_PIN_14_DIR", "Out")
#   Database.setSymbolValue("core", "BSP_PIN_14_LAT", "")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")
    
    # Clock setting
    Database.setSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL", 8000000)

    BSP_NAME = "pic32mx440H_cas_host_explorer"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
