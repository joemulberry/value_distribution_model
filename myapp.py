# Import Packages
from ctypes import RTLD_GLOBAL
from dataclasses import dataclass, field
import streamlit as st
import pandas as pd
from random import randint
from matplotlib import pyplot as plt
from utils import calculate_points, create_summary_text, get_css, create_logos
from players import get_players
from settings import get_initial_values
from class_store import Player, Results

initial_vals = get_initial_values()
players = get_players()
logos = create_logos()


# refactor to UTILS TODO

def get_fiat_text(fiat):
    return '<p class="big-font">€' + str(fiat) + 'm</p>'


if 'players_class' in st.session_state:
    players_class = st.session_state.players_class
else:
    players_class = []
    for p in players:
        players_class.append(Player(
            title=p['title'],
            slider_key=p['slider_key'],
            debut=p['debut'],
            name=p['name'],
            scouted_by=p['scouted_by'],
            scouted_age=p['scouted_age'],
            sold_for=p['sold_for'],
            sold_from=p['sold_from'],
            pre_16=p['pre_16'],
            post_16=p['post_16'],
            playing_time_1000s=p['playing_time_1000s']
        ))

# players_class = []
calibrations = None

st.title('Value Distribution Model')
intro, setttings, examples, add_player = st.tabs(
    ["Introduction", "Settings", "Examples", "Add a Player"])


with intro:
    st.subheader('Model Introduction')
    intro_col1, intro_col2 = st.columns([3, 2])
    with intro_col1:
        st.write('When players transfer between the clubs and academies owned or operated by the Right to Dream Group they do so at no acquisition cost for the acquiring club. However, in the result of a player being transferred to a club outside of the Right to Dream Group; the fee, if any, is fairly distributed to the Right to Dream clubs and academies that contributed to their development. Such a mechanism encourages collaboration between Right to Dream organisations in player trading and succession planning. The Value Distribution Model (VDM) is used to calculate the distribution of transfer profits (net of acquistion costs).')
    with intro_col2:
        st.image(
            'https://www.espldaily.com/wp-content/uploads/2021/07/219363963_911524162735780_1056505399119593431_n.jpg')

    st.write("The model takes a players history within Right to Dream and allocates points to the organisations that are responsible for various processes or milestones that feature. Such processes and milestones can be catergoriesd into 4 main buckets: 1) Recruitment 2) Development 3) Senior Football 4) Value Realisation. More detailed explainers can be viewed within the 'settings' tab")
    st.write("Once the points have been allocated, each organisation can tally their points and calcuate its % of total points - this represents their % share of the transfer profits. For example, if Right to Dream Ghana are allocated 30 points, while FCN is allocated 70 points, RTD-Ghana would receive 30% of the transfer profits whilst FCN would receive 70% .")

with setttings:
    st.subheader('Points Allocation')
    st.success(
        "You can change the points allocation per factor can be experimented with. The changes won' be saved")
    st.write("The factors chosen, to be rewarded with points, reflect the journey of a player's development as well as significant points of value capture or value growth along the way. The Right to Dream Process rewarded. These factors are:")
    st.subheader("**1. Identified and Recruited By**")
    st.write("High quality players are essential for the The Right to Dream player development model to develop players of the highest quality. Therefore the organisation that initially identifies and recruits the player is rewarded.")
    with st.expander("Expand to Change Identified and Recruited By Points"):
        scouted_points = st.slider(
            '', min_value=0, max_value=10, value=initial_vals['scouted']['points'])
        scouted_multiplier = st.slider(
            'Multiplier for Players Recruited at 16+', min_value=0.0, max_value=5.0, value=initial_vals['scouted']['multiplier'], step=0.1)

    st.subheader('**2. Development Pre-16**')
    st.write("The development of a player before the age of 16 years old is vitally important and is at the very core of our development model.")
    with st.expander("Expand to Change Pre-16 Development Points"):
        col1, col2, col3 = st.columns(3)
        with col1:
            _9_points = st.slider(
                '9 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_9'])
            _12_points = st.slider(
                '12 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_12'])
            _15_points = st.slider(
                '15 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_15'])

        with col2:
            _10_points = st.slider(
                '10 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_10'])
            _13_points = st.slider(
                '13 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_13'])

        with col3:
            _11_points = st.slider(
                '11 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_11'])
            _14_points = st.slider(
                '14 Year Points', min_value=0, max_value=5, value=initial_vals['pre_16']['_14'])

    st.subheader('**3. Development Post-16**')
    st.write("The development of a player's talent between 16-21 is also important and happens across our group.")
    with st.expander("Expand to Change Post-16 Development Points"):
        post16_col1, post16_col2, post16_col3 = st.columns(3)
        with post16_col1:
            _16_points = st.slider(
                '16 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_16'])
            _19_points = st.slider(
                '19 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_19'])
        with post16_col2:
            _17_points = st.slider(
                '17 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_17'])
            _20_points = st.slider(
                '20 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_20'])
        with post16_col3:
            _18_points = st.slider(
                '18 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_18'])
            _21_points = st.slider(
                '21 Year Points', min_value=0, max_value=5, value=initial_vals['post_16']['_21'])

    st.subheader('**4. Professional Debut**')
    st.write("Organisations that give a player their debut should be rewarded for believing in the player and giving his first step in senior football.")
    with st.expander("Expand to Change Professional Debut Points"):
        debut_points = st.slider(
            '', min_value=0, max_value=10, value=initial_vals['debut'])

    st.subheader('**5. Senior Playing Time (per 1000 minutes)**')
    st.write("Playing minutes help the player develop but also help facilitate growth in market value of the player, it should therefore be rewarded.")
    with st.expander("Expand to Change Senior Playing Time Points"):
        playing_time = st.slider(
            'Playing Time', min_value=0, max_value=10, value=initial_vals['playing_time'])

    st.subheader('**6. Sold By**')
    st.write("Evenutally selling the player outside of the Right to Dream organisation represents the point at which value is realised. The organisation that makes this sale should be rewarded.")
    with st.expander("Expand to Change Sold By Points"):
        sold_by_points = st.slider(
            'Sold By', min_value=0, max_value=10, value=initial_vals['sold_by'])

    calibrations = {
        'sold_by_points': sold_by_points,
        'scouted_points': scouted_points,
        'scouted_multiplier': scouted_multiplier,
        'debut_points': debut_points,
        'playing_time': playing_time,
        '_9_points': _9_points,
        '_10_points': _10_points,
        '_11_points': _11_points,
        '_12_points': _12_points,
        '_13_points': _13_points,
        '_14_points': _14_points,
        '_15_points': _15_points,
        '_16_points': _16_points,
        '_17_points': _17_points,
        '_18_points': _18_points,
        '_19_points': _19_points,
        '_20_points': _20_points,
        '_21_points': _21_points
    }


