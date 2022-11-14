from opentrons import protocol_api
from opentrons import types
import numpy as np
from opentrons.types import Location, Point

metadata = {'apiLevel': '2.12'}

def run(protocol):

        def tilt_down():
                p300.move_to(plate1['A1'].top(78).move(Point(x=9,y = 12)),minimum_z_height= 100)
                p300.move_to(plate1['A1'].top(65).move(Point(x=9,y = 12)),minimum_z_height=100)

        def tilt_up():
                p300.move_to(plate1['A1'].top(57.8).move(Point(x=70,y = 12)))


        def tilted(well,l_x=3.38, r_x=117.38, l_z=56.82, r_z=83.92):
                left_z = l_z #20.22
                right_z = r_z #25.42
                left_x = l_x #4.38
                right_x = r_x# 119.38
                angle = np.arctan2((right_z - left_z), (right_x - left_x))  # np.rad2deg(angle)
                x = well.bottom().point.x - well.diameter / 2
                y_dash = well.bottom().point.y
                z = well.bottom().point.z

                x_dash = (x * np.cos(angle)) - (z * np.sin(angle))
                z_dash = ((x * np.sin(angle)) + (z * np.cos(angle))) + left_z

                new_x = x_dash - well.bottom().point.x
                new_y = y_dash
                new_z = z_dash - z
 
                new_pos = well.bottom().move(types.Point(new_x, 1, new_z-14.3)) # old -14
                print(new_pos)
                return new_pos
                
        tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
        tiprack1.set_offset(x=-0.60, y=0.40, z=0.00)
        plate1 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 5)
        plate1.set_offset(x= 0 , y = 1, z =0 )
        res = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)

        p300 = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tiprack1])

        #tilt the plate down
        tilt_down()

        p300.pick_up_tip()
        vol = 215
        height = 115
        p300.aspirate(1,res['A1'].top(height))
        p300.dispense(1,res['A1'].top(height))
        for m in [0,1]:
                for w in plate1.rows()[m][:3]:
                        #p300.move_to(tilted(w),minimum_z_height=80)
                        #p300.move_to(tilted(w),minimum_z_height=80)
                        p300.aspirate(vol,tilted(w))
                        protocol.delay(1)
                        p300.move_to(res['A1'].top(25),minimum_z_height=height)
                        p300.dispense(vol)
                        p300.blow_out(res['A1'].top(25))
                        p300.aspirate(1,res['A1'].top(25))
                        p300.dispense(1,res['A1'].top(25))
                        p300.move_to(w.top(height))

        p300.drop_tip()

        tilt_up()