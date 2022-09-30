
from dataclasses import dataclass, field


@dataclass
class Player:
    title: str
    slider_key: str
    name: str
    scouted_by: str
    scouted_age: int
    debut: str
    sold_from: str
    sold_for: int
    pre_16: dict = field(default_factory=lambda: {
        '009': None, '010': None, '011': None,
        '012': None, '013': None, '014': None,
        '015': None})
    post_16: dict = field(default_factory=lambda: {
        '016': None, '017': None, '018': None,
        '019': None, '020': None, '021': None})
    playing_time_1000s: dict = field(default_factory=lambda: {
        'FCN': None, 'SDFC': None})

    def debuted(self):
        return self.debut

    def __str__(self) -> str:
        return self.name

    def summary_text(self) -> str:
        string = ''
        string += self.name + \
            ' was first identified and recruited by ' + \
            self.scouted_by + ' at the age of ' + \
            str(self.scouted_age) + '.'
        string += ' He debuted with ' + \
            self.debut + ' and accured ' + \
            str(int(self.playing_time_1000s[self.debut]
                    * 1000)) + ' senior playing minutes for the club.'
        string += ' He was eventually sold outside of the Right to Dream Group by ' + \
            self.sold_from + ', having accured ' +   \
            str(int(self.playing_time_1000s[self.sold_from] * 1000)) + \
            ' senior playing minutes for the club.'
        return string

    def calculate_points(self, calibration):

        self.r = Results(0, 0, 0, 0, 0, 0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

        if self.scouted_age >= 16:
            scouted_points_adjusted = calibration['scouted_points'] * \
                calibration['scouted_multiplier']
        else:
            scouted_points_adjusted = calibration['scouted_points']
        # SCOUTED BY
        if self.scouted_by == "FCN":
            self.r.fcn += scouted_points_adjusted
        elif self.scouted_by == "SDFC":
            self.r.sdfc += scouted_points_adjusted
        elif self.scouted_by == "RTD-Ghana":
            self.r.rtd_g += scouted_points_adjusted
        elif self.scouted_by == "RTD-Egypt":
            self.r.rtd_e += scouted_points_adjusted
        elif self.scouted_by == "RTD-Denmark":
            self.r.rtd_d += scouted_points_adjusted
        elif self.scouted_by == "RTD-USA":
            self.r.rtd_u += scouted_points_adjusted

        # DEBUTED AT
        if self.debut == "FCN":
            self.r.fcn += calibration['debut_points']
        elif self.debut == "SDFC":
            self.r.sdfc += calibration['debut_points']

        # PLAYING MINUTES
        if self.playing_time_1000s['SDFC'] != None:
            self.r.sdfc += self.playing_time_1000s['SDFC'] * \
                calibration['playing_time']
        if self.playing_time_1000s['FCN'] != None:
            self.r.fcn += self.playing_time_1000s['FCN'] * \
                calibration['playing_time']

        # PRE-16 DEV
        if self.pre_16['009'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_9_points']
        elif self.pre_16['009'] == "RTD-Egypt":
            self.r.rtd_e += calibration[' _9_points']
        elif self.pre_16['009'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_9_points']
        elif self.pre_16['009'] == "RTD-USA":
            self.r.rtd_u += calibration['_9_points']

        if self.pre_16['010'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_10_points']
        elif self.pre_16['010'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_10_points']
        elif self.pre_16['010'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_10_points']
        elif self.pre_16['010'] == "RTD-USA":
            self.r.rtd_u += calibration['_10_points']

        if self.pre_16['011'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_11_points']
        elif self.pre_16['011'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_11_points']
        elif self.pre_16['011'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_11_points']
        elif self.pre_16['011'] == "RTD-USA":
            self.r.rtd_u += calibration['_11_points']

        if self.pre_16['012'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_12_points']
        elif self.pre_16['012'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_12_points']
        elif self.pre_16['012'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_12_points']
        elif self.pre_16['012'] == "RTD-USA":
            self.r.rtd_u += calibration['_12_points']

        if self.pre_16['013'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_13_points']
        elif self.pre_16['013'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_13_points']
        elif self.pre_16['013'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_13_points']
        elif self.pre_16['013'] == "RTD-USA":
            self.r.rtd_u += calibration['_13_points']

        if self.pre_16['014'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_14_points']
        elif self.pre_16['014'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_14_points']
        elif self.pre_16['014'] == "RTD-Denmark":
            self.r.rtd_e += calibration['_14_points']
        elif self.pre_16['014'] == "RTD-USA":
            self.r.rtd_e += calibration['_14_points']

        if self.pre_16['015'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_15_points']
        elif self.pre_16['015'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_15_points']
        elif self.pre_16['015'] == "RTD-Denmark":
            self.r.rtd_e += calibration['_15_points']
        elif self.pre_16['015'] == "RTD-USA":
            self.r.rtd_e += calibration['_15_points']

        # POST-16 DEV
        if self.post_16['016'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_16_points']
        elif self.post_16['016'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_16_points']
        elif self.post_16['016'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_16_points']
        elif self.post_16['016'] == "RTD-USA":
            self.r.rtd_u += calibration['_16_points']

        if self.post_16['017'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_17_points']
        elif self.post_16['017'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_17_points']
        elif self.post_16['017'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_17_points']
        elif self.post_16['017'] == "RTD-USA":
            self.r.rtd_u += calibration['_17_points']
        elif self.post_16['017'] == "FCN":
            self.r.fcn += calibration['_17_points']
        elif self.post_16['017'] == "SDFC":
            self.r.sdfc += calibration['_17_points']

        if self.post_16['018'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_18_points']
        elif self.post_16['018'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_18_points']
        elif self.post_16['018'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_18_points']
        elif self.post_16['018'] == "RTD-USA":
            self.r.rtd_u += calibration['_18_points']
        elif self.post_16['018'] == "FCN":
            self.r.fcn += calibration['_18_points']
        elif self.post_16['018'] == "SDFC":
            self.r.sdfc += calibration['_18_points']

        if self.post_16['019'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_19_points']
        elif self.post_16['019'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_19_points']
        elif self.post_16['019'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_19_points']
        elif self.post_16['019'] == "RTD-USA":
            self.r.rtd_u += calibration['_19_points']
        elif self.post_16['019'] == "FCN":
            self.r.fcn += calibration['_19_points']
        elif self.post_16['019'] == "SDFC":
            self.r.sdfc += calibration['_19_points']

        if self.post_16['021'] == "RTD-Ghana":
            self.r.rtd_g += calibration['_21_points']
        elif self.post_16['021'] == "RTD-Egypt":
            self.r.rtd_e += calibration['_21_points']
        elif self.post_16['021'] == "RTD-Denmark":
            self.r.rtd_d += calibration['_21_points']
        elif self.post_16['021'] == "RTD-USA":
            self.r.rtd_u += calibration['_21_points']
        elif self.post_16['021'] == "FCN":
            self.r.fcn += calibration['_21_points']
        elif self.post_16['021'] == "SDFC":
            self.r.sdfc += calibration['_21_points']

        if self.sold_from == "FCN":
            self.r.fcn += calibration['sold_by_points']
        elif self.sold_from == "SDFC":
            self.r.sdfc += calibration['sold_by_points']

        return self.r

    def trigger_calcs(self, calibration, fee_paid):
        self.calculate_points(calibration)
        self.r.total_points = self.r.get_total_points()
        self.r.calculate_share()

    def get_fees(self, fee_paid):
        if self.sold_for != None:
            return {
                'rtd_g': round(self.r.rtd_g_share * fee_paid, 2),
                'rtd_e': round(self.r.rtd_e_share * fee_paid, 2),
                'rtd_d': round(self.r.rtd_d_share * fee_paid, 2),
                'rtd_u': round(self.r.rtd_u_share * fee_paid, 2),
                'fcn': round(self.r.fcn_share * fee_paid, 2),
                'sdfc': round(self .r.sdfc_share * fee_paid, 2)
            }


@dataclass
class Results:
    rtd_g: int
    rtd_e: int
    rtd_d: int
    rtd_u: int
    fcn: int
    sdfc: int
    rtd_g_share: float
    rtd_e_share: float
    rtd_d_share: float
    rtd_u_share: float
    fcn_share: float
    sdfc_share: float
    total_points: float
    rtd_g_fiat: float
    rtd_e_fiat: float
    rtd_d_fiat: float
    rtd_u_fiat: float
    fcn_fiat: float
    sdfc_fiat: float

    def get_total_points(self):
        return self.rtd_g + self.rtd_e + \
            self.rtd_d + self.rtd_u + self.fcn + self.sdfc

    def calculate_share(self):
        if self.total_points > 0:
            self.rtd_g_share = round(self.rtd_g / self.total_points, 4)
            self.rtd_e_share = round(self.rtd_e / self.total_points, 4)
            self.rtd_d_share = round(self.rtd_d / self.total_points, 4)
            self.rtd_u_share = round(self.rtd_u / self.total_points, 4)
            self.fcn_share = round(self.fcn / self.total_points, 4)
            self.sdfc_share = round(self.sdfc / self.total_points, 4)
