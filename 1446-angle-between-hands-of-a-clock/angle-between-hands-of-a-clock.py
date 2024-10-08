class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        perminangle = 360 / 60
        minangle = minutes * perminangle
        perhourangle = 360 / 12
        hour = hour%12
        hourangle = hour * perhourangle
        
        smallhrangle = 30 / 60
        smallhrangleval = minutes * smallhrangle
        finalhr = hourangle + smallhrangleval
        return min(abs(finalhr-minangle), 360-abs(finalhr-minangle))

        # elegant cal for hour angle:
        # hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

        