with add_player:

    extra_player = {'title': 'Template Player',
                    'slider_key': '1a',
                    'image_url': 'https://fmdataba.com/images/p2/660215.png',
                    'name': 'Template',
                    'scouted_by': 'RTD-Ghana',
                    'scouted_age': 12,
                    'pre_16': {
                        '009': 'RTD-Ghana',
                        '010': None,
                        '011': None,
                        '012': 'RTD-Ghana',
                        '013': 'RTD-Ghana',
                        '014': 'RTD-Ghana',
                        '015': 'RTD-Ghana'
                    },
                    'post_16': {
                        '016': 'RTD-Ghana',
                        '017': 'RTD-Ghana',
                        '018': 'FCN',
                        '019': 'FCN',
                        '020': 'FCN',
                        '021': 'FCN'
                    },
                    'debut': 'FCN',
                    'playing_time_1000s': {
                        'FCN': 2.944,
                        'SDFC': None
                    },
                    'sold_from': 'FCN',
                    'sold_for': 1.0
                    }

    st.header("Add a Player Scenario")

    academies = ['RTD-Ghana', 'RTD-Denmark',
                 'RTD-Egypt', 'RTD-USA', 'FCN', 'SDFC', None]

    extra_player['name'] = st.text_input('Player Name', extra_player['name'])
    extra_player['title'] = extra_player['name']

    scouted1, scouted2 = st.columns(2)

    with scouted1:
        extra_player['scouted_by'] = st.selectbox(
            'Scouted By', academies, key="scouted_by")
    with scouted2:
        extra_player['scouted_age'] = st.selectbox(
            'Scouted Age', [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], key="scouted_age")

    where1, where2, where3 = st.columns(3)

    with where1:

        extra_player['pre_16']['009'] = st.selectbox(
            'Where at 9?', academies, key="at9",
            index=academies.index(extra_player['pre_16']['009']))

        extra_player['pre_16']['012'] = st.selectbox(
            'Where at 12?', academies, key="at12",
            index=academies.index(extra_player['pre_16']['012']))

        extra_player['pre_16']['015'] = st.selectbox(
            'Where at 15?', academies, key="at15",
            index=academies.index(extra_player['pre_16']['015']))

        extra_player['post_16']['018'] = st.selectbox(
            'Where at 18?', academies, key="at18",
            index=academies.index(extra_player['post_16']['018']))

        extra_player['post_16']['021'] = st.selectbox(
            'Where at 21?', academies, key="at21",
            index=academies.index(extra_player['post_16']['021']))

    with where2:
        extra_player['pre_16']['010'] = st.selectbox(
            'Where at 10', academies, key="at10",
            index=academies.index(extra_player['pre_16']['010']))

        extra_player['pre_16']['013'] = st.selectbox(
            'Where at 13?', academies, key="at13",
            index=academies.index(extra_player['pre_16']['013']))

        extra_player['post_16']['016'] = st.selectbox(
            'Where at 16?', academies, key="at16",
            index=academies.index(extra_player['post_16']['016']))

        extra_player['post_16']['019'] = st.selectbox(
            'Where at 19?', academies, key="at19",
            index=academies.index(extra_player['post_16']['019']))

    with where3:
        extra_player['pre_16']['011'] = st.selectbox(
            'Where at 11?', academies, key="at11",
            index=academies.index(extra_player['pre_16']['011']))

        extra_player['pre_16']['014'] = st.selectbox(
            'Where at 14?', academies, key="at14",
            index=academies.index(extra_player['pre_16']['014']))

        extra_player['post_16']['017'] = st.selectbox(
            'Where at 17?', academies, key="at17",
            index=academies.index(extra_player['post_16']['017']))

        extra_player['post_16']['020'] = st.selectbox(
            'Where at 20?', academies, key="at20",
            index=academies.index(extra_player['post_16']['020']))

    debut_col, sold_col = st.columns(2)

    with debut_col:
        extra_player['debut'] = st.selectbox('Which club sold him outside of the RTD Group?', [
                                             'FCN', 'SDFC'], key="debut", index=['FCN', 'SDFC'].index(extra_player['debut']))

        a_starting = extra_player['playing_time_1000s']['FCN']
        if a_starting == None:
            a_starting = 0
        else:
            a_starting = int(round(a_starting * 1000, -2))

        a = st.slider(
            'How many senior minutes did the player play for FCN?', 0, 15000, step=100, key="mins_fcn", value=a_starting)
        if a == 0:
            a = None

        if a:
            a = a / 1000
        extra_player['playing_time_1000s']['FCN'] = a

    with sold_col:
        extra_player['sold_from'] = st.selectbox('Where did he make his debut?', [
            'FCN', 'SDFC'], key="sold_from", index=['FCN', 'SDFC'].index(extra_player['sold_from']))

        b_starting = extra_player['playing_time_1000s']['SDFC']
        if b_starting == None:
            b_starting = 0
        else:
            b_starting = int(round(b_starting * 1000, -2))

        b = st.slider(
            'How many senior minutes did the player play for SDFC?', 0, 15000, step=100, key="mins_sdfc", value=b_starting)
        if b == 0:
            b = None

        if b:
            b = b / 1000
        extra_player['playing_time_1000s']['SDFC'] = b

    player_list = []
    if st.button("Add Player to Examples"):

        new_player = Player(
            title=extra_player['title'],
            slider_key=extra_player['slider_key'],
            debut=extra_player['debut'],
            name=extra_player['name'],
            scouted_by=extra_player['scouted_by'],
            scouted_age=extra_player['scouted_age'],
            sold_for=extra_player['sold_for'],
            sold_from=extra_player['sold_from'],
            pre_16=extra_player['pre_16'],
            post_16=extra_player['post_16'],
            playing_time_1000s=extra_player['playing_time_1000s']
        )

        players_class.append(new_player)
        st.write(players_class)


