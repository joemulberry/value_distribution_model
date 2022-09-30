

def create_summary_text(player):

    string = ''
    string += player['name'] + \
        ' was first identified and recruited by ' + \
        player['scouted_by'] + ' at the age of ' + \
        str(player['scouted_age']) + '.'

    string += ' He debuted with ' + \
        player['debut'] + ' and accured ' + \
        str(int(player['playing_time_1000s'][player['debut']]
                * 1000)) + ' senior playing minutes for the club.'

    string += ' He was eventually sold outside of the Right to Dream Group by ' + \
        player['sold_from'] + ' at the age of ' + str(player['scouted_age']) + ', having accured ' + \
        str(int(player['playing_time_1000s'][player['sold_from']] * 1000)) + \
        ' senior playing minutes for the club.'

    return string


def calculate_points(player,
                     sold_by_points,
                     scouted_points,
                     scouted_multiplier,
                     debut_points,
                     playing_time,
                     _9_points,
                     _10_points,
                     _11_points,
                     _12_points,
                     _13_points,
                     _14_points,
                     _15_points,
                     _16_points,
                     _17_points,
                     _18_points,
                     _19_points,
                     _20_points,
                     _21_points):

    fcn_counter = 0
    sdfc_counter = 0
    rtdE_counter = 0
    rtdG_counter = 0
    rtdU_counter = 0
    rtdD_counter = 0

    if player['scouted_age'] >= 16:
        scouted_points_adjusted = scouted_points * scouted_multiplier
    else:
        scouted_points_adjusted = scouted_points

    if player['sold_from'] == "FCN":
        fcn_counter += sold_by_points
    elif player['sold_from'] == "RTD-Ghana":
        rtdG_counter += sold_by_points
    elif player['sold_from'] == "SDFC":
        sdfc_counter += sold_by_points

    if player['scouted_by'] == "FCN":
        fcn_counter += scouted_points_adjusted
    elif player['scouted_by'] == "RTD-Ghana":
        rtdG_counter += scouted_points_adjusted
    elif player['scouted_by'] == "SDFC":
        sdfc_counter += scouted_points_adjusted

    if player['debut'] == "FCN":
        fcn_counter += debut_points
    elif player['debut'] == "RTD-Ghana":
        rtdG_counter += debut_points
    elif player['debut'] == "SDFC":
        sdfc_counter += debut_points

    fcn_counter += player['playing_time_1000s']['FCN'] * playing_time
    if player['playing_time_1000s']['SDFC'] != None:
        sdfc_counter += player['playing_time_1000s']['SDFC'] * playing_time

    if player['pre_16']['009'] == "FCN":
        fcn_counter += _9_points
    elif player['pre_16']['009'] == "RTD-Ghana":
        rtdG_counter += _9_points
    elif player['pre_16']['009'] == "SDFC":
        sdfc_counter += _9_points

    if player['pre_16']['010'] == "FCN":
        fcn_counter += _10_points
    elif player['pre_16']['010'] == "RTD-Ghana":
        rtdG_counter += _10_points
    elif player['pre_16']['010'] == "SDFC":
        sdfc_counter += _10_points

    if player['pre_16']['011'] == "FCN":
        fcn_counter += _11_points
    elif player['pre_16']['011'] == "RTD-Ghana":
        rtdG_counter += _11_points
    elif player['pre_16']['011'] == "SDFC":
        sdfc_counter += _11_points

    if player['pre_16']['012'] == "FCN":
        fcn_counter += _12_points
    elif player['pre_16']['012'] == "RTD-Ghana":
        rtdG_counter += _12_points
    elif player['pre_16']['012'] == "SDFC":
        sdfc_counter += _12_points

    if player['pre_16']['013'] == "FCN":
        fcn_counter += _13_points
    elif player['pre_16']['013'] == "RTD-Ghana":
        rtdG_counter += _13_points
    elif player['pre_16']['013'] == "SDFC":
        sdfc_counter += _13_points

    if player['pre_16']['014'] == "FCN":
        fcn_counter += _14_points
    elif player['pre_16']['014'] == "RTD-Ghana":
        rtdG_counter += _14_points
    elif player['pre_16']['014'] == "SDFC":
        sdfc_counter += _14_points

    if player['pre_16']['015'] == "FCN":
        fcn_counter += _15_points
    elif player['pre_16']['015'] == "RTD-Ghana":
        rtdG_counter += _15_points
    elif player['pre_16']['015'] == "SDFC":
        sdfc_counter += _15_points

    if player['post_16']['016'] == "FCN":
        fcn_counter += _16_points
    elif player['post_16']['016'] == "RTD-Ghana":
        rtdG_counter += _16_points
    elif player['post_16']['016'] == "SDFC":
        sdfc_counter += _16_points

    if player['post_16']['017'] == "FCN":
        fcn_counter += _17_points
    elif player['post_16']['017'] == "RTD-Ghana":
        rtdG_counter += _17_points
    elif player['post_16']['017'] == "SDFC":
        sdfc_counter += _17_points

    if player['post_16']['017'] == "FCN":
        fcn_counter += _17_points
    elif player['post_16']['017'] == "RTD-Ghana":
        rtdG_counter += _17_points
    elif player['post_16']['017'] == "SDFC":
        sdfc_counter += _17_points

    if player['post_16']['018'] == "FCN":
        fcn_counter += _18_points
    elif player['post_16']['018'] == "RTD-Ghana":
        rtdG_counter += _18_points
    elif player['post_16']['018'] == "SDFC":
        sdfc_counter += _18_points

    if player['post_16']['019'] == "FCN":
        fcn_counter += _19_points
    elif player['post_16']['019'] == "RTD-Ghana":
        rtdG_counter += _19_points
    elif player['post_16']['019'] == "SDFC":
        sdfc_counter += _19_points

    if player['post_16']['020'] == "FCN":
        fcn_counter += _20_points
    elif player['post_16']['020'] == "RTD-Ghana":
        rtdG_counter += _20_points
    elif player['post_16']['020'] == "SDFC":
        sdfc_counter += _20_points

    if player['post_16']['021'] == "FCN":
        fcn_counter += _21_points
    elif player['post_16']['021'] == "RTD-Ghana":
        rtdG_counter += _21_points
    elif player['post_16']['021'] == "SDFC":
        sdfc_counter += _21_points

    total_points = rtdG_counter + fcn_counter + sdfc_counter
    # st.write('rtd_counter', rtd_counter, round(rtd_counter / total_points,
    #                                            2), round(rtd_counter / total_points, 2) * player['sold_for'])
    # st.write('fcn_counter', fcn_counter, round(fcn_counter / total_points,
    #                                            2), round(fcn_counter / total_points, 2) * player['sold_for'])
    # st.write('sdfc_counter', sdfc_counter,
    #          round(sdfc_counter / total_points, 2), round(sdfc_counter / total_points, 2) * player['sold_for'])

    new = {
        'rtd_points': rtdG_counter,
        'fcn_points': fcn_counter,
        'sdfc_points': sdfc_counter,
        'total_points': rtdG_counter + fcn_counter + sdfc_counter,
        'rtd_pct_share': round(rtdG_counter / total_points, 2),
        'fcn_pct_share': round(fcn_counter / total_points, 2),
        'sdfc_pct_share': round(sdfc_counter / total_points, 2),
        'rtd_share': round(rtdG_counter / total_points, 2) * player['sold_for'],
        'fcn_share': round(fcn_counter / total_points, 2) * player['sold_for'],
        'sdfc_share': round(sdfc_counter / total_points, 2) * player['sold_for'],
        'player': player
    }

    return new


