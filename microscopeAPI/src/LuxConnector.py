from luxconnector import LuxConnector

class LuxConnectorClass():

    def __init__(self):

        self.connector = LuxConnector(number_of_devices=1)
        self.serial_numbers = self.connector.get_all_serial_numbers()
        self.serial_number = self.serial_numbers[0]



    def setFocus(self, focus):

        '''
        This function will set the focus of the camera   
        '''

        self.connector.set_focus(self.serial_numbers, focus)
        return 'focus has changed'


    def getStack(self, num_img, start_focus, end_focus):

        '''
        This function will return a list of pillow images. Each image will be at a different focus level.

        This code will create a z-stack of 6 images. The focuses of these images will be [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        '''
        
        return self.connector.get_z_stack(self.serial_numbers, num_img, start_focus, end_focus)
    

    def getImage(self):

        '''
        This function will return an image from the microscope 
        '''

        return self.connector.get_image(self.serial_number)

    
    def getTemperature(self):

        '''
        This function will return the temperature of the device
        '''

        return self.connector.get_temperature(self.serial_number)
    

    def getSerialNumber(self):

        '''
        This function will return the serial_number of the microscope
        '''

        return self.serial_number