with examples:

    player_idx = st.selectbox(
        'Choose a player as an example...',
        options=list(range(len(players_class))),
        format_func=lambda idx: players_class[idx].title
    )

    pc = players_class[player_idx]

    st.header(pc)
    st.write(pc.summary_text())
    pc.trigger_calcs(calibrations, pc.sold_for)

    fee = st.slider('Simulated Transfer Profit (€m)',
                    min_value=0.0,
                    max_value=10.0,
                    value=pc.sold_for,
                    step=0.25,
                    key=pc.slider_key)

    st.markdown("<br>", unsafe_allow_html=True)
    fees = pc.get_fees(fee)

    club_met_1, club_met_2 = st.columns(2)

    with club_met_1:
        st.markdown(logos['fcn'],
                    unsafe_allow_html=True)
        st.markdown(get_fiat_text(fees['fcn']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.fcn, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.fcn_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with club_met_2:
        st.markdown(logos['sdfc'],
                    unsafe_allow_html=True)
        st.markdown(get_fiat_text(
            fees['sdfc']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.sdfc, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.sdfc_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    acad_met_1, acad_met_2, acad_met_3, acad_met_4 = st.columns(4)

    with acad_met_1:
        st.markdown(logos['rtd_g'], unsafe_allow_html=True)
        st.markdown(get_fiat_text(
            fees['rtd_g']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.rtd_g, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.rtd_g_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with acad_met_2:
        st.markdown(logos['rtd_d'], unsafe_allow_html=True)
        st.markdown(get_fiat_text(
            fees['rtd_d']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.rtd_d, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.rtd_d_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with acad_met_3:
        st.markdown(logos['rtd_e'], unsafe_allow_html=True)
        st.markdown(get_fiat_text(
            fees['rtd_e']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.rtd_e, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.rtd_e_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with acad_met_4:
        st.markdown(logos['rtd_u'], unsafe_allow_html=True)
        st.markdown(get_fiat_text(
            fees['rtd_u']), unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(pc.r.rtd_u, 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(pc.r.rtd_u_share*100, 2))) + "% share</p>", unsafe_allow_html=True)

    st.markdown('''---''')


for css_text in get_css():
    st.markdown(css_text, unsafe_allow_html=True)


st.session_state.players_class = players_class