def get_css():

    return [
        """
            <style>
            .big-font {
                font-size:26px !important;
                font-weight: bold !important;
                text-align: center !important;
                margin: -1.5rem -1rem 1rem -1rem;
            }
            </style>
            """,
        """
            <style>
            .yoyo-font {
                font-size:22px !important;
                font-weight: semibold !important;
            }
            </style>
            """,
        """
            <style>
            .title-font {
                font-size:34px !important;
                font-weight: bold !important;
                text-align: center !important;
            }
            </style>
            """,
        """
            <style>
            .light-font {
                font-size:14px !important;
                font-weight: lighter; !important;
                text-align: center !important;
                margin: -1.5rem -1rem 1rem -1rem;

            }
            </style>
            """,
        """
            <style>
            .centered-text {
                text-align: center !important;
            }
            </style>
            """,
        """
            <style>
            .centered-image {
                display: block !important;
                margin-left: auto !important;
                margin-right: auto !important;
                
            }
            </style>
            """

    ]


def create_logos():
    return {
        'fcn': '<img src ="https://github.com/FCrSTATS/helper/blob/main/images/FCN%20Logo%20R&Y.png?raw=true" class="centered-image" width="100"></img>',
        'sdfc': '<img src="https://github.com/FCrSTATS/helper/blob/b06f01ad9f64911708408070b5b39bbe8b915cca/images/sdfc%20lgoo.png?raw=true" class="centered-image" width="100"></img>',
        'rtd_g': '<img src="https://github.com/FCrSTATS/helper/blob/main/images/RTD_Academy_Crests_Ghana.png?raw=true" class="centered-image" width="100"></img>',
        'rtd_u': '<img src="https://github.com/FCrSTATS/helper/blob/main/images/rtd_usa.png?raw=true" class="centered-image" width="100"></img>',
        'rtd_e': '<img src="https://github.com/FCrSTATS/helper/blob/main/images/RTD_Academy_Crests_Egypt.png?raw=true" class="centered-image" width="100"></img>',
        'rtd_d': '<img src="https://github.com/FCrSTATS/helper/blob/main/images/RTD_Academy_Crests_Denmark.png?raw=true" class="centered-image" width="100"></img>'
    }
