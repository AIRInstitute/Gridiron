from opentrons import protocol_api
from opentrons import types
import numpy as np
from opentrons.types import Location, Point
import datetime

metadata = {'apiLevel': '2.12'}

def run(protocol):
        def create_history (nLetters,number):
                history = []
                #For A to Letter
                for i in range(0,nLetters):
                        #For 1 to number
                        for j in range(0,number):
                                #Add the string to the list
                                history.append(str(chr(65+i))+str(j+1))
                return history

        def back_home(pipette300):
                if (pipette300.has_tip):
                        pipette300.drop_tip()
                protocol.home() 
                pipette300.home_plunger()
                pipette300.home() 

        def tilt_down():
                p300.move_to(plate1['A1'].top(78).move(Point(x=9,y = 12)),minimum_z_height= 100)
                p300.move_to(plate1['A1'].top(65).move(Point(x=9,y = 12)),minimum_z_height=100)
                p300.move_to(plate1['A1'].top(80).move(Point(x=9,y = 12)),minimum_z_height=100)

        def tilt_up():
                p300.move_to(plate1['A1'].top(57.8).move(Point(x=70,y = 12)))

        def tilted(well,operation,i):
                left_z = 56.82 #20.22
                right_z = 83.92 #25.42
                left_x = 3.38 #4.38
                right_x = 117.38 # 119.38
                # angle = np.arctan2((right_z - left_z), (right_x - left_x))  # np.rad2deg(angle)
                angle = 0.19687313962496036
                # angle = 0.23338737934210896
                x = well.bottom().point.x - well.diameter / 2
                y_dash = well.bottom().point.y
                z = well.bottom().point.z

                x_dash = (x * np.cos(angle)) - (z * np.sin(angle))
                z_dash = ((x * np.sin(angle)) + (z * np.cos(angle))) + left_z

                new_x = x_dash - well.bottom().point.x
                new_y = y_dash
                new_z = z_dash - z - 90
 
                # new_pos = well.bottom().move(types.Point(new_x, 1, new_z)) # old -14
                radius = (well.diameter / 2)*0.75
                if(operation): # operation == ASPIRATE
                        if i==1:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==2:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==3:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==4:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==5:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==6:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==7:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==8:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==9:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==10:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                        else:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-10)) # old -14
                                print(new_pos)
                                return new_pos
                else: # Operation == DISPENSE
                        if i==1:
                                new_pos = well.bottom().move(types.Point(new_x+radius, 1, new_z+10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==2:
                                new_pos = well.bottom().move(types.Point(new_x+12, 1+12, new_z+10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==3:
                                new_pos = well.bottom().move(types.Point(new_x-12, 1+12, new_z+10)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==4:
                                new_pos = well.bottom().move(types.Point(new_x, 1+radius, new_z)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==5:
                                new_pos = well.bottom().move(types.Point(new_x, 1-radius, new_z)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==6:
                                new_pos = well.bottom().move(types.Point(new_x, 1, new_z)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==7:
                                new_pos = well.bottom().move(types.Point(new_x-13, 1-13, new_z)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==8:
                                new_pos = well.bottom().move(types.Point(new_x-13, 1+13, new_z-5)) # old -14
                                print(new_pos)
                                return new_pos
                        if i==9:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z-5)) # old -14
                                print(new_pos)
                                return new_pos
                        else:
                                new_pos = well.bottom().move(types.Point(new_x-radius, 1, new_z+10)) # old -14
                                print(new_pos)
                                return new_pos

                
        tiprack1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
        tiprack1000_history = create_history(8,12)
        # tiprack1000.set_offset(x=-0.60, y=0.40, z=0.00)
        plate1 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 5)
        plate1.set_offset(x= 25 , y = 1, z =70 )
        eppendorf = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)

        p300 = protocol.load_instrument('p1000_single_gen2', mount='right')
        eppendorf_history = create_history(4,6)

        timeStart = datetime.datetime.now()

        #tilt the plate down
        # tilt_down()

        ASPIRATE = True
        DISPENSE = False

        vol = 215
        height = 40
        timeFirstTransfeStart = datetime.datetime.now()
        for m in [0,1]:
                for w in plate1.rows()[m][:3]:
                        p300.pick_up_tip(tiprack1000[tiprack1000_history[0]])
                        p300.move_to(tiprack1000[tiprack1000_history[0]].top(height))
                        tiprack1000_history.pop(0)
                        for i in range(1,10):
                                # p300.move_to(w.top(height))
                                p300.aspirate(vol,tilted(w,ASPIRATE,i))
                                p300.dispense(vol,tilted(w,DISPENSE,i))
                        p300.aspirate(vol,tilted(w,ASPIRATE,10))
                        p300.move_to(w.top(height))
                        p300.dispense(vol,eppendorf[eppendorf_history[0]])
                        p300.move_to(eppendorf[eppendorf_history[0]].top(height))
                        eppendorf_history.pop(0)
                        p300.drop_tip()

                        timeFirstTransferEnd = datetime.datetime.now()
        
        timeEnd = datetime.datetime.now()
        protocol.comment("Protocol 6 finished")
        back_home(p300)

        print("timeStart: " + str(timeStart))
        protocol.comment("timeStart: " + str(timeStart))

        print("timeEnd: " + str(timeEnd))
        protocol.comment("timeEnd: " + str(timeEnd))

         #------------------------------------------
        # Create datamodel
        #------------------------------------------

        data = {
            'timeStart': {
                "type": "datetime",
                "value": timeStart.isoformat()
            },
            'timeFirstTransfeStart': {
                "type": "datetime",
                "value":timeFirstTransfeStart.isoformat()
            },
            'timeFirstTransferEnd': {
                "type": "datetime",
                "value": timeFirstTransferEnd.isoformat()
            },
            'intervalSetup':{
                "type": "Float",
                "value": (timeFirstTransfeStart - timeStart).total_seconds()
            },
            'intervalFirstTransfer':{
                "type": "Float",
                "value":(timeFirstTransferEnd - timeFirstTransfeStart).total_seconds()
            },
            'intervalTransfer':{
                "type": "Float",
                "value": (timeEnd - timeFirstTransferEnd).total_seconds()
            },
            'intervalProcess':{
                "type": "Float",
                "value": (timeEnd - timeStart).total_seconds()
            },
            'protocol':{
                "type":"Integer",
                "value":3
            }
        }

        #------------------------------------------
        # Create data file
        #------------------------------------------
        # try:
        #     with open('json_data.json', 'w') as outfile:
        #         json.dump(data, outfile)        

        # except Exception as e:
        #     print("Error creating data file ")
        #     print(e)
        #     protocol.comment("Error creating data file ")
        #     protocol.comment(e)
