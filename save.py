# Import Packages
import streamlit as st
import pandas as pd
from random import randint
from matplotlib import pyplot as plt
from utils import calculate_points, create_summary_text, get_css, create_logos, Player
from players import get_players
from settings import get_initial_values

initial_vals = get_initial_values()
players = get_players()
logos = create_logos()

for css_text in get_css():
    st.markdown(css_text, unsafe_allow_html=True)


# App
st.header('Value Distribution Model')
intro, setttings, examples = st.tabs(
    ["Introduction", "Settings", "Examples"])


with intro:

    st.subheader('Model Introduction')
    intro_col1, intro_col2 = st.columns([3, 2])
    with intro_col1:
        st.write('When players transfer between the clubs and academies owned or operated by the Right to Dream Group they do so at no acquisition cost for the acquiring club. However, in the result of a player being transferred to a club outside of the Right to Dream Group; the fee, if any, is fairly distributed to the Right to Dream clubs and academies that contributed to their development. Such a mechanism encourages collaboration between Right to Dream organisations in player trading and succession planning. The Value Distribution Model (VDM) is used to calculate the distribution of transfer profits (net of acquistion costs).')
    with intro_col2:
        st.image(
            'https://www.espldaily.com/wp-content/uploads/2021/07/219363963_911524162735780_1056505399119593431_n.jpg')

    st.write('new paraolutpat enim vel justo venenatis lobortis. Aenean accumsan pretium lectus, ut maximus orci gravida a. Sed nec quam id libero consequat eleifend a ac arcu. Etiam hendrerit mollis tellus, malesuada tristique magna congue in. Curabitur euismod nec ex quis porta. Mauris id consequat massa. Donec finibus nec purus quis consectetur. Vivamus facilisis tincidunt tellus id hendrerit. Mauris in pharetra magna, venenatis euismod mi. Cras vehicula sollicitudin venenatis. Vestibulum id suscipit velit, a pellentesque metus.')

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
    st.write("**blah**")
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
    st.write("blah blah")
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
    st.write("blah blah")
    with st.expander("Expand to Change Professional Debut Points"):
        debut_points = st.slider(
            '', min_value=0, max_value=10, value=initial_vals['debut'])

    st.subheader('**5. Senior Playing Time (per 1000 minutes)**')
    st.write("blah blah")
    with st.expander("Expand to Change Senior Playing Time Points"):
        playing_time = st.slider(
            'Playing Time', min_value=0, max_value=10, value=initial_vals['playing_time'])

    st.subheader('**6. Sold By**')
    st.write("blah blah")
    with st.expander("Expand to Change Sold By Points"):
        sold_by_points = st.slider(
            'Sold By', min_value=0, max_value=10, value=initial_vals['sold_by'])


def create_example(player):

    st.markdown('<p class="big-font">' +
                player['title'] + '</p>', unsafe_allow_html=True)
    example1_col1, example1_col2, example_col3 = st.columns([1, 6, 1])
    with example1_col1:
        st.write(" ")
    with example1_col2:
        st.write(create_summary_text(player))
        if player['sold_for']:
            player['sold_for'] = st.slider('Simulated Transfer Profit (€m)',
                                           min_value=0.0,
                                           max_value=10.0,
                                           value=player['sold_for'],
                                           step=0.25,
                                           key=player['slider_key'])
        else:
            player['sold_for'] = st.slider('Simulated Transfer Profit (€m)',
                                           min_value=0.0,
                                           max_value=10.0,
                                           value=1.0,
                                           step=0.25,
                                           key=player['slider_key'])
    with example_col3:
        st.write(" ")

    st.markdown("<br>", unsafe_allow_html=True)
    # rtd_points, fcn_points, sdfc_points, rtd_share, fcn_share, sdfc_share
    player_calculated = calculate_points(player,
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
                                         _21_points)

    met_col1, met_col2, met_col3 = st.columns(3)

    with met_col1:
        st.markdown(logos['rtd'],
                    unsafe_allow_html=True)
        st.markdown('<p class="big-font">€' +
                    str(round(player_calculated['rtd_share'], 2)) + 'm</p>', unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(player_calculated['rtd_points'], 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(player_calculated['rtd_pct_share']*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with met_col2:
        st.markdown(logos['fcn'],
                    unsafe_allow_html=True)
        st.markdown('<p class="big-font">€' +
                    str(round(player_calculated['fcn_share'], 2)) + 'm</p>', unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(player_calculated['fcn_points'], 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(player_calculated['fcn_pct_share']*100, 2))) + "% share</p>", unsafe_allow_html=True)

    with met_col3:
        st.markdown(logos['sdfc'],
                    unsafe_allow_html=True)
        st.markdown('<p class="big-font">€' +
                    str(round(player_calculated['sdfc_share'], 2)) + 'm</p>', unsafe_allow_html=True)
        st.markdown('<p class="light-font">' + str(int(round(player_calculated['sdfc_points'], 0))) + ' points' + "&nbsp | &nbsp" +
                    str(int(round(player_calculated['sdfc_pct_share']*100, 2))) + "% share</p>", unsafe_allow_html=True)

    st.markdown('''---''')


with examples:
    # st.markdown('<p class="yoyo-font">Numerous examples to get a feel of the output of the model</p>',
    #             unsafe_allow_html=True)

    francis_real, francis_sim, xavier, simon = st.tabs(
        [p['title'] for p in players])

    with francis_real:
        create_example(players[0])

    with francis_sim:
        create_example(players[1])

    with xavier:
        create_example(players[2])

    with simon:
        create_example(players[3])

    # for player in players:
    #     create_example(player)

        # if rtd_share > 0:

        #     if fcn_share > 0:

        #         if sdfc_share > 0:
        #             plt.clf()   # Clear figure
        #             plt.rcParams["figure.figsize"] = plot_dimensions
        #             plt.rcParams["figure.autolayout"] = True
        #             plt.barh([" "], [rtd_share, fcn_share, sdfc_share],
        #                      left=[0, rtd_share, (rtd_share+fcn_share)], color=[rtd_hex, fcn_hex, sdfc_hex])
        #             plt.axis('off')
        #             plt.annotate('€' + str(round(rtd_share, 2)) + 'm | ' + str(
        #                 round((rtd_share/player['sold_for'])*100, 2)) + "%", (0.055, y_offset), xycoords="figure fraction", fontsize='small', color="white", fontweight="bold")
        #             plt.annotate('€' + str(fcn_share) + 'm | ' + str(
        #                 fcn_share/player['sold_for']) + "%", (rtd_share/player['sold_for']-0.055, y_offset), xycoords="figure fraction")
        #             st.pyplot(plt)

        #         else:
        #             st.write('no sdfc')

        #             plt.clf()   # Clear figure
        #             plt.rcParams["figure.figsize"] = plot_dimensions
        #             plt.rcParams["figure.autolayout"] = True
        #             plt.barh([" "], [rtd_share, fcn_share],
        #                      left=[0, rtd_share], color=[rtd_hex, fcn_hex])
        #             plt.axis('off')
        #             plt.annotate(
        #                 '€' + str(player['sold_for']*rtd_share) + 'm | ' + str(rtd_share) + "%", (0.0, 0.5), xycoords="figure fraction")
        #             st.pyplot(plt)
# with tab1:
#     calculate_points(players[0])

# with tab2:
#     st.write('tab 2')
