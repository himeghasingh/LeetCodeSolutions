class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        perminangle = 360 / 60
        minangle = minutes * perminangle
        perhourangle = 360 / 12
        hourangle = hour * perhourangle
        if hourangle == 360:
            hourangle = 0
        smallhrangle = 30 / 60
        smallhrangleval = minutes * smallhrangle
        finalhr = hourangle + smallhrangleval
        return min(abs(finalhr-minangle), 360-abs(finalhr-minangle))